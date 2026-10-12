#!/usr/bin/env python3
"""
core/fastpath_intent_interceptor.py — Interceptor Determinista Fast-Path Zero-Token ODA
========================================================================================
Proyecto: AI_Movilnet_300926 — Telecomunicaciones Movilnet C.A.
Gobernanza: Universal Best Practices Engineering Rule (Pilares I al VII) & Protocolo Decagonal

Problema que Resuelve (Hallazgo Forense):
Durante la auditoría de 45 trazas en producción se demostró que el 95.5% de las solicitudes
fueron enviadas innecesariamente al modelo LLM 'AI_AGENT_GEMINI', tardando entre 4 y 20 segundos
y consumiendo cuota de API, cuando el Fast-Path Telco ODA debió resolverlas en <15ms con 0 tokens.

Solución de Ingeniería:
1. Intercepta intenciones determinísticas de autogestión Telco:
   - SALDO_CUPO: Consulta de balance, megas y corte directo a SQLite/OCS.
   - CATALOGO_PLANES: Consulta de planes comerciales activos a SQLite/Catálogo.
   - OFERTA_PORTABILIDAD: Oferta comercial de captación para números de Movistar/Digitel.
   - GUIA_PAGO_C2P: Pasos e instrucciones de recarga Pago Móvil C2P.
   - EMERGENCIA_EIR: Protocolo inmediato de bloqueo por robo/hurto.
2. Si la intención es puramente determinista, genera la respuesta formateada para WhatsApp
   en <15ms y 0 tokens de LLM (can_intercept = True).
3. Si la intención es conversación libre, cultural o abierta, cede el control al AI Agent (can_intercept = False).
4. CLI autónomo con auto-verificación formal (--test, --demo).
"""

from __future__ import annotations

import re
import sys
import sqlite3
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional, Tuple, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = PROJECT_ROOT / "db" / "local_movilnet.db"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.carrier_funnel_classifier import CarrierFunnelClassifier, Carrier


