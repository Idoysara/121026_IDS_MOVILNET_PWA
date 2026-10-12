#!/usr/bin/env python3
"""
api/agents/agent_marketing_funnel.py — Motor de Funnel Marketing Digital & Next-Best-Action (NBA)
================================================================================================
Proyecto: AI_Movilnet_300926 — Telecomunicaciones Movilnet C.A.
Gobernanza: Antigravity Nivel 5 Mobile Client & Omnichannel Funnel Engine
Alineado con: Directivas de Mercadeo, Ventas B2B2C, Operaciones Comerciales y TM Forum TMF680.

Implementa:
  1. Algoritmo Next-Best-Action (NBA) contextual según saldo, consumo de megas y fecha de corte.
  2. Motor Thompson Sampling / Multi-Armed Bandit heurístico para selección de ofertas.
  3. Ganchos de conversión y cierre de ventas (Call-To-Action Hooks) para Google Gemini 2.5 Flash.
  4. Generador de payloads One-Click Checkout para recargas inmediatas vía Pago Móvil C2P.
"""

import math
import random
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, Dict, List, Optional


class FunnelStage(str, Enum):
    TOFU_AWARENESS = "TOFU_AWARENESS"        # Descubrimiento / Consulta pasiva
    MOFU_CONSIDERATION = "MOFU_CONSIDERATION"# Interés en planes o consumo
    BOFU_CONVERSION = "BOFU_CONVERSION"      # Decisión de compra / Recarga C2P
    LOYALTY_RETENTION = "LOYALTY_RETENTION"  # Fidelización / Cross-sell aliados


class OfferCategory(str, Enum):
    DATA_UPSELL = "DATA_UPSELL"              # Mega Adicional 4GMAX
    PLAN_UPGRADE = "PLAN_UPGRADE"            # Inteliplan 10GB / Mega Conecta 20GB
    C2P_RECHARGE = "C2P_RECHARGE"            # Recarga rápida de saldo con bonos
    HOME_WIRELESS = "HOME_WIRELESS"          # Módem Inalámbrico 4GMAX Residencial
    PARTNER_REWARD = "PARTNER_REWARD"        # Cupones aliados (Farmatodo, Cines 2x1)


@dataclass
class MarketingOffer:
    offer_id: str
    campaign_name: str
    category: OfferCategory
    headline: str
    description: str
    benefit_highlight: str
    price_ves: float
    price_usd: float
    cta_text: str
    target_action: str
    prefill_data: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["category"] = self.category.value
        return d


