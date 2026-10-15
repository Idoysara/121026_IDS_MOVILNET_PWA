# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-15 00:25 VET | **Capítulos Bitácora:** 183 al 202 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712, Supresión de Tarjetas Falsas `linkPreview`, Despliegue en Render, Centro de Monitoreo :8010, Blindaje Inmutable de Producción `v1.0.0-prod-sealed`, Diagnóstico Forense Estado 'PENDING' en Evolution API, Regla General de Cero Adivinación y Datos Faltantes, Clasificador "Saludo Puro" vs "Consulta Compuesta", Módulo Exclusivo NO_USUARIOS_MOVILNET, Erradicación Total de Secuestro Comercial Ciego, Releases `v1.0.1-prod-sealed`, `v1.0.2-prod-sealed`, `v1.0.3-prod-sealed`, `v1.0.4-prod-sealed`, Firewall Booleano `IS_MOVILNET_SUBSCRIBER` 0416/0426, Hardware GPS WhatsApp Nativo, Ingesta Certificada del Censo Nacional de 1.017 Puntos Físicos Movilnet, Resolución de Error GPS en Router n8n [Cap. 201], y Blindaje Soberano de Telemetría Conversatorio y Watchdog Activo [Cap. 202]).
- **Estado de Producción:** 🔒 **PROD_LOCKED_AND_SHIELDED** (Rama `main` sincronizada con `develop` al commit `30582a1`, sincronizado en GitHub `Idoysara/121026_IDS_MOVILNET_PWA`, Render Cloud y n8n Cloud).
- **Entorno de Trabajo Activo:** 🏛️ Ramas Git **`main`** y **`develop`** (100% sincronizadas y al día).
- **Versión de Producción:** `v1.0.4-carrier-enterprise` (Tag `v1.0.4-prod-sealed` + Commit `30582a1`).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura (331/331 pruebas automatizadas aprobadas en 9.64s, 0 fallos, 0 errores).
- **Línea Oficial Única Auditada del Asistente (El '1' en N <-> 1):** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Directiva Soberana Inviolable:** Erradicación total de números no oficiales. Segmentación perimetral:
  * Si el prefijo es **0416 o 0426**: `IS_MOVILNET_SUBSCRIBER = true` -> `CORE_MOVILNET_AUTOGESTION` (Menú de autogestión, saldo, planes, C2P, reposición SIM en agencias).
  * Si el prefijo es **diferente a 0416 y 0426** (0414, 0424, 0412, etc.): `IS_MOVILNET_SUBSCRIBER = false` -> `NO_USUARIOS_MOVILNET` (Portabilidad 4GMAX, eSIM gratis, bono 10GB, entrega física de chip en agencias).

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube Blindado (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`, Uptime >1500s).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`, `Edge Carrier Firewall` perimetral booleano, soporte geoespacial para `locationMessage`, enrutamiento determinista blindado contra Task Broker Disconnect).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en puerto 8010, sincronizador poller n8n conectado en tiempo real con 297 líneas indexadas, watchdog visual activo).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Blindaje de Telemetría Conversatorio (:8010) — Reglas Maestras (Capítulo 202):**
  * Documento normativo: `docs/REGLAS_BLINDAJE_TELEMETRIA_CONVERSATORIO.md`.
  * Pre-Flight Check en `api/service.py` al arrancar.
  * Telemetría de poller en `/health` y `/api/v1/monitor/conversations`.
  * 100% Soberanía local en `conversatorio.html`: cero peticiones a Render al estar en localhost.
  * Watchdog visual en cabecera: advertencia roja automática si el poller pierde red.
  * Lanzador oficial certificado: `scripts/reiniciar_todo_limpio.command`.

- **Censo Nacional Oficial Movilnet (Capítulo 199):**
  * **1.017 Puntos Físicos Georreferenciados:** 1 Sede Corporativa (Torre El Recreo), 31 Oficinas de Atención al Cliente (OSAC), 500 Agentes Autorizados (AA), 485 Agentes Comerciales Integrales (ACI).
  * Sello Criptográfico Inmutable SHA-256: `a9d3578b5dbfa52b16f5692dfdbe4f713d0f7829ea97d2fec749220eea4eb492`.
  * Archivo estructurado: `data/censo_oficial_movilnet_puntos_atencion.json`.

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
