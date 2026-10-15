# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** Jueves 2026-10-15 08:00 VET | **Capítulos Bitácora:** 183 al 203 (Desacoplamiento Físico Zero-Phone, Línea Central +58 424 153 3712, Supresión Tarjetas Falsas, Despliegue Render, Centro Monitoreo :8010, Blindaje Inmutable `v1.0.0-prod-sealed`, Diagnóstico Forense Evolution API, Regla General Cero Adivinación, Clasificador Saludo Puro vs Compuesto, Módulo NO_USUARIOS_MOVILNET, Releases `v1.0.1` a `v1.0.4-prod-sealed`, Firewall Booleano `IS_MOVILNET_SUBSCRIBER` 0416/0426, GPS Nativo WhatsApp, Ingesta Certificada Censo 1.017 Puntos Movilnet, Resolución Error GPS Router n8n [Cap. 201], Blindaje Telemetría Conversatorio y Watchdog [Cap. 202], y Convergencia Estratégica Master Blueprint B2B Tripartito, DOFA, Factibilidad Integral, Dossier de Inversión $58k CAPEX y Posicionamiento en Rama `develop` [Cap. 203]).
- **Entorno de Trabajo Activo:** 🏛️ Rama Git **`develop`** (Activa para nuevos desarrollos; `main` blindada con tag `v1.0.4-prod-sealed` al commit `30582a1`).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura (331/331 pruebas automatizadas aprobadas, 0 fallos, 0 errores).
- **Línea Oficial Única Auditada del Asistente:** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Directiva Soberana Inviolable:** Segmentación perimetral estricta:
  * Si el prefijo es **0416 o 0426**: `IS_MOVILNET_SUBSCRIBER = true` -> `CORE_MOVILNET_AUTOGESTION` (Saldo, planes, C2P, reposición SIM en agencias).
  * Si el prefijo es **diferente a 0416 y 0426** (0414, 0424, 0412, etc.): `IS_MOVILNET_SUBSCRIBER = false` -> `NO_USUARIOS_MOVILNET` (Portabilidad 4GMAX, eSIM gratis, bono 10GB).

- **Dossier de Inversión y Alianza B2B (Capítulo 203):**
  * **Documento para Inversionistas:** `IDS_DOC/DOSSIER_EJECUTIVO_INVERSIONISTA_MOVILNET_B2B.md` (CAPEX $58,000 USD en activos tangibles GPU/servidores, Break-Even Mes 5-6, ROI 141.2% semestral, +$81,900 USD de ganancia neta y +$46,800 USD/mes de flujo neto recurrente a M6).
  * **Comisión Telco:** 20% bruto liquidado trimestralmente ($40,000 USD en semestre 1, $116,200 USD Año 1, $152,400 USD/año régimen estable con $0 CAPEX).
  * **Censo Nacional Oficial Movilnet:** 1.017 Puntos Físicos Georreferenciados en `data/censo_oficial_movilnet_puntos_atencion.json` (SHA-256 `a9d3578b5dbfa52b16f5692dfdbe4f713d0f7829ea97d2fec749220eea4eb492`).

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube Blindado (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en puerto 8010, watchdog visual activo).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Instrucción para Nueva Conversación (`+`) Fecha Jueves 151026:**
  > Al abrir la nueva sesión, escribir simplemente: **"¿Recuerdas dónde quedamos?"** o **"Continuemos en rama develop"**. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
