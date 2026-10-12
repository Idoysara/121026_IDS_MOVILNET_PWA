#!/usr/bin/env python3
"""
core/webhook_noise_filter.py — Guardián de Frontera y Filtro de Ruido para Webhooks
===================================================================================
Proyecto: AI_Movilnet_300926 — Telecomunicaciones Movilnet C.A.
Gobernanza: Universal Best Practices Engineering Rule (Pilares I al VII) & Protocolo Decagonal

Problema que Resuelve (Hallazgo Forense):
Durante la auditoría de ejecuciones en n8n Cloud se detectó que Evolution API envía eventos
secundarios masivos al webhook central:
  - 'presence.update': Se disparó 6 veces en 10 segundos (#13099 a #13104).
  - 'contacts.update': Disparado en cada interacción (#13096).
  - 'send.message': Eco emitido por Baileys al responder el bot (#13098).
Aunque el nodo Switch los frena antes de Gemini, saturan la cola de trabajo de n8n con cientos de
ejecuciones inútiles por hora.

Solución de Ingeniería:
1. Filtro estricto en la frontera (Edge Filter) que evalúa el payload crudo en <1ms.
2. Descarta inmediatamente ecos del bot (fromMe == True).
3. Descarta eventos que no contienen contenido conversacional (presence, contacts, chats).
4. Aprueba únicamente mensajes auténticos con texto, audio, imagen o documentos.
5. CLI autónomo con auto-verificación formal (--test, --demo).
"""

from __future__ import annotations

import sys
import argparse
from typing import Dict, Any, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class FilterVerdict(str, Enum):
    PASS_MESSAGE = "PASS_MESSAGE"
    DROP_FROM_ME_ECHO = "DROP_FROM_ME_ECHO"
    DROP_PRESENCE_UPDATE = "DROP_PRESENCE_UPDATE"
    DROP_CONTACTS_UPDATE = "DROP_CONTACTS_UPDATE"
    DROP_CHATS_UPDATE = "DROP_CHATS_UPDATE"
    DROP_EMPTY_CONTENT = "DROP_EMPTY_CONTENT"
    DROP_UNKNOWN_EVENT = "DROP_UNKNOWN_EVENT"


@dataclass
class FilterResult:
    should_process: bool
    verdict: FilterVerdict
    reason: str
    event_type: str
    sender_jid: Optional[str] = None
    extracted_text: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class WebhookNoiseFilter:
    """Filtro de Ruido de Alta Velocidad para Webhooks de WhatsApp / Baileys."""

    ALLOWED_EVENTS = {"messages.upsert", "messages.update"}

    @classmethod
    def evaluate(cls, raw_payload: Dict[str, Any]) -> FilterResult:
        """
        Evalúa de forma determinista el payload recibido del webhook.
        Retorna FilterResult indicando si debe procesarse o descartarse en el borde.
        """
        if not isinstance(raw_payload, dict):
            return FilterResult(
                should_process=False,
                verdict=FilterVerdict.DROP_EMPTY_CONTENT,
                reason="Payload no es un diccionario JSON válido",
                event_type="INVALID"
            )

        # 1. Inspección del evento principal
        event = raw_payload.get("event", "")
        data = raw_payload.get("data", {})

        # Si el evento no está en los permitidos
        if event == "presence.update":
            return FilterResult(
                should_process=False,
                verdict=FilterVerdict.DROP_PRESENCE_UPDATE,
                reason="Evento de presencia (online/typing) no contiene mensajes",
                event_type=event
            )
        elif event == "contacts.update":
            return FilterResult(
                should_process=False,
                verdict=FilterVerdict.DROP_CONTACTS_UPDATE,
                reason="Evento de sincronización de contactos no contiene mensajes",
                event_type=event
            )
        elif event == "chats.update":
            return FilterResult(
                should_process=False,
                verdict=FilterVerdict.DROP_CHATS_UPDATE,
                reason="Evento de actualización de chat no contiene mensajes",
                event_type=event
            )
        elif event and event not in cls.ALLOWED_EVENTS and event != "send.message":
            return FilterResult(
                should_process=False,
                verdict=FilterVerdict.DROP_UNKNOWN_EVENT,
                reason=f"Evento '{event}' no admitido en el pipeline conversacional",
                event_type=event
            )

        # 2. Manejo de 'data' (puede ser lista o dict)
        message_data = data[0] if isinstance(data, list) and len(data) > 0 else data
        if not isinstance(message_data, dict):
            return FilterResult(
                should_process=False,
                verdict=FilterVerdict.DROP_EMPTY_CONTENT,
                reason="Objeto data vacío o malformado",
                event_type=event or "UNKNOWN"
            )

        key = message_data.get("key", {})
        # 3. Detección y descarte de eco propio (fromMe == True)
        from_me = key.get("fromMe", False) or raw_payload.get("fromMe", False)
        if from_me is True:
            return FilterResult(
                should_process=False,
                verdict=FilterVerdict.DROP_FROM_ME_ECHO,
                reason="Mensaje saliente generado por el bot (fromMe=True), descartado para evitar bucles",
                event_type=event or "send.message",
                sender_jid=key.get("remoteJid")
            )

        # 4. Extracción de contenido conversacional
        message = message_data.get("message", {})
        sender_jid = key.get("remoteJid") or raw_payload.get("sender")

        text = (
            message.get("conversation")
            or message.get("extendedTextMessage", {}).get("text")
            or message.get("imageMessage", {}).get("caption")
            or message.get("videoMessage", {}).get("caption")
            or ""
        )

        has_media = bool(
            message.get("audioMessage")
            or message.get("imageMessage")
            or message.get("videoMessage")
            or message.get("documentMessage")
        )

        if not text and not has_media:
            return FilterResult(
                should_process=False,
                verdict=FilterVerdict.DROP_EMPTY_CONTENT,
                reason="Payload no contiene texto ni archivos multimedia procesables",
                event_type=event or "EMPTY",
                sender_jid=sender_jid
            )

        return FilterResult(
            should_process=True,
            verdict=FilterVerdict.PASS_MESSAGE,
            reason="Mensaje de abonado válido para procesamiento",
            event_type=event or "messages.upsert",
            sender_jid=sender_jid,
            extracted_text=text
        )


