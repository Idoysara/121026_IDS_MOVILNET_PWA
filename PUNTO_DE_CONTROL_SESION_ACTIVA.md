# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 16:05 VET | **Capítulos Bitácora:** 183 al 195 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712, Supresión de Tarjetas Falsas `linkPreview`, Despliegue en Render, Centro de Monitoreo :8010, Blindaje Inmutable de Producción `v1.0.0-prod-sealed`, Diagnóstico Forense Estado 'PENDING' en Evolution API, Regla General de Cero Adivinación y Datos Faltantes, Clasificador "Saludo Puro" vs "Consulta Compuesta", Módulo Exclusivo NO_USUARIOS_MOVILNET, Erradicación Total de Secuestro Comercial Ciego, Release `v1.0.1-prod-sealed`, Blindaje Absoluto Contra Asunción de Abonado en Líneas No-Movilnet (0414/0424/0412) y Promoción Oficial Release `v1.0.2-prod-sealed`).
- **Estado de Producción:** 🔒 **PROD_LOCKED_AND_SHIELDED** (Rama `main` congelada bajo tag inmutable `v1.0.2-prod-sealed`, sincronizado en GitHub, Render Cloud y n8n Cloud).
- **Entorno de Trabajo Activo:** 🛠️ Rama Git **`develop`** (Desarrollo y pruebas locales activas).
- **Versión de Producción:** `v1.0.2-carrier-enterprise` (Tag `v1.0.2-prod-sealed`, Health 200 OK en Render).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura, PWA, clasificación compuesta, guardarraíles y reencuentros (0 fallos).
- **Línea Oficial Única Auditada del Asistente (El '1' en N <-> 1):** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Directiva Soberana Inviolable:** Erradicación total de números no oficiales. Segmentación absoluta:
  * Si el prefijo es **0416 o 0426**: `ABONADO_MOVILNET_ACTIVO` (Menú de autogestión, saldo, planes, C2P).
  * Si el prefijo es **diferente a 0416 y 0426** (0414, 0424, 0412, etc.): `MODO_CAPTACION_FUNNEL_MARKETING_NO_MOVILNET` (Portabilidad 4GMAX, eSIM gratis, bono 10GB, prohibido decir 'con tu línea Movilnet' o asumir que tiene contrato).

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube Blindado (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`, Uptime >1200s, desplegado sobre producción).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`, `AI Agent` con prompt dinámico de modo operativo y regla de no-asunción, Router con soporte de reencuentros).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en `develop` con demonio HTTP en puerto 8010, verificado 100% saludable).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Avances Fundamentales Capítulo 195 (Blindaje No-Movilnet & Reencuentros):**
  * **Solución al Caso Real Ids (0414-2554590 - "Nuevamente soy yo"):**
    - Identificada causa raíz: el clasificador no reconocía fórmulas de reencuentro coloquial y el nodo `AI Agent` no recibía la operadora ni el modo del usuario, alucinando que tenía una línea Movilnet.
  * **Doble Guardia Inviolable:**
    - **Guardia A (Router Determinista):** Reconoce expresiones de reencuentro (`"Nuevamente soy yo"`, `"Soy yo de nuevo"`, `"Volví"`) y enruta líneas 0414/0424/0412 al módulo `FUNNEL_MARKETING_NO_USUARIOS_MOVILNET` con bienvenida cordial reconociendo su operadora y ofreciendo Portabilidad 4GMAX.
    - **Guardia B (AI Agent en n8n Cloud y Python):** `parameters.text` inyecta dinámicamente `MODO OPERATIVO: MODO_CAPTACION_FUNNEL_MARKETING_NO_MOVILNET` para todo número no-0416/0426. `systemMessage` prohíbe terminantemente decir *"con tu línea Movilnet"* y obliga a operar en modo captación y portabilidad.
  * **Sincronización en Caliente de n8n Cloud:** Desplegado con éxito en el workflow canónico `sNMbtiEiTkuQ9OCY`.
  * **Certificación Militar:** Suite de pruebas `scripts/test_pure_greeting_vs_compound_query.py` con 100% PASS (7/7 pruebas, incluyendo aserciones negativas contra `"tu línea Movilnet"` para el caso `0414-2554590`).

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
