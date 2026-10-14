# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 12:20 VET | **Capítulos Bitácora:** 183 al 187 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712 y Erradicación Total de Números Ajenos, Auditoría de Caracteres WhatsApp y Supresión de Tarjetas Falsas `linkPreview`, Reset de Límites Freemium, Despliegue en Render `dep-db7qb57avr4c7396gv9g` en Commit `c74f5c0`, y Verificación del Centro de Monitoreo Conversacional :8010 Activo para Pruebas Reales).
- **Entorno de Trabajo Activo:** Ramas Git **`main`** y **`develop`** (Sincronizadas y desplegadas en GitHub y Render).
- **Versión de Producción:** `v1.0.0-carrier-enterprise` (Commit `c74f5c0`, Render Deploy `dep-db7qb57avr4c7396gv9g`).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura, PWA y guardarraíles (0 fallos).
- **Línea Oficial Única Auditada del Asistente (El '1' en N <-> 1):** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Directiva Soberana Inviolable:** Erradicación total de números no oficiales (`0414-2650088`, `0414-2554590`, `0416-6251587`). Extracción de abonados 100% dinámica en n8n y en el núcleo.

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en PID 24531, 481 trazas en vivo).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Correcciones Quirúrgicas Aplicadas en n8n:**
  * **Codificación de URL:** Inyección de `encodeURIComponent()` en el nodo `HTTP Request` para evitar el error `400 Bad Request` ante nombres de instancia con espacios (`Viki LPGTEC`).
  * **Sanitización de Caracteres Egress:** Conversión automática de `\n` literales a saltos de línea físicos y de viñetas `•` al guion estándar `- `.
  * **Supresión de Tarjetas Falsas:** Forzado de `"linkPreview": false` a nivel raíz y en opciones, erradicando el cuadro negro con botón Play (`▶`) que aplastaba el texto en WhatsApp.

- **Estado de Bases de Datos y Reset Freemium:**
  * Tabla `prospect_trial_limits` en SQLite WAL (`db/local_movilnet.db`) reseteada a 0 registros.
  * Aislamiento de sesiones en `Postgres Chat Memory` bajo el esquema `SESSION:E164:<numero_abonado>`.

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