def main():
    parser = argparse.ArgumentParser(description="Filtro de Ruido de Frontera para Webhooks WhatsApp")
    parser.add_argument("--test", action="store_true", help="Ejecutar suite formal de pruebas")
    parser.add_argument("--demo", action="store_true", help="Demostración con eventos reales")
    args = parser.parse_args()

    if args.test:
        print("🧪 [TEST] Verificando WebhookNoiseFilter (Pilares I al VII)...")
        # Test 1: Descarte de presence.update
        p_presence = {"event": "presence.update", "data": {"id": "123@lid"}}
        r1 = WebhookNoiseFilter.evaluate(p_presence)
        assert r1.should_process is False
        assert r1.verdict == FilterVerdict.DROP_PRESENCE_UPDATE

        # Test 2: Descarte de contacts.update
        p_contacts = {"event": "contacts.update", "data": [{"remoteJid": "123@lid"}]}
        r2 = WebhookNoiseFilter.evaluate(p_contacts)
        assert r2.should_process is False
        assert r2.verdict == FilterVerdict.DROP_CONTACTS_UPDATE

        # Test 3: Descarte de eco saliente (fromMe == True)
        p_echo = {
            "event": "messages.upsert",
            "data": {
                "key": {"remoteJid": "584142554590@s.whatsapp.net", "fromMe": True},
                "message": {"conversation": "Respuesta enviada por el bot"}
            }
        }
        r3 = WebhookNoiseFilter.evaluate(p_echo)
        assert r3.should_process is False
        assert r3.verdict == FilterVerdict.DROP_FROM_ME_ECHO

        # Test 4: Pase de mensaje auténtico de cliente
        p_valid = {
            "event": "messages.upsert",
            "data": {
                "key": {"remoteJid": "584142554590@s.whatsapp.net", "fromMe": False},
                "message": {"conversation": "Hola, cuál es mi saldo?"}
            }
        }
        r4 = WebhookNoiseFilter.evaluate(p_valid)
        assert r4.should_process is True
        assert r4.verdict == FilterVerdict.PASS_MESSAGE
        assert r4.extracted_text == "Hola, cuál es mi saldo?"

        print("✅ [TEST PASS] Todos los invariantes de WebhookNoiseFilter aprobados con 100% de éxito.")
        return

    if args.demo:
        sample_presence = {"event": "presence.update", "data": {"id": "188364414275735@lid"}}
        sample_msg = {
            "event": "messages.upsert",
            "data": {
                "key": {"remoteJid": "584142650088@s.whatsapp.net", "fromMe": False},
                "message": {"conversation": "Buenas tardes, quiero recargar mi saldo"}
            }
        }
        res_p = WebhookNoiseFilter.evaluate(sample_presence)
        res_m = WebhookNoiseFilter.evaluate(sample_msg)
        print("\n🔬 Demostración de Filtrado de Frontera:")
        print(f"   Evento 1 (presence.update):   ¿Procesar?: {res_p.should_process} | Veredicto: {res_p.verdict.value}")
        print(f"   Evento 2 (Mensaje de texto):   ¿Procesar?: {res_m.should_process}  | Veredicto: {res_m.verdict.value} | Texto: '{res_m.extracted_text}'\n")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
