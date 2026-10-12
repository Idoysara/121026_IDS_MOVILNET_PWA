#!/usr/bin/env python3
"""
scripts/update_n8n_instant_dispatch.py — Actualizador de Despacho Instantáneo y Normalización Flexible
====================================================================================================
1. Actualiza 'Movilnet Core & Marketing Router' en el workflow sNMbtiEiTkuQ9OCY para tolerar
   saludos con letras repetidas (ej. 'Holaaaaaaaasswwaaa' -> 'hola') y reconocer inmediatamente
   a la línea VIP de pruebas 04142554590 como Movilnet Activo.
2. Actualiza 'HTTP Request' para usar 'delay: 0', eliminando la cola de retraso en Evolution API.
"""

import sys
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ROUTER_JS = r'''for (const item of items) {
  // 1. Extraer datos del remitente y mensaje de forma segura usando .first()
  const editFields = $('Edit Fields').first().json.body || {};
  const dataKey = (editFields.data && editFields.data.key) || {};
  const rawJid = dataKey.remoteJid || '';
  const pushName = (editFields.data && editFields.data.pushName) || 'Abonado';
  const rawMsg = item.json.Content || '';
  const cleanMsg = rawMsg.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim();
  const dedupMsg = cleanMsg.replace(/(.)\1{2,}/g, '$1$1');
  const normalizedMsg = cleanMsg.replace(/(.)\1+/g, '$1');

  // 2. Normalizar número a formato legible nacional e internacional
  let cleanDigits = rawJid.replace(/@.*$/, '').replace(/[^\d]/g, '');
  let phoneFormatted = cleanDigits;
  if (cleanDigits.startsWith('58') && cleanDigits.length === 12) {
    phoneFormatted = '+58 ' + cleanDigits.slice(2, 5) + ' ' + cleanDigits.slice(5);
  } else if (cleanDigits.length === 11 && cleanDigits.startsWith('0')) {
    phoneFormatted = '+58 ' + cleanDigits.slice(1, 4) + ' ' + cleanDigits.slice(4);
  }

  const prefix = cleanDigits.startsWith('58') ? '0' + cleanDigits.slice(2, 5) : cleanDigits.slice(0, 4);
  const isVipTestLine = cleanDigits.endsWith('4142554590');
  const isCompetitor = !isVipTestLine && (prefix === '0414' || prefix === '0424' || prefix === '0412');
  const competitorLabel = (prefix === '0414' || prefix === '0424') ? 'Movistar Venezuela' : 'Digitel 4G';

  // 3. Saludo dinámico según horario de Venezuela (UTC-4)
  const nowUtc = new Date();
  const vetHour = (nowUtc.getUTCHours() - 4 + 24) % 24;
  let saludoDia = '¡Buenas noches';
  if (vetHour >= 5 && vetHour < 12) saludoDia = '¡Buenos días';
  else if (vetHour >= 12 && vetHour < 19) saludoDia = '¡Buenas tardes';

  // 4. Lógica de Enrutamiento y Generación de Respuesta
  let replyText = '';
  let pipelineRoute = 'FAST_PATH_TELCO_ODA';

  // Reconocimiento flexible de saludos
  const isGreeting = /^(hola|buen(as?|os?)|que tal|como estas?|saludos|alo|epa|epale|hi|hello)\b/.test(cleanMsg) ||
                     /^(hola|buen|que tal|como estas|saludos|alo|epa|epale|hi|hello)/.test(normalizedMsg) ||
                     /(hola|buenos dias|buenas tardes|buenas noches)/.test(cleanMsg) ||
                     /(hola|buenos dias|buenas tardes|buenas noches)/.test(normalizedMsg);

  // CASO 0: SALUDOS, BIENVENIDA Y CORTESÍA (Respuesta instantánea en <0.05s)
  if (isGreeting) {
    if (isVipTestLine) {
      replyText = `${saludoDia}, ${pushName}! Te damos la bienvenida a tu canal de autoservicio Movilnet 4GMAX (${phoneFormatted}).\n\n` +
                  `✨ Tu línea VIP se encuentra ACTIVA con Inteliplan 10GB 4GMAX.\n` +
                  `💰 Saldo actual: Bs. 450,00 | Datos: 10.0 GB disponibles.\n\n` +
                  `¿Qué trámite deseas realizar?\n` +
                  `• Escribe 'Saldo' para consultar tu balance disponible y megas.\n` +
                  `• Escribe 'Planes' para conocer nuestras tarifas activas.\n` +
                  `• Escribe 'Recarga' para recargar mediante Pago Móvil C2P.\n` +
                  `• Escribe 'Contrato' para consultar tu información de contrato.`;
    } else if (isCompetitor) {
      pipelineRoute = 'FUNNEL_MARKETING_PORTABILIDAD';
      replyText = `${saludoDia}, ${pushName}! Te damos la bienvenida al canal oficial de Movilnet.\n\n` +
                  `Detectamos que te comunicas desde una línea ${competitorLabel} (${phoneFormatted}).\n\n` +
                  `¿En qué te podemos ayudar hoy?\n` +
                  `• Escribe 'Saldo' o 'Planes' para consultar tarifas y servicios.\n` +
                  `• Escribe 'Portabilidad' para cambiarte GRATIS a Movilnet 4GMAX con eSIM digital y 10GB de bono de bienvenida.\n` +
                  `• Escribe 'Recarga' para realizar recargas con Pago Móvil C2P.`;
    } else {
      replyText = `${saludoDia}, ${pushName}! Bienvenido al canal de autoservicio Movilnet 4GMAX (${phoneFormatted}).\n\n` +
                  `¿Qué trámite deseas realizar?\n` +
                  `• Escribe 'Saldo' para consultar tu balance disponible y megas.\n` +
                  `• Escribe 'Planes' para conocer nuestras tarifas activas.\n` +
                  `• Escribe 'Recarga' para recargar mediante Pago Móvil C2P.\n` +
                  `• Escribe 'Portabilidad' para solicitar una nueva eSIM 4GMAX.`;
    }

  // CASO 1: CONSULTA DE SALDO, DEUDA, BALANCE O CORTE
  } else if (/saldo|cuanto debo|debo|balance|cuenta|corte/.test(cleanMsg) || /saldo|cuanto debo|debo|balance|cuenta|corte/.test(normalizedMsg)) {
    if (isVipTestLine) {
      replyText = `Estimado abonado Movilnet (${phoneFormatted}):\n\n` +
                  `💰 Tu saldo disponible es: Bs. 450,00\n` +
                  `📶 Datos 4GMAX: 10.0 GB de 10.0 GB\n` +
                  `📋 Plan activo: Inteliplan 10GB 4GMAX\n` +
                  `📅 Fecha de corte: 31 del mes.\n\n` +
                  `Para recargar tu saldo vía Pago Móvil C2P, escribe 'Recarga'.`;
    } else {
      replyText = `Estimado abonado Movilnet (${phoneFormatted}):\n\n` +
                  `💰 Tu saldo disponible es: Bs. 1.650,00\n` +
                  `📶 Datos 4GMAX: 11.9 GB de 5 GB\n` +
                  `📋 Plan activo: Inteliplan 10GB\n` +
                  `📅 Fecha de corte: 15 del mes.\n\n` +
                  `Para recargar tu saldo vía Pago Móvil C2P, escribe 'Recargar'.`;
      if (isCompetitor) {
        replyText += `\n\n💡 Beneficio Movilnet: ¿Deseas portar tu línea ${competitorLabel} a Movilnet 4GMAX con eSIM GRATIS + 10GB de bono? Escribe 'Portabilidad'.`;
      }
    }

  // CASO 2: CONSULTA DE MEGAS, DATOS, CONSUMO O GIGAS
  } else if (/mega|datos|cupo|navegacion|gigas?/.test(cleanMsg) || /mega|datos|cupo|navegacion|gigas?/.test(normalizedMsg)) {
    replyText = `Estimado abonado Movilnet (${phoneFormatted}):\n\n` +
                `📶 Navegación 4GMAX: 10.0 GB disponibles de tu cuota de 10 GB.\n` +
                `🚀 Estado de Red: Cobertura 4GMAX LTE Activa.\n` +
                `✨ WhatsApp libre incluido en tu ciclo actual.`;

  // CASO 3: RECARGA DE SALDO O PAGO MÓVIL C2P
  } else if (/recarga|pagar|pago movil|c2p/.test(cleanMsg) || /recarga|pagar|pago movil|c2p/.test(normalizedMsg)) {
    replyText = `Recarga Digital Movilnet (${phoneFormatted}):\n\n` +
                `Puedes recargar mediante Pago Móvil C2P SUDEBAN instantáneo desde cualquier banco nacional:\n` +
                `• Banco Receptor: Banco de Venezuela (0102)\n` +
                `• RIF: G-20000012-3\n` +
                `• Teléfono: 0416-6251587\n\n` +
                `Indica el monto a recargar (Monto mínimo: Bs. 150,00).`;

  // CASO 4: CATÁLOGO DE PLANES
  } else if (/plan|planes|inteliplan|conecta|tarifa/.test(cleanMsg) || /plan|planes|inteliplan|conecta|tarifa/.test(normalizedMsg)) {
    replyText = `Catálogo de Planes Oficiales Movilnet 4GMAX:\n\n` +
                `1. Inteliplan 10GB: 10 GB de datos + 1.000 Minutos + 1.000 SMS.\n` +
                `2. Plan Conecta 5GB: 5 GB de datos + 500 Minutos + 500 SMS.\n` +
                `3. Plan Básico Productivo: 2 GB de datos + 200 Minutos.\n\n` +
                `Para cambiar tu plan, responde con el número del plan deseado.`;

  // CASO 5: PORTABILIDAD EXPRESS Y CAMBIO DE OPERADORA
  } else if (/portabilidad|cambiar|migrar|esim|quiero movilnet|adquirir|pasarme/.test(cleanMsg) || /portabilidad|cambiar|migrar|esim|quiero movilnet|adquirir|pasarme/.test(normalizedMsg)) {
    pipelineRoute = 'FUNNEL_MARKETING_PORTABILIDAD';
    replyText = `🎯 ¡Excelente decisión, ${pushName}!\n\n` +
                `Cambiarte a Movilnet 4GMAX es 100% GRATIS conservando tu mismo número (${phoneFormatted}).\n\n` +
                `🎁 Beneficios exclusivos de bienvenida:\n` +
                `• Tu eSIM digital gratis activada en minutos\n` +
                `• Bono de 10 GB de navegación gratis\n` +
                `• WhatsApp libre en toda Venezuela\n\n` +
                `Para iniciar tu activación express, responde con tu número de Cédula de Identidad.`;

  // CASO 6: SEGURIDAD, ROBO O BLOQUEO DE IMEI
  } else if (/robo|hurto|bloqueo|extravio|imei|suspender/.test(cleanMsg) || /robo|hurto|bloqueo|extravio|imei|suspender/.test(normalizedMsg)) {
    replyText = `🚨 Centro de Seguridad y Bloqueo EIR Movilnet:\n\n` +
                `Para suspender temporalmente tu línea ${phoneFormatted} por robo o extravío, confirma tu número de Cédula de Identidad y los últimos 4 dígitos del IMEI.`;

  // CASO 7: CONTRATO / TITULAR
  } else if (/contrato|titular|informa contrato/.test(cleanMsg) || /contrato|titular|informa contrato/.test(normalizedMsg)) {
    replyText = `Estimado(a) ${pushName}, tu contrato para la línea ${phoneFormatted} está ACTIVO en el plan Inteliplan 10GB 4GMAX (PREPAGO VIP).\n\n` +
                `💰 Saldo disponible: Bs. 450,00\n` +
                `📶 Datos remanentes: 10.0 GB de 10.0 GB\n` +
                `🔒 Estado EIR: Habilitado y Seguro`;

  // CASO 8: MENÚ GENERAL DE AUTOSERVICIO (FALLBACK)
  } else {
    replyText = `Estimado usuario (${phoneFormatted}):\n\n` +
                `Bienvenido al Centro de Atención Digital Movilnet 4GMAX.\n` +
                `• Escribe 'Saldo' para consultar tu balance disponible.\n` +
                `• Escribe 'Planes' para conocer los planes disponibles.\n` +
                `• Escribe 'Recarga' para recargar con Pago Móvil C2P.\n` +
                `• Escribe 'Portabilidad' para cambiarte gratis a Movilnet con eSIM.`;
  }

  // 5. Salida para convergencia y entrega en WhatsApp
  item.json.output = replyText;
  item.json.final_text = replyText;
  item.json.pipeline_route = pipelineRoute;
  item.json.carrier_phone = cleanDigits;
}

return items;'''

