#!/usr/bin/env python3
"""
tests/test_cazador_movilnet_integration.py — Pruebas de Integración E2E Cazador de Ofertas & Movilnet Core
========================================================================================================
Proyecto: AI_Movilnet_300926 — Telecomunicaciones Movilnet C.A.
Fase 5: Validación Transversal E2E (Chat WhatsApp -> FastPath -> Radar -> Cuponería -> Carrier Billing)
Gobernanza: Protocolo Decagonal Maestro & Cero Alucinación (Pilares I al VII)
"""

import json
import time
from pathlib import Path
import pytest

from core.fastpath_intent_interceptor import FastPathIntentInterceptor
from api.agents.agent_deals_scout import AgentDealsScout
from api.service import MovilnetAPIService
from services.cazador_ofertas.src.application.cazador_service import CazadorApplicationService
from services.cazador_ofertas.src.domain.invariants import CazadorInvariants, DomainInvariantViolationError
from services.cazador_ofertas.src.domain.entities import EstadoCupon


@pytest.fixture(scope="module")
def interceptor():
    return FastPathIntentInterceptor()


@pytest.fixture(scope="module")
def api_service():
    return MovilnetAPIService()


@pytest.fixture(scope="module")
def deals_scout():
    return AgentDealsScout()


# ============================================================================
# 1. FASTPATH & DETECCIÓN CONVERSACIONAL DE OFERTAS (WHATSAPP / PWA)
# ============================================================================

def test_fastpath_deals_cero_adivinacion_sin_ubicacion(interceptor):
    """
    Regla Cero Adivinación: Si el usuario pide ofertas sin indicar ubicación ni GPS,
    el bot NUNCA debe inventar locales ni asumir Caracas; debe pedir la zona amablemente.
    """
    res = interceptor.intercept("¿Cuáles promociones u ofertas tienen hoy?", "04169991122")

    assert res.can_intercept is True
    assert res.intent_detected == "CAZADOR_OFERTAS_CLUB"
    assert res.tokens_consumed == 0
    assert "indicas en qué ciudad o zona te encuentras" in res.response_text
    # Enlace oficial PWA universal
    assert "/ui/pwa_stitch/index.html" in res.response_text


def test_fastpath_deals_con_zona_chacao(interceptor):
    """
    Si el usuario indica 'ofertas en Chacao', el FastPath geocodifica la zona,
    encuentra comercios físicos y genera la respuesta con precios y Magic Link.
    """
    # Pre-calentar llamada para eliminar cold start
    interceptor.intercept("ofertas en Chacao", "04169991122")
    t0 = time.perf_counter()
    res = interceptor.intercept("Quiero ver ofertas en Chacao", "04169991122")
    lat_ms = (time.perf_counter() - t0) * 1000.0

    assert res.can_intercept is True
    assert res.intent_detected == "CAZADOR_OFERTAS_CLUB"
    assert res.tokens_consumed == 0
    assert lat_ms < 50.0  # Carrier-grade latency sub-50ms en caliente
    assert "¡Club 4GMAX Activado!" in res.response_text
    assert "Bs" in res.response_text
    assert "reclamar tu cupón" in res.response_text.lower() or "1-tap" in res.response_text.lower()
    # Verifica presencia de Magic Link
    assert "sig=" in res.response_text
    # Sufijo PWA universal
    assert "/ui/pwa_stitch/index.html" in res.response_text


def test_fastpath_deals_con_gps_directo(interceptor):
    """
    Envío de coordenadas GPS directas resuelve las ofertas más cercanas por Haversine.
    """
    # Coordenadas Plaza Francia Altamira
    lat_altamira = 10.4965
    lon_altamira = -66.8490
    res = interceptor.intercept(
        message_text="ofertas cerca de mi",
        phone_number="04161112233",
        latitude=lat_altamira,
        longitude=lon_altamira
    )

    assert res.can_intercept is True
    assert res.intent_detected == "CAZADOR_OFERTAS_CLUB"
    assert "¡Club 4GMAX Activado!" in res.response_text


# ============================================================================
# 2. SUBAGENTE SCOUT DE OFERTAS (SWARM L5)
# ============================================================================

def test_deals_scout_agent_execution(deals_scout):
    """Valida la ejecución formal del agente DealsScout."""
    res = deals_scout.scout_deals(
        phone="04169991122",
        message="ofertas en Las Mercedes",
        max_distancia_m=3000.0
    )
    assert res.success is True
    assert res.requiere_ubicacion is False
    assert res.total_ofertas > 0
    assert len(res.ofertas) > 0
    item = res.ofertas[0]
    assert item.precio_oferta_ves > 0
    assert item.descuento_pct >= 0


# ============================================================================
# 3. ENDPOINTS REST API MOVILNET CORE (:8010 VIA CAZADOR_ROUTER)
# ============================================================================

