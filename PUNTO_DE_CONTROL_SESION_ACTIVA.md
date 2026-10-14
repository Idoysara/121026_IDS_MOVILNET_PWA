# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 13:42 VET | **Capítulos Bitácora:** 183 al 189 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712 y Erradicación Total de Números Ajenos, Auditoría de Caracteres WhatsApp y Supresión de Tarjetas Falsas `linkPreview`, Reset de Límites Freemium, Despliegue en Render `dep-db7qb57avr4c7396gv9g` en Commit `c74f5c0`, Verificación del Centro de Monitoreo :8010, Restauración de Visualización Omnicanal N <--> 1 en Conversatorio Web e Integración Omnicanal PWA Móvil/Web con Aislamiento Soberano de Datos).
- **Entorno de Trabajo Activo:** Ramas Git **`main`** y **`develop`** (Sincronizadas y desplegadas en GitHub y Render).
- **Versión de Producción:** `v1.0.0-carrier-enterprise` (Commit `4ff0b10`, Render Deploy `dep-db7qb57avr4c7396gv9g`).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura, PWA y guardarraíles (0 fallos).
- **Línea Oficial Única Auditada del Asistente (El '1' en N <-> 1):** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Directiva Soberana Inviolable:** Erradicación total de números no oficiales (`0414-2650088`, `0414-2554590`, `0416-6251587`). Extracción de abonados 100% dinámica en n8n y en el núcleo.

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo y desconfinado de sandbox con demonio poller n8n cada 2.5s, 10 abonados reales indexados, 249 trazas en vivo).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Resolución Forense Omnicanal (Capítulos 188 y 189 - Visualización N <--> 1 y PWA):**
  * **Ingesta PWA Confirmada:** Toda interacción PWA (`/pwa`, `/ui/pwa_stitch/index.html`) ingresa a `conversation_trace_engine` y `webhook_feed_manager` clasificada como `PWA Móvil (Data 4GMAX)`.
  * **Aislamiento Soberano PWA:** Las interacciones PWA responden directamente por retorno HTTP (<15ms FastPath / <800ms IA) y NUNCA se despachan a WhatsApp ni a n8n, evitando costos SMS o mensajes duplicados.
  * **Unificación de Hilo de Abonado:** Si el usuario chatea por WhatsApp y luego por PWA con el mismo número, el historial se consolida en el mismo hilo de abonado. La línea demo `0416-0000001` se visualiza como "Abonado PWA (Movilnet)".
  * **Poller Demonio Asíncrono:** Añadido `_background_n8n_poller` dentro de `api/service.py` que consulta n8n Cloud cada 2.5s y actualiza RAM y `shared_live_traces.json`.
  * **Auto-Selección Reactiva:** `conversatorio.html` selecciona automáticamente el abonado con actividad más reciente (`groupedThreads[0]`) y aborta peticiones remotas lentas a Render con timeout de 2s.

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