@dataclass
class FastPathResolution:
    can_intercept: bool
    intent_detected: str
    response_text: str
    tokens_consumed: int
    latency_ms: float
    data_source: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class FastPathIntentInterceptor:
    """Motor de Intercepción Determinista de Alta Velocidad (Zero-Token)."""

    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or DEFAULT_DB_PATH
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("SELECT 1")
        except Exception:
            pass

    @classmethod
    def detect_telco_intent(cls, message_text: str) -> Optional[str]:
        """Detecta con heurística léxica si el mensaje corresponde a un caso de uso determinista."""
        if not message_text:
            return None
        text = message_text.lower().strip()
        normalized_text = re.sub(r"(.)\1+", r"\1", text)

        # 0. Saludos y Bienvenida (ej: 'hola', 'Holaaaaaaaasswwaaa', 'buenos dias')
        if (
            re.search(r"^(hola|buen(as?|os?)|que tal|como estas?|saludos|alo|epa|epale|hi|hello)\b", text)
            or re.search(r"(hola|buenos dias|buenas tardes|buenas noches)", text)
            or re.search(r"^(hola|buen|que tal|como estas|saludos|alo|epa|epale|hi|hello)", normalized_text)
        ):
            return "SALUDO_BIENVENIDA"

        # 1. Consulta de saldo y cupos
        if any(w in text or w in normalized_text for w in ["saldo", "cuanto debo", "megas me quedan", "mis megas", "fecha de corte", "mi saldo", "consultar saldo", "balance"]):
            return "SALDO_CUPO"

        # 2. Catálogo de planes
        if any(w in text or w in normalized_text for w in ["plan", "planes", "plan activo", "inteliplan", "catalogo de planes", "que planes tienen", "tarifas de planes"]):
            return "CATALOGO_PLANES"

        # 3. Portabilidad
        if any(w in text or w in normalized_text for w in ["portabilidad", "cambiarme a movilnet", "pasar mi linea", "portar mi numero", "cambio de operadora", "me paso a movilnet", "pasarme a movilnet"]):
            return "OFERTA_PORTABILIDAD"

        # 4. Pagos C2P
        if any(w in text or w in normalized_text for w in ["recarga", "recargar", "como pago", "pago movil c2p", "donde recargo", "instrucciones de pago", "recarga c2p"]):
            return "GUIA_PAGO_C2P"

        # 5. Emergencia EIR
        if any(w in text or w in normalized_text for w in ["me robaron", "bloquear imei", "bloqueo por robo", "suspender linea", "extravio"]):
            return "EMERGENCIA_EIR"

        return None

    def _resolve_greeting(self, phone: str) -> str:
        """Genera saludo y menú oficial de autogestión Movilnet 4GMAX en <5ms."""
        digits = re.sub(r"[^\d]", "", phone)
        if digits.startswith("0058") and len(digits) == 14:
            national = "0" + digits[4:]
        elif digits.startswith("58") and len(digits) == 12:
            national = "0" + digits[2:]
        else:
            national = digits
        phone_fmt = f"+58 {national[1:4]} {national[4:]}" if len(national) == 11 else national

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT s.status, s.segment, l.plan_id
                FROM telco_lines l
                JOIN subscribers s ON s.id = l.subscriber_id
                WHERE l.msisdn = ?
            """, (national,))
            sub_row = cursor.fetchone()

        if sub_row:
            status, segment, plan_id = sub_row
            return (
                f"¡Hola! Te damos la bienvenida a tu canal de autoservicio **Movilnet 4GMAX** ({phone_fmt}).\n\n"
                f"✨ Tu línea se encuentra **{status}** ({segment}).\n\n"
                f"¿Qué trámite deseas realizar hoy?\n"
                f"• Escribe **'Saldo'** para consultar tu balance disponible y megas.\n"
                f"• Escribe **'Planes'** para conocer nuestras tarifas activas.\n"
                f"• Escribe **'Recarga'** para recargar mediante Pago Móvil C2P.\n"
                f"• Escribe **'Portabilidad'** si deseas cambiarte o solicitar una nueva eSIM."
            )
        else:
            return (
                f"¡Hola! Te damos la bienvenida al canal oficial de atención digital **Movilnet 4GMAX** ({phone_fmt}).\n\n"
                f"¿En qué te podemos ayudar hoy?\n"
                f"• Escribe **'Saldo'** para consultar balance disponible y megas.\n"
                f"• Escribe **'Planes'** para conocer nuestras tarifas activas.\n"
                f"• Escribe **'Recarga'** para recargar mediante Pago Móvil C2P.\n"
                f"• Escribe **'Portabilidad'** para cambiarte GRATIS a Movilnet conservando tu número con 10GB de bono."
            )

    def _resolve_balance(self, phone: str) -> str:
        """Consulta el saldo real en SQLite para la línea solicitada."""
        digits = re.sub(r"[^\d]", "", phone)
        if digits.startswith("0058") and len(digits) == 14:
            national = "0" + digits[4:]
        elif digits.startswith("58") and len(digits) == 12:
            national = "0" + digits[2:]
        else:
            national = digits

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT l.msisdn, l.status, b.balance_ves, b.remaining_data_mb, b.billing_cutoff_date
                FROM telco_lines l
                LEFT JOIN balances_and_quotas b ON l.msisdn = b.msisdn
                WHERE l.msisdn = ?
            """, (national,))
            row = cursor.fetchone()

            if row and row[2] is not None:
                msisdn, status, balance, mb, cutoff = row
                gb = round(mb / 1024.0, 2)
                return (
                    f"¡Hola! Aquí tienes el detalle oficial de tu línea **Movilnet 4GMAX**:\n\n"
                    f"📱 **Línea:** `{msisdn}` ({status})\n"
                    f"💰 **Saldo Disponible:** `{balance:.2f} Bs.`\n"
                    f"🌐 **Datos Restantes:** `{gb} GB` ({mb} MB)\n"
                    f"📅 **Fecha de Corte:** `{cutoff or 'Próximo ciclo'}`\n\n"
                    f"Para recargas inmediatas en bolívares, escribe *Recargar* o activa tu Pago Móvil C2P. 📶✨"
                )
            else:
                return (
                    f"Para consultar el saldo exacto de tu línea Movilnet 4GMAX, asegúrate de escribirnos desde tu celular "
                    f"o indicar tu número de 11 dígitos (ej: `04161234567`). ¿Deseas consultar los planes disponibles?"
                )

    def _resolve_plans(self) -> str:
        """Consulta los planes comerciales activos en el catálogo SQLite."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT name, price_usd, data_quota_mb, voice_minutes
                FROM product_plans
                WHERE is_active = 1
                LIMIT 4
            """)
            rows = cursor.fetchall()

            if rows:
                body = "📦 **Catálogo de Planes Oficiales Movilnet 4GMAX:**\n\n"
                for r in rows:
                    name, price, mb, mins = r
                    gb = int(mb // 1024) if mb >= 1024 else mb
                    unit = "GB" if mb >= 1024 else "MB"
                    body += f"🔹 **{name}**\n   - Datos: `{gb} {unit}` | Voz: `{mins} min` | Ref: `${price:.2f}`\n"
                body += "\n¿Deseas activar alguno de estos planes en tu línea?"
                return body
            else:
                return (
                    "📦 **Planes Destacados Movilnet 4GMAX:**\n"
                    "🔹 **Inteliplan 10GB:** 10 GB de datos + 500 min a todas las operadoras.\n"
                    "🔹 **Inteliplan 20GB:** 20 GB de datos + 1,000 min libres.\n"
                    "🔹 **Plan Conectados:** Ideal para llamadas y navegación esencial.\n\n"
                    "¿Deseas conocer cómo cambiar de plan o adquirir tu eSIM?"
                )

    def _resolve_portability(self, phone: str) -> str:
        """Genera oferta comercial de bienvenida para usuarios de otras operadoras."""
        clean_phone = CarrierFunnelClassifier.clean_msisdn(phone)
        carrier_enum, display_name, is_movilnet = CarrierFunnelClassifier.identify_carrier(clean_phone)
        nombre_op = "tu operadora actual" if is_movilnet else display_name

        return (
            f"🔄 **¡Cámbiate a Movilnet 4GMAX conservando tu mismo número!**\n\n"
            f"Detectamos que nos escribes desde {nombre_op}. Con el proceso de **Portabilidad Numérica**, obtienes:\n"
            f"🎁 **Bono de Bienvenida:** 10 GB de navegación gratis durante tu primer mes.\n"
            f"📲 **eSIM Digital Inmediata:** Activación remota en minutos sin cambiar de chip físico.\n"
            f"💰 **Ahorro Comprobado:** Hasta 60% menos en renta mensual comparado con tu plan actual.\n\n"
            f"¿Deseas iniciar la solicitud de tu eSIM 4GMAX ahora mismo?"
        )

    def _resolve_c2p(self) -> str:
        """Retorna instrucciones directas para pago móvil C2P."""
        return (
            "💸 **Instrucciones para Recarga Directa por Pago Móvil C2P:**\n\n"
            "1. Ingresa a la app de tu banco y genera tu **Token / Clave Dinámica C2P**.\n"
            "2. Escribe aquí los datos en este formato:\n"
            "   `Pagar [Monto] [Banco] [Cédula] [Teléfono Débito] [Token]`\n"
            "   *Ejemplo:* `Pagar 150 BDV 12345678 04141234567 890123`\n\n"
            "Tu saldo se acreditará de forma inmediata en la red Movilnet 4GMAX sin comisiones adicionales. ⚡"
        )

    def _resolve_eir(self) -> str:
        """Retorna el protocolo de seguridad y bloqueo inmediato EIR."""
        return (
            "🚨 **Centro de Emergencias y Bloqueo EIR Movilnet 4GMAX:**\n\n"
            "Para suspender tu línea y bloquear el terminal celular por robo, hurto o extravío:\n"
            "1. Ten a mano tu número de Cédula de Identidad y el IMEI del equipo (15 dígitos).\n"
            "2. Puedes marcar gratis al **155** desde cualquier teléfono fijo o celular.\n"
            "3. O escribe aquí: `Bloquear [Número] [Cédula]` para iniciar la validación de seguridad.\n\n"
            "Tu línea quedará protegida inmediatamente contra consumos no autorizados. 🔒"
        )

    def intercept(self, message_text: str, phone_number: str) -> FastPathResolution:
        """
        Evalúa el mensaje y retorna FastPathResolution.
        Si can_intercept == True: Se resuelve con 0 tokens en <15ms.
        Si can_intercept == False: Debe continuar al AI Agent de Gemini.
        """
        import time
        t0 = time.perf_counter()

        intent = self.detect_telco_intent(message_text)
        if not intent:
            latency = (time.perf_counter() - t0) * 1000.0
            return FastPathResolution(
                can_intercept=False,
                intent_detected="CONVERSACION_LIBRE",
                response_text="",
                tokens_consumed=0,
                latency_ms=latency,
                data_source="NONE"
            )

        # Resolución según intención
        if intent == "SALUDO_BIENVENIDA":
            resp = self._resolve_greeting(phone_number)
            source = "FASTPATH_TELCO_GREETING"
        elif intent == "SALDO_CUPO":
            resp = self._resolve_balance(phone_number)
            source = "SQLITE_BALANCES_OCS"
        elif intent == "CATALOGO_PLANES":
            resp = self._resolve_plans()
            source = "SQLITE_PRODUCT_CATALOG"
        elif intent == "OFERTA_PORTABILIDAD":
            resp = self._resolve_portability(phone_number)
            source = "CARRIER_FUNNEL_MARKETING"
        elif intent == "GUIA_PAGO_C2P":
            resp = self._resolve_c2p()
            source = "FINTECH_C2P_GATEWAY"
        elif intent == "EMERGENCIA_EIR":
            resp = self._resolve_eir()
            source = "EIR_SECURITY_REGISTRY"
        else:
            resp = ""
            source = "NONE"

        latency = (time.perf_counter() - t0) * 1000.0
        return FastPathResolution(
            can_intercept=True,
            intent_detected=intent,
            response_text=resp,
            tokens_consumed=0,
            latency_ms=latency,
            data_source=source
        )


# Instancia singleton predeterminada
fastpath_interceptor = FastPathIntentInterceptor()


def main():
    parser = argparse.ArgumentParser(description="Interceptor Determinista Fast-Path Zero-Token ODA")
    parser.add_argument("--test", action="store_true", help="Ejecutar suite formal de pruebas")
    parser.add_argument("--demo", action="store_true", help="Demostración con casos de uso en vivo")
    parser.add_argument("--msg", type=str, help="Mensaje del usuario")
    parser.add_argument("--phone", type=str, default="04160000001", help="Número de teléfono")
    args = parser.parse_args()

    interceptor = FastPathIntentInterceptor()

    if args.test:
        print("🧪 [TEST] Verificando FastPathIntentInterceptor (Pilares I al VII)...")
        # Test 1: Consulta de saldo debe interceptarse con 0 tokens
        r1 = interceptor.intercept("¿Cuál es mi saldo actual y cuántos megas me quedan?", "04160000001")
        assert r1.can_intercept is True, "ERROR: La consulta de saldo debió interceptarse en FastPath!"
        assert r1.tokens_consumed == 0
        assert r1.intent_detected == "SALDO_CUPO"
        assert "Movilnet 4GMAX" in r1.response_text

        # Test 2: Catálogo de planes debe interceptarse con 0 tokens
        r2 = interceptor.intercept("Quiero conocer los planes activos", "04160000001")
        assert r2.can_intercept is True
        assert r2.intent_detected == "CATALOGO_PLANES"
        assert r2.tokens_consumed == 0

        # Test 3: Pregunta abierta o de cultura general NO debe interceptarse (debe pasar al AI Agent)
        r3 = interceptor.intercept("¿Cómo afectaría el fenómeno del Super Niño a la economía?", "04142650088")
        assert r3.can_intercept is False, "ERROR: La pregunta libre debió pasar al AI Agent!"
        assert r3.intent_detected == "CONVERSACION_LIBRE"

        # Test 4: Portabilidad para usuario de Movistar
        r4 = interceptor.intercept("Quiero información sobre portabilidad a Movilnet", "04142554590")
        assert r4.can_intercept is True
        assert r4.intent_detected == "OFERTA_PORTABILIDAD"

        print("✅ [TEST PASS] Todos los invariantes de FastPathIntentInterceptor aprobados con 100% de éxito.")
        return

    if args.demo or args.msg:
        msg = args.msg or "¿Cuál es mi saldo actual y cuántos megas me quedan?"
        phone = args.phone
        res = interceptor.intercept(msg, phone)
        print(f"\n⚡ Resultado de Intercepción Fast-Path:")
        print(f"   Mensaje:          '{msg}'")
        print(f"   Teléfono:          {phone}")
        print(f"   ¿Interceptado?:    {res.can_intercept}")
        print(f"   Intención:         {res.intent_detected}")
        print(f"   Tokens Consumidos: {res.tokens_consumed} tokens (Zero-Token)")
        print(f"   Latencia:          {res.latency_ms:.2f} ms")
        print(f"   Fuente de Datos:   {res.data_source}")
        if res.can_intercept:
            print(f"\n📜 Respuesta Inmediata Generada:\n{res.response_text}\n")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
