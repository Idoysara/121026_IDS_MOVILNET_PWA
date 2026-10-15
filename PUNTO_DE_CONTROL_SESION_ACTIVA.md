# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** Jueves 2026-10-15 10:40 VET | **Capítulos Bitácora:** 183 al 204 (Desacoplamiento Físico Zero-Phone, Línea Central +58 424 153 3712, Supresión Tarjetas Falsas, Despliegue Render, Centro Monitoreo :8010, Blindaje Inmutable `v1.0.0-prod-sealed`, Diagnóstico Forense Evolution API, Regla General Cero Adivinación, Clasificador Saludo Puro vs Compuesto, Módulo NO_USUARIOS_MOVILNET, Releases `v1.0.1` a `v1.0.4-prod-sealed`, Firewall Booleano `IS_MOVILNET_SUBSCRIBER` 0416/0426, GPS Nativo WhatsApp, Ingesta Certificada Censo 1.017 Puntos Movilnet, Master Blueprint B2B Tripartito [Cap. 203], Diagnóstico Forense Multisesión 5 Conversaciones, Eliminación Saldos Falsos N8N, Detección Sordera Tiendas, Protocolo Recargas a Terceros, Suite Automatizada de Verificación y Plan de Acción 4 Niveles Ahorro 82% Tokens [Cap. 204]).
- **Entorno de Trabajo Activo:** 🏛️ Rama Git **`develop`** (Activa para nuevos desarrollos; `main` blindada con tag `v1.0.4-prod-sealed` al commit `30582a1`).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura (**489/489 pruebas automatizadas aprobadas, 0 fallos, 0 errores**: 464 tests en `tests/` + 25 en `scripts/test_*.py`).
- **Línea Oficial Única Auditada del Asistente:** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad inmutable `MOVI`).
- **Directiva Soberana Inviolable:** Segmentación perimetral estricta:
  * Si el prefijo es **0416 o 0426**: `IS_MOVILNET_SUBSCRIBER = true` -> `CORE_MOVILNET_AUTOGESTION` (Saldo real OCS/PWA, planes, C2P, reposición SIM en agencias).
  * Si el prefijo es **diferente a 0416 y 0426** (0414, 0424, 0412, etc.): `IS_MOVILNET_SUBSCRIBER = false` -> `NO_USUARIOS_MOVILNET` (Portabilidad 4GMAX, eSIM gratis, bono 10GB, recargas seguras a terceros solicitando número Movilnet).

- **Plan de Acción Maestro de Ahorro de Tokens y Reglas Construidas (Capítulo 204):**
  * **Documento Técnico:** `docs/PLAN_DE_ACCION_OPTIMIZACION_REGLAS_COMUNICACION_Y_AHORRO_TOKENS.md` (Ahorro del 82% de tokens, arquitectura limpia en 4 niveles, matriz de prioridades P0, P1, P2).
  * **Algoritmos y Módulos Construidos y Verificados:**
    1. `core/fastpath_intent_interceptor.py`: Mapeo de hitos caraqueños, ficha APN oficial (`PARAMETROS_APN`), guardarraíl telco (`OFF_TOPIC_TELCO_GUARD`), memoria de sesión GPS (TTL 30 min) y compuerta C2P a terceros (`HIJA_TERCEROS_GUARD`).
    2. `scripts/update_n8n_instant_dispatch.py`: Sincronización canónica y purgado de saldos quemados en `root.nodes` y `activeVersion.nodes`.
    3. `api/n8n_workflows/viki_lpgtec_v2_ids_instant_dispatch.json`: Workflow N8N purgado (0 saldos quemados, 0 números C2P inconsistentes).
    4. `tests/test_action_plan_rules_204.py`: Suite de 7 pruebas unitarias formales con 100% PASS.
  * **Causa Raíz Erradicada:** Saldos quemados en JS de N8N (`Bs. 1.650`, `11.9 GB de 5 GB`), omisión de regex de tiendas y número C2P erróneo en `ConsultarSaldo` y `PagoC2P`.
  * **Dossier de Inversión B2B:** `IDS_DOC/DOSSIER_EJECUTIVO_INVERSIONISTA_MOVILNET_B2B.md` (CAPEX $58,000 USD, ROI 141.2% semestral, +$46,800 USD/mes flujo neto recurrente).

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube Blindado (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en puerto 8010, watchdog visual activo).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Instrucción para Retomar Sesión:**
  > Escribir simplemente: **"¿Recuerdas dónde quedamos?"** o **"Continuemos en rama develop"**. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
