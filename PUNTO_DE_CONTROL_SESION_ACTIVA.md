# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** Jueves 2026-10-15 11:15 VET | **Capítulos Bitácora:** 183 al 205 (Desacoplamiento Físico Zero-Phone, Línea Central +58 424 153 3712, Supresión Tarjetas Falsas, Despliegue Render, Centro Monitoreo :8010, Blindaje Inmutable `v1.0.0-prod-sealed`, Diagnóstico Forense Evolution API, Regla General Cero Adivinación, Clasificador Saludo Puro vs Compuesto, Módulo NO_USUARIOS_MOVILNET, Releases `v1.0.1` a `v1.0.4-prod-sealed`, Firewall Booleano `IS_MOVILNET_SUBSCRIBER` 0416/0426, GPS Nativo WhatsApp, Ingesta Certificada Censo 1.017 Puntos Movilnet, Master Blueprint B2B Tripartito [Cap. 203], Diagnóstico Forense Multisesión 5 Conversaciones, Eliminación Saldos Falsos N8N, Detección Sordera Tiendas, Protocolo Recargas a Terceros, Suite Automatizada de Verificación y Plan de Acción 4 Niveles Ahorro 82% Tokens [Cap. 204], Ejecución y Certificación Militar de la Opción B, Aislamiento de Puertos, Despliegue de Interfaces Gráficas y Erradicación Total de Trazas Ficticias [Cap. 205]).
- **Entorno de Trabajo Activo:** 🏛️ Rama Git **`develop`** (Activa para nuevos desarrollos; `main` blindada con tag `v1.0.4-prod-sealed` al commit `30582a1`).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura (**495/495 pruebas automatizadas aprobadas, 0 fallos, 0 errores**: 470 tests en `tests/` + 25 en `scripts/test_*.py`).
- **Línea Oficial Única Auditada del Asistente:** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad inmutable `MOVI`).
- **Directiva Soberana Inviolable:** Segmentación perimetral estricta:
  * Si el prefijo es **0416 o 0426**: `IS_MOVILNET_SUBSCRIBER = true` -> `CORE_MOVILNET_AUTOGESTION` (Saldo real OCS/PWA, planes, C2P, reposición SIM en agencias).
  * Si el prefijo es **diferente a 0416 y 0426** (0414, 0424, 0412, etc.): `IS_MOVILNET_SUBSCRIBER = false` -> `NO_USUARIOS_MOVILNET` (Portabilidad 4GMAX, eSIM gratis, bono 10GB, recargas seguras a terceros solicitando número Movilnet).

- **Ejecución y Verificación en Caliente Opción B (Capítulo 205):**
  * **Puerto :8000 (Docker DSS GPS):** Preservado intacto y blindado según `agy-port-guardian`.
  * **Puerto :8010 (Movilnet Core & Conversatorio):** Activo en PID 12889 con salud HTTP 200 y poller n8n Cloud sincronizado.
  * **Interfaces Web Abiertas en el Navegador del Usuario:**
    1. Conversatorio: `http://localhost:8010/ui/monitor/conversatorio.html`
    2. Simulador PWA Móvil: `http://localhost:8010/ui/pwa_stitch/simulador.html`
  * **5 Casos Críticos Simulados e Inyectados en Vivo:**
    1. Francisco Landaeta (0414-2650088): Oficina Centro Plaza (0.68 ms, 0 tokens).
    2. Abonado VIP (0416-0000001): Saldo real OCS/SQLite sin saldos quemados (0.78 ms, 0 tokens).
    3. Ids (0414-2554590): `HIJA_TERCEROS_GUARD` exige 0416/0426 antes de recargar (0.11 ms, 0 tokens).
    4. Ids (0414-2554590): `OFF_TOPIC_TELCO_GUARD` corta restaurantes a telco (0.42 ms, 0 tokens).
    5. Abonado (0416-1234567): Ficha oficial de parámetros APN (0.28 ms, 0 tokens).
  * **Remoción Definitiva de Trazas Ficticias:** Purgadas cadenas `1.650,00` y `11.9 GB` en `core/conversation_trace_engine.py` y `reports/shared_live_traces.json`.

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube Blindado (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en puerto 8010, watchdog visual activo).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Instrucción para Retomar Sesión:**
  > Escribir simplemente: **"¿Recuerdas dónde quedamos?"** o **"Continuemos en rama develop"**. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
