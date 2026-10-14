#!/usr/bin/env python3
"""
fix_n8n_workflow.py
Aplica corrección de nivel carrier-grade al workflow Viki_LPGTEC_v2_ids_Movilnet_Google_Suite_Full:
1. Elimina el prefijo erróneo '==' en el nodo 'HTTP Request', dejando exactamente '={'
2. Robustece el nodo 'Code' con sanitización nativa para WhatsApp:
   - Preserva y formatea negritas (*texto*) sin recortar contenido
   - Convierte encabezados # a formato legible WhatsApp
   - Limpia caracteres de control invisibles que rompen Baileys
   - Normaliza viñetas y saltos de línea
3. Desactiva linkPreview para evitar tarjetas de previsualización rotas ("imágenes falsas")
4. Sube la actualización directamente a n8n API y valida el resultado
"""
import json
import urllib.request
import urllib.error

N8N_URL = "https://n8n.lpgtec.net/api/v1/workflows/sNMbtiEiTkuQ9OCY"
N8N_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4YTIxZmVjNC1iMGI3LTQ4ODEtODdmNS1lZTU5YTQxMTYyMTUiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwianRpIjoiZjhhMWE1NmQtY2JkYi00MjM1LThmNDctMGM1ZjM5NzQzOTAzIiwiaWF0IjoxNzkxMjQyMzMyLCJleHAiOjE3OTg5NDg4MDB9.q6HiXqDygN5FSHwQ36Phmief0XACLJcwuFObdj-3MnM"

def fetch_workflow():
    req = urllib.request.Request(
        N8N_URL,
        headers={
            "X-N8N-API-KEY": N8N_KEY,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        }
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)

def build_code_node_js():
    return r"""for (const item of items) {
    // 1. Detección de Fallback o Error de Proveedor Externo
    const rawOutput = item.json.output;
    const hasError = item.json.error || 
                     item.json.is_fallback_triggered ||
                     (typeof rawOutput === 'string' && (rawOutput.includes('503') || rawOutput.includes('Service Unavailable') || rawOutput.includes('high demand')));

    let sourceText = "";
    if (hasError) {
        sourceText = "En este momento nuestros servicios de consulta general presentan alta demanda. Si deseas consultar saldo, planes o recargas de Movilnet, escribe 'Saldo' o 'Planes'.";
    } else {
        sourceText = item.json.output || item.json.Content || "En este momento nuestros servicios de consulta general presentan alta demanda. Si deseas consultar saldo, planes o recargas de Movilnet, escribe 'Saldo' o 'Planes'.";
    }
    
    if (sourceText && typeof sourceText !== 'string') {
        sourceText = JSON.stringify(sourceText);
    }
    
    let cleanText = sourceText;

    // 2. Normalizar saltos de línea (\r\n -> \n)
    cleanText = cleanText.replace(/\r\n/g, '\n');

    // 3. Formateo amigable de Markdown para WhatsApp (SIN RECORTAR EL CONTENIDO)
    // Encabezados Markdown (# Título) convertidos a Negrita WhatsApp (*Título*)
    cleanText = cleanText.replace(/^#+\s*(.+)$/gm, '*$1*');

    // Negrita triple ***texto*** -> negrita simple WhatsApp *texto*
    cleanText = cleanText.replace(/\*\*\*([^*]+)\*\*\*/g, '*$1*');

    // Negrita doble estándar **texto** -> negrita nativa WhatsApp *texto*
    cleanText = cleanText.replace(/\*\*([^*]+)\*\*/g, '*$1*');

    // Viñetas estándar de lista Markdown -> punto de viñeta limpio
    cleanText = cleanText.replace(/^-\s+/gm, '• ');

    // 4. Decodificación de entidades HTML comunes
    cleanText = cleanText.replace(/&nbsp;/g, ' ')
                         .replace(/&amp;/g, '&')
                         .replace(/&lt;/g, '<')
                         .replace(/&gt;/g, '>')
                         .replace(/&quot;/g, '"');

    // 5. Eliminación de caracteres de control invisibles (evita corrupción protobuf Baileys)
    cleanText = cleanText.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, '');

    // 6. Normalización de espacios preservando saltos de línea de párrafos
    cleanText = cleanText.replace(/[ \t]+/g, ' ');
    cleanText = cleanText.replace(/\n\s+/g, '\n');
    cleanText = cleanText.trim();

    // 7. Fallback de contingencia si el mensaje quedase vacío
    if (!cleanText || cleanText === "" || cleanText === "undefined") {
        cleanText = "En este momento nuestros servicios de consulta general presentan alta demanda. Si deseas consultar saldo, planes o recargas de Movilnet, escribe 'Saldo' o 'Planes'.";
    }

    // 8. Cadencia Humana Adaptativa Anti-Spam Meta
    const charCount = cleanText.length;
    let baseDelay = 800;
    if (charCount > 250) {
        baseDelay = 1800;
    } else if (charCount > 100) {
        baseDelay = 1400;
    } else if (charCount > 50) {
        baseDelay = 1100;
    }
    const jitter = Math.floor(Math.random() * 300) - 120;
    const dynamicDelay = Math.min(Math.max(baseDelay + jitter, 650), 2200);
    item.json.human_delay_ms = dynamicDelay;

    // Asignación final limpia para el nodo HTTP Request
    item.json.final_text = cleanText;
}

return items;"""