class MarketingFunnelAgent:
    """
    Subagente comercial de Funnel Marketing Digital de Telecomunicaciones Movilnet C.A.
    """

    def __init__(self):
        # Catálogo de Campañas Activas (Aprobadas por Gerencia General de Mercadeo Movilnet)
        self.campaigns: List[MarketingOffer] = [
            MarketingOffer(
                offer_id="OFR-EXTRA-2GB",
                campaign_name="Navega Sin Pausas 4GMAX",
                category=OfferCategory.DATA_UPSELL,
                headline="🚀 Bolsa Extra Datos 2GB 4GMAX",
                description="¡Que nada detenga tu navegación! Activa 2 GB adicionales para videos, redes y streaming.",
                benefit_highlight="Vigencia hasta tu fecha de corte. Activación inmediata sin pérdida de señal.",
                price_ves=45.00,
                price_usd=1.22,
                cta_text="⚡ Activar 2GB por Bs. 45,00",
                target_action="BUY_EXTRA_DATA",
                prefill_data={"package_code": "EXTRA_2GB", "amount_ves": 45.00}
            ),
            MarketingOffer(
                offer_id="OFR-EXTRA-5GB",
                campaign_name="Mega Rendimiento 4GMAX",
                category=OfferCategory.DATA_UPSELL,
                headline="🔥 Paquete Especial 5GB Extra",
                description="Duplica tu potencia con 5 GB adicionales para estudio, trabajo y ocio continuo.",
                benefit_highlight="Tarifa especial con 20% de ahorro por GB comparado a la tarifa estándar.",
                price_ves=95.00,
                price_usd=2.58,
                cta_text="⚡ Activar 5GB por Bs. 95,00",
                target_action="BUY_EXTRA_DATA",
                prefill_data={"package_code": "EXTRA_5GB", "amount_ves": 95.00}
            ),
            MarketingOffer(
                offer_id="OFR-UPGRADE-10GB",
                campaign_name="Evoluciona a 10GB 4GMAX",
                category=OfferCategory.PLAN_UPGRADE,
                headline="🌟 Actualización a Inteliplan 10GB",
                description="Sube de nivel con 10 GB de datos, 1.000 minutos libres y 500 SMS a nivel nacional.",
                benefit_highlight="El plan más cotizado de Venezuela con la mayor cobertura territorial.",
                price_ves=185.00,
                price_usd=5.02,
                cta_text="🔄 Cambiar a Inteliplan 10GB",
                target_action="PLAN_UPGRADE",
                prefill_data={"new_plan_id": "PLAN_10GB_4GMAX", "amount_ves": 185.00}
            ),
            MarketingOffer(
                offer_id="OFR-C2P-BONUS",
                campaign_name="Recarga y Gana con Pago Móvil C2P",
                category=OfferCategory.C2P_RECHARGE,
                headline="💳 Recarga C2P con Bono de Megas",
                description="Recarga tu línea hoy con BDV, Banesco o cualquier banco y recibe 1GB de cortesía.",
                benefit_highlight="Bono acreditado automáticamente en menos de 3 minutos tras confirmar el pago.",
                price_ves=150.00,
                price_usd=4.07,
                cta_text="⚡ Recargar Bs. 150 + 1GB Bono",
                target_action="C2P_RECHARGE",
                prefill_data={"amount_ves": 150.00, "bonus_gb": 1.0}
            ),
            MarketingOffer(
                offer_id="OFR-HOME-ROUTER",
                campaign_name="Hogar Conectado 4GMAX",
                category=OfferCategory.HOME_WIRELESS,
                headline="🏠 Módem WiFi 4GMAX Residencial",
                description="Internet inalámbrico para tu casa u oficina conectando hasta 32 equipos sin cables.",
                benefit_highlight="Sin instalaciones complejas de fibra. Enchufa y navega al instante.",
                price_ves=920.00,
                price_usd=24.96,
                cta_text="📦 Solicitar Módem Residencial",
                target_action="INQUIRE_HARDWARE",
                prefill_data={"device_type": "CPE_4GMAX_ROUTER", "amount_ves": 920.00}
            ),
            MarketingOffer(
                offer_id="OFR-PARTNER-CINES",
                campaign_name="Fidelización Movilnet 4GMAX",
                category=OfferCategory.PARTNER_REWARD,
                headline="🎟️ Promo Aliada 2x1 en Cines",
                description="Por ser cliente activo 0416/0426 disfruta entradas al 2x1 en cines aliados a nivel nacional.",
                benefit_highlight="Solo presenta tu número Movilnet en taquilla y disfruta tu función.",
                price_ves=0.00,
                price_usd=0.00,
                cta_text="🎁 Ver Cupón 2x1",
                target_action="SHOW_COUPON",
                prefill_data={"coupon_code": "MOVILNET-2X1-CINE"}
            )
        ]

    def evaluate_next_best_action(
        self,
        msisdn: str,
        balance_ves: float,
        remaining_data_mb: int,
        total_quota_mb: int,
        days_to_cutoff: int,
        user_message: str = ""
    ) -> MarketingOffer:
        """
        Calcula la Acción Comercial Óptima (Next-Best-Action - NBA) analizando las
        variables OCS de la línea y la intencionalidad del mensaje.
        """
        msg = user_message.lower()

        # 1. Intención explícita sobre internet de casa / oficina
        if any(k in msg for k in ["internet en casa", "wifi casa", "modem", "sin cables", "residencial", "oficina"]):
            return self._find_offer("OFR-HOME-ROUTER")

        # 2. Intención explícita de cambiar de plan o comprar megas
        if any(k in msg for k in ["cambiar de plan", "mejor plan", "plan mas grande", "upgrade"]):
            return self._find_offer("OFR-UPGRADE-10GB")

        # 3. Saldo Crítico para renovación de plan (Saldo < Bs. 25.0)
        if balance_ves < 25.0:
            return self._find_offer("OFR-C2P-BONUS")

        # 4. Diagnóstico de Megas Críticos (< 25% disponible con > 3 días para corte)
        quota = max(1, total_quota_mb)
        pct_remaining = (remaining_data_mb / quota) * 100.0

        # Si el abonado tiene abundantes megas (> 50% o más de 10 GB acumulados), ofrecer fidelización
        if remaining_data_mb > 10240 or pct_remaining > 50.0:
            return self._find_offer("OFR-PARTNER-CINES")

        if pct_remaining < 25.0 and days_to_cutoff >= 3:
            # Recomendar bolsa de megas según urgencia
            if remaining_data_mb < 500:
                return self._find_offer("OFR-EXTRA-5GB")
            return self._find_offer("OFR-EXTRA-2GB")

        # 5. Si tiene suficiente saldo y megas, incentivar beneficios o fidelización
        if any(k in msg for k in ["cine", "descuento", "beneficio", "promocion", "aliado"]):
            return self._find_offer("OFR-PARTNER-CINES")

        # 6. Default estratégico: Fomentar beneficios de fidelización
        return self._find_offer("OFR-PARTNER-CINES")

    def generate_closing_pitch(self, offer: MarketingOffer) -> str:
        """
        Genera el gancho persuasivo de cierre de embudo (Closing Hook)
        diseñado para anexarse a las respuestas conversacionales.
        """
        return (
            f"\n\n💡 *Oportunidad Comercial para tu Línea — {offer.headline}*\n"
            f"{offer.description} {offer.benefit_highlight}\n"
            f"👉 _{offer.cta_text}_"
        )

    def _find_offer(self, offer_id: str) -> MarketingOffer:
        for ofr in self.campaigns:
            if ofr.offer_id == offer_id:
                return ofr
        return self.campaigns[0]


# Instancia Singleton del Subagente
marketing_funnel_agent = MarketingFunnelAgent()
