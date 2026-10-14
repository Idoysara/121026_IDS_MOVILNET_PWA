# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 17:12 VET | **Capítulos Bitácora:** 183 al 196 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712, Supresión de Tarjetas Falsas `linkPreview`, Despliegue en Render, Centro de Monitoreo :8010, Blindaje Inmutable de Producción `v1.0.0-prod-sealed`, Diagnóstico Forense Estado 'PENDING' en Evolution API, Regla General de Cero Adivinación y Datos Faltantes, Clasificador "Saludo Puro" vs "Consulta Compuesta", Módulo Exclusivo NO_USUARIOS_MOVILNET, Erradicación Total de Secuestro Comercial Ciego, Release `v1.0.1-prod-sealed`, Blindaje Absoluto Contra Asunción de Abonado en Líneas No-Movilnet (0414/0424/0412), Promoción Oficial Release `v1.0.2-prod-sealed` e Implementación Perimetral del Firewall Booleano `IS_MOVILNET_SUBSCRIBER` 0416/0426 y Arquitectura `NO_USUARIOS_MOVILNET`).
- **Estado de Producción:** 🔒 **PROD_LOCKED_AND_SHIELDED** (Rama `main` congelada bajo tag inmutable `v1.0.2-prod-sealed`, sincronizado en GitHub, Render Cloud y n8n Cloud).
- **Entorno de Trabajo Activo:** 🛠️ Rama Git **`develop`** (Desarrollo y pruebas locales activas).
- **Versión de Producción:** `v1.0.2-carrier-enterprise` (Tag `v1.0.2-prod-sealed`, Health 200 OK en Render).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura, PWA, clasificación compuesta, firewall perimetral booleano, guardarraíles y reencuentros (0 fallos).
- **Línea Oficial Única Auditada del Asistente (El '1' en N <-> 1):** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Directiva Soberana Inviolable:** Erradicación total de números no oficiales. Segmentación absoluta:
  * Si el prefijo es **0416 o 0426**: `IS_MOVILNET_SUBSCRIBER = true` -> `CORE_MOVILNET_AUTOGESTION` (Menú de autogestión, saldo, planes, C2P).
  * Si el prefijo es **diferente a 0416 y 0426** (0414, 0424, 0412, etc.): `IS_MOVILNET_SUBSCRIBER = false` -> `NO_USUARIOS_MOVILNET` (Portabilidad 4GMAX, eSIM gratis, bono 10GB, prohibido decir 'con tu línea Movilnet' o asumir que tiene contrato).

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube Blindado (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`, Uptime >1200s, desplegado sobre producción).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`, `Edge Carrier Firewall` perimetral booleano, `AI Agent` con prompt dinámico y regla de no-asunción, Router con soporte de reencuentros).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en `develop` con demonio HTTP en puerto 8010, verificado 100% saludable).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Avances Fundamentales Capítulo 196 (Firewall Perimetral Booleano 0416/0426 & Ecosistema NO_USUARIOS_MOVILNET):**
  * **Nodo 'Edge Carrier Firewall (0416/0426)' en n8n:**
    - Insertado entre `Edit Fields` y `Switch`, centralizando en una Fuente Única de Verdad (SSOT) la normalización defensiva (LID, E.164, internacionales) y el estampado de invariantes inmutables:
      `IS_MOVILNET_SUBSCRIBER = Boolean(isMovilnet)`, `authorized_pipeline` (`CORE_MOVILNET_AUTOGESTION` vs `NO_USUARIOS_MOVILNET`), `detected_carrier` y `carrier_label`.
  * **Blindaje en Capa Python Core:**
    - `PhoneDescriptor.is_movilnet_subscriber`: Property tipada booleana (`prefix in ("0416", "0426")`).
    - `CarrierClassificationResult.is_movilnet_subscriber`: Exposición tipada de la compuerta.
    - `NormalizedInboundMessage`: Incorporación de `is_movilnet_subscriber`, `authorized_pipeline`, `detected_carrier`.
    - `FastPathIntentInterceptor`: `FastPathResolution` estampando formalmente `is_movilnet_subscriber` y `authorized_pipeline`.
  * **Certificación Militar:**
    - Suite de pruebas `scripts/test_edge_carrier_firewall.py` con 100% PASS (6/6 pruebas).
    - Suite de regresión `scripts/test_pure_greeting_vs_compound_query.py` con 100% PASS (7/7 pruebas). Total: 13/13 pruebas exitosas (0 fallos).

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
