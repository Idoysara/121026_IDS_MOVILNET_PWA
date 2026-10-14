# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 15:46 VET | **Capítulos Bitácora:** 183 al 194 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712, Supresión de Tarjetas Falsas `linkPreview`, Despliegue en Render, Centro de Monitoreo :8010, Blindaje Inmutable de Producción `v1.0.0-prod-sealed`, Diagnóstico Forense Estado 'PENDING' en Evolution API, Regla General de Cero Adivinación y Datos Faltantes, Clasificador "Saludo Puro" vs "Consulta Compuesta", Módulo Exclusivo NO_USUARIOS_MOVILNET, Erradicación Total de Secuestro Comercial Ciego y Promoción Oficial a Producción Release `v1.0.1-prod-sealed`).
- **Estado de Producción:** 🔒 **PROD_LOCKED_AND_SHIELDED** (Rama `main` congelada bajo tag inmutable `v1.0.1-prod-sealed`, Commit `23ed7c9`, sincronizado en GitHub y Render Cloud).
- **Entorno de Trabajo Activo:** 🛠️ Rama Git **`develop`** (Desarrollo y pruebas locales activas).
- **Versión de Producción:** `v1.0.1-carrier-enterprise` (Tag `v1.0.1-prod-sealed`, Commit `23ed7c9`, Health 200 OK en Render).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura, PWA, clasificación compuesta y guardarraíles (0 fallos).
- **Línea Oficial Única Auditada del Asistente (El '1' en N <-> 1):** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Directiva Soberana Inviolable:** Erradicación total de números no oficiales (`0414-2650088`, `0414-2554590`, `0416-6251587`). Extracción de abonados 100% dinámica en n8n y en el núcleo.

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube Blindado (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`, Uptime >830s, desplegado sobre tag `v1.0.1-prod-sealed`).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en `develop` con demonio poller n8n desconfinado cada 2.5s, 11 abonados indexados, 264 trazas en vivo).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Avances Fundamentales Capítulo 193 y 194 (Clasificador de Saludos & Promoción a Producción):**
  * **Clasificador `GreetingCompoundClassifier`:** Analiza la carga semántica residual tras suprimir saludos y cortesías. Si contiene preguntas, verbos (`quiero`, `comprar`, `recomiendas`) o sustantivos (`laptop`, `precio`, `farmacia`), se cataloga como `COMPOUND_QUERY` y jamás como saludo puro.
  * **Aislamiento Estricto de Menús por Operadora:**
    - **Abonados ÚNICOS Movilnet (0416/0426):** Reciben el Menú Oficial de Autogestión (Saldo, Planes, Recarga C2P, Contrato) con link a la PWA de autogestión.
    - **NO Usuarios Movilnet (0414/0424/0412/otros):** Derivados obligatoriamente al módulo `NO_USUARIOS_MOVILNET` (Funnel Marketing Portabilidad 4GMAX, eSIM digital gratis, 10 GB de bienvenida, 60% ahorro en renta, sin opciones de saldo interno).
  * **Cero Secuestro Comercial Ciego:** Toda consulta abierta de cualquier usuario (sea Movistar, Digitel o Movilnet) viaja directamente al motor de Inteligencia Artificial (`AI Agent` - Gemini 2.5 Flash), erradicando respuestas sordas.
  * **Sincronización en Caliente de n8n Cloud:** Desplegada la nueva condición en el nodo `Router - Consultas determinísticas` (`telco_movilnet_fastpath`) y el enrutador en `Movilnet Core & Marketing Router`.
  * **Promoción Oficial a Producción:** `develop` fusionado en `main`, tag inmutable `v1.0.1-prod-sealed` emitido y pusheado a GitHub y Render Cloud.
  * **Certificación Militar:** Suite de pruebas `test_pure_greeting_vs_compound_query.py` con 100% PASS (6/6 suites, 35 aserciones sin fallos).

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