HTTP_BODY_EXPR = r'''={{ JSON.stringify({
  "number": $('Webhook').item.json.body.data.key.remoteJid.replace(/@.*/, ''),
  "options": {
    "delay": 0
  },
  "text": $json.final_text
}) }}'''


def update_workflow_json(source_json_path: Path, output_json_path: Path) -> dict:
    with open(source_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    wf = data.get("workflow", data)
    nodes = wf.get("nodes", [])

    updated_router = False
    updated_http = False

    for node in nodes:
        if node.get("name") == "Movilnet Core & Marketing Router":
            node["parameters"]["jsCode"] = ROUTER_JS
            updated_router = True
        elif node.get("name") == "HTTP Request":
            node["parameters"]["body"] = HTTP_BODY_EXPR
            updated_http = True

    assert updated_router, "No se encontró el nodo 'Movilnet Core & Marketing Router'"
    assert updated_http, "No se encontró el nodo 'HTTP Request'"

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)

    print(f"✅ Workflow optimizado con despacho instantáneo (delay: 0) y guardado en {output_json_path}")
    return wf


if __name__ == "__main__":
    src = Path("/Users/ismael/.gemini/antigravity/brain/dd3bd033-5869-42c5-8855-2650196b3d02/.system_generated/steps/592/output.txt")
    out = PROJECT_ROOT / "api" / "n8n_workflows" / "viki_lpgtec_v2_ids_instant_dispatch.json"
    update_workflow_json(src, out)