def test_api_rest_radar_ofertas_endpoint(api_service):
    """Endpoint GET /api/v1/cazador/ofertas debe responder con estructura de anillos."""
    status, headers, body = api_service.dispatch(
        method="GET",
        path="/api/v1/cazador/ofertas?lat=10.4925&lon=-66.8550&max_m=2000",
        headers={},
        body_bytes=b""
    )
    assert status == 200
    data = json.loads(body.decode("utf-8"))
    assert data["success"] is True
    assert "anillos" in data
    assert "zona_1_inmediata" in data["anillos"]
    assert data["total_comercios_en_rango"] > 0


def test_api_rest_ciclo_completo_cupon_y_billing(api_service):
    """
    Ciclo E2E completo:
    1. Reclamar cupón dinámico con MSISDN Movilnet.
    2. Verificar código TOTP y firma HMAC-SHA256.
    3. Canjear en caja POS.
    4. Liquidar Carrier Billing con Split 20/80.
    5. Bloqueo anti-replay: el segundo intento de canje DEBE fallar.
    """
    msisdn = f"0416{int(time.time() * 100) % 9000000 + 1000000}"
    oferta_id = "OFE-002"

    # 1. Reclamo
    req_body = json.dumps({"oferta_id": oferta_id, "msisdn": msisdn}).encode("utf-8")
    status_rec, _, body_rec = api_service.dispatch(
        method="POST",
        path="/api/v1/cazador/cupon/reclamar",
        headers={"Content-Type": "application/json"},
        body_bytes=req_body
    )
    assert status_rec == 201
    rec_data = json.loads(body_rec.decode("utf-8"))
    assert rec_data["success"] is True
    cupon = rec_data["cupon"]
    cupon_id = cupon["uuid"]
    comercio_id = cupon["comercio_id"]
    firma = cupon["firma_hmac"]
    assert len(cupon["codigo_dinamico"]) > 0
    assert cupon["codigo_dinamico"].startswith("QRO-")

    # 2. Canje exitoso en POS
    canje_body = json.dumps({
        "cupon_id": cupon_id,
        "msisdn": msisdn,
        "comercio_id": comercio_id,
        "firma_hmac": firma
    }).encode("utf-8")

    status_canje, _, body_canje = api_service.dispatch(
        method="POST",
        path="/api/v1/cazador/cupon/canjear",
        headers={"Content-Type": "application/json"},
        body_bytes=canje_body
    )
    assert status_canje == 200
    canje_data = json.loads(body_canje.decode("utf-8"))
    assert canje_data["success"] is True
    assert canje_data["estado"] == "CANJEADO"

    # 3. Liquidación Carrier Billing Split 20/80
    monto_oferta = rec_data["oferta"]["precio_oferta_ves"]
    idemp_key = f"IDEMP-E2E-{cupon_id}-{int(time.time())}"
    bill_body = json.dumps({
        "msisdn": msisdn,
        "monto_ves": monto_oferta,
        "idempotency_key": idemp_key
    }).encode("utf-8")

    status_bill, _, body_bill = api_service.dispatch(
        method="POST",
        path="/api/v1/cazador/billing",
        headers={"Content-Type": "application/json"},
        body_bytes=bill_body
    )
    assert status_bill == 200
    bill_data = json.loads(body_bill.decode("utf-8"))
    assert bill_data["success"] is True
    tx = bill_data["transaccion"]
    # Validar invariante del split 20/80
    assert tx["comision_telco_ves"] == round(monto_oferta * 0.20, 2)
    assert tx["neto_comercio_ves"] == round(monto_oferta * 0.80, 2)
    assert abs((tx["comision_telco_ves"] + tx["neto_comercio_ves"]) - monto_oferta) < 0.02

    # 4. Blindaje Anti-Replay: Segundo intento de canje con la misma firma debe ser rechazado
    status_replay, _, body_replay = api_service.dispatch(
        method="POST",
        path="/api/v1/cazador/cupon/canjear",
        headers={"Content-Type": "application/json"},
        body_bytes=canje_body
    )
    assert status_replay in (409, 422)
    replay_data = json.loads(body_replay.decode("utf-8"))
    assert "CANJEADO" in replay_data.get("message", "") or "Transición de estado ilegal" in replay_data.get("message", "")


def test_api_rest_magic_link_endpoint(api_service):
    """Endpoint GET /api/v1/cazador/magic-link debe retornar link firmado."""
    status, _, body = api_service.dispatch(
        method="GET",
        path="/api/v1/cazador/magic-link?msisdn=04161234567&oferta_id=OFE-001",
        headers={},
        body_bytes=b""
    )
    assert status == 200
    data = json.loads(body.decode("utf-8"))
    assert data["success"] is True
    assert "sig=" in data["magic_link"]
    assert data["zero_rating"] is True