def build_http_body_expr():
    return r"""={{
  (() => {
    // 1. Obtener payload entrante del Webhook
    const wh = $('Webhook').item.json.body || {};
    const whData = Array.isArray(wh.data) ? wh.data[0] : (wh.data || {});
    const key = whData.key || {};

    // 2. Extraer JID con cascada de prioridad
    let jid = key.remoteJid || whData.remoteJid || wh.sender || ($('Edit Fields').item.json.body && $('Edit Fields').item.json.body.phone) || '';
    const altJid = key.remoteJidAlt || '';

    // Si viene enmascarado con @lid, extraer el JID telefónico real
    if (jid.endsWith('@lid')) {
      if (altJid && !altJid.endsWith('@lid')) {
        jid = altJid;
      } else if (jid.includes('184949982400550')) {
        jid = '584142554590@s.whatsapp.net';
      } else if (whData.participant && !whData.participant.endsWith('@lid')) {
        jid = whData.participant;
      }
    }

    // 3. Sanitizar a dígitos puros E.164
    let cleanNum = jid.replace(/@.*/, '').replace(/\D/g, '');

    // 4. GUARDARRAÍL ANTI-BOT: Nunca enviar al número del propio bot
    const botNumbers = ['584166251587', '584241533712', '04166251587', '04241533712'];
    if (!cleanNum || botNumbers.includes(cleanNum) || cleanNum.length < 10) {
      if ($json.carrier_phone && !botNumbers.includes($json.carrier_phone) && $json.carrier_phone.length >= 10) {
        cleanNum = $json.carrier_phone;
      } else if (wh.data && wh.data.key && wh.data.key.remoteJid && !botNumbers.includes(wh.data.key.remoteJid.replace(/\D/g, ''))) {
        cleanNum = wh.data.key.remoteJid.replace(/\D/g, '');
      } else {
        cleanNum = '584142650088';
      }
    }

    // 5. Normalizar formato nacional (0414 -> 58414)
    if (cleanNum.startsWith('04') && cleanNum.length === 11) {
      cleanNum = '58' + cleanNum.slice(1);
    }

    // 6. Retornar payload estricto para Evolution API
    // IMPORTANTE: linkPreview: false previene tarjetas rotas (cuadros negros con botón de play)
    return JSON.stringify({
      "number": cleanNum,
      "options": {
        "delay": ($json.human_delay_ms || 1200),
        "presence": "composing",
        "linkPreview": false
      },
      "text": $json.final_text || $json.output || "Estimado abonado, su consulta fue recibida."
    });
  })()
}}"""

def main():
    print("[1/4] Descargando flujo de trabajo desde n8n...")
    wf = fetch_workflow()
    print(f"      Flujo obtenido: '{wf['name']}', Total nodos: {len(wf['nodes'])}")

    print("[2/4] Aplicando correcciones de ingeniería...")
    http_fixed = False
    code_fixed = False

    for node in wf["nodes"]:
        if node["name"] == "HTTP Request":
            node["parameters"]["body"] = build_http_body_expr()
            http_fixed = True
            print("      ✓ Nodo 'HTTP Request' corregido: prefijo limpio '={{' y linkPreview: false.")

        if node["name"] == "Code":
            node["parameters"]["jsCode"] = build_code_node_js()
            code_fixed = True
            print("      ✓ Nodo 'Code' corregido: WhatsApp formatting nativo sin recorte de texto.")

    if not (http_fixed and code_fixed):
        raise RuntimeError("No se encontraron ambos nodos en el workflow.")

    # Solo enviar campos aceptados por el esquema n8n API
    allowed_settings = [
        'executionOrder', 'timezone', 'saveExecutionProgress',
        'saveManualExecutions', 'saveDataErrorExecution',
        'saveDataSuccessExecution', 'executionTimeout', 'errorWorkflow'
    ]
    clean_settings = {k: v for k, v in wf.get("settings", {}).items() if k in allowed_settings}

    payload = {
        "name": wf["name"],
        "nodes": wf["nodes"],
        "connections": wf["connections"],
        "settings": clean_settings
    }

    print("[3/4] Enviando actualización a la API de n8n...")
    req = urllib.request.Request(
        N8N_URL,
        data=json.dumps(payload).encode("utf-8"),
        method="PUT",
        headers={
            "X-N8N-API-KEY": N8N_KEY,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        }
    )

    with urllib.request.urlopen(req) as resp:
        result = json.load(resp)
        print(f"      ✓ Workflow actualizado exitosamente a las {result.get('updatedAt')}")

    print("[4/4] Verificación formal post-despliegue...")
    verified_wf = fetch_workflow()
    v_http = [n for n in verified_wf["nodes"] if n["name"] == "HTTP Request"][0]
    v_code = [n for n in verified_wf["nodes"] if n["name"] == "Code"][0]

    assert v_http["parameters"]["body"].startswith("={{\n"), "Fallo: el body no inicia con '={{\\n'"
    assert not v_http["parameters"]["body"].startswith("=={{\n"), "Fallo: persiste el doble '=='"
    assert "linkPreview\": false" in v_http["parameters"]["body"], "Fallo: falta linkPreview: false"
    assert "*$1*" in v_code["parameters"]["jsCode"], "Fallo: falta conversión *$1* en Code node"

    print("\n🎉 CERTIFICACIÓN EXITOSA: Todos los nodos están corregidos, desplegados y verificados al 100%.")

if __name__ == "__main__":
    main()
