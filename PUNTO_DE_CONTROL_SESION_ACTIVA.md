# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 18:05 VET | **Capítulos Bitácora:** 183 al 198 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712, Supresión de Tarjetas Falsas `linkPreview`, Despliegue en Render, Centro de Monitoreo :8010, Blindaje Inmutable de Producción `v1.0.0-prod-sealed`, Diagnóstico Forense Estado 'PENDING' en Evolution API, Regla General de Cero Adivinación y Datos Faltantes, Clasificador "Saludo Puro" vs "Consulta Compuesta", Módulo Exclusivo NO_USUARIOS_MOVILNET, Erradicación Total de Secuestro Comercial Ciego, Releases `v1.0.1-prod-sealed`, `v1.0.2-prod-sealed`, `v1.0.3-prod-sealed`, Firewall Booleano `IS_MOVILNET_SUBSCRIBER` 0416/0426, e Implementación Integral Vía 1: Extracción Física de Hardware GPS Nativo de WhatsApp WGS84 para Localizador de Oficinas Movilnet 4GMAX).
- **Estado de Producción:** 🔒 **PROD_LOCKED_AND_SHIELDED** (Rama `main` congelada bajo tag inmutable `v1.0.3-prod-sealed`, sincronizado en GitHub `Idoysara/121026_IDS_MOVILNET_PWA`, Render Cloud y n8n Cloud).
- **Entorno de Trabajo Activo:** 🛠️ Rama Git **`develop`** (Desarrollo y pruebas locales activas).
- **Versión de Producción:** `v1.0.3-carrier-enterprise` (Tag `v1.0.3-prod-sealed`, Health 200 OK en Render).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura (25/25 pruebas unitarias e integración en 0.136s, 5/5 casos de demo en vivo, 0 fallos).
- **Línea Oficial Única Auditada del Asistente (El '1' en N <-> 1):** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Directiva Soberana Inviolable:** Erradicación total de números no oficiales. Segmentación absoluta:
  * Si el prefijo es **0416 o 0426**: `IS_MOVILNET_SUBSCRIBER = true` -> `CORE_MOVILNET_AUTOGESTION` (Menú de autogestión, saldo, planes, C2P, reposición SIM en agencias).
  * Si el prefijo es **diferente a 0416 y 0426** (0414, 0424, 0412, etc.): `IS_MOVILNET_SUBSCRIBER = false` -> `NO_USUARIOS_MOVILNET` (Portabilidad 4GMAX, eSIM gratis, bono 10GB, entrega física de chip en agencias).

- **Servicios Activos en Producción y Monitoreo Local:**
  * **Servidor en la Nube Blindado (Render):** `https://movilnet-core.onrender.com` (`/health` responde `healthy`, DB `CONNECTED`, Uptime >1200s, desplegado sobre producción).
  * **Portal PWA Móvil 24/7:** `https://movilnet-core.onrender.com/pwa` (HTTP 200 OK).
  * **Orquestador n8n Cloud:** `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY` (Webhook activo en `/webhook/messages_upsert4`, `Edge Carrier Firewall` perimetral booleano, soporte geoespacial para `locationMessage`, enrutamiento determinista).
  * **Centro de Monitoreo Conversacional Local (:8010):** `http://localhost:8010/ui/monitor/conversatorio.html` (Servidor activo en `develop` con demonio HTTP en puerto 8010, verificado 100% saludable).
  * **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.

- **Avances Fundamentales Capítulo 198 (Vía 1: Extracción Física de Hardware GPS Nativo de WhatsApp WGS84):**
  * **Interacción Física Hardware -> SO -> WhatsApp:**
    - El dispositivo móvil/tablet del usuario activa el chip satelital GNSS mediante los permisos del sistema operativo (`ACCESS_FINE_LOCATION` en Android, `NSLocationWhenInUseUsageDescription` en iOS).
    - El módem satelital calcula la posición geodésica exacta WGS84 en el instante en que el usuario toca el clip (📎) o (+) -> *Ubicación* -> *Enviar mi ubicación actual*.
    - WhatsApp empaqueta las coordenadas en `message.locationMessage` o `message.liveLocationMessage` (`degreesLatitude`, `degreesLongitude`, `accuracyInMeters`, `name`, `address`).
  * **Normalización en n8n y Python Core (`core/n8n_webhook_payload_extractor.py`):**
    - Métodos `extract_from_evolution_api`, `extract_from_meta_cloud` y `extract_universal` adaptados para desestructurar `locationMessage` y `location` extrayendo `latitude`, `longitude` y `location_name`.
    - Clasificación automática determinista a la intención `LOCALIZADOR_OFICINAS_TELCO`.
    - Conexión directa en `execute_in_movilnet_core` hacia `FastPathIntentInterceptor` entregando respuesta en <15 ms y 0 tokens LLM.
  * **Catálogo Geoespacial (`core/geo_catalog.py`):**
    - Red de 14 Agencias Comerciales Oficiales sembradas en SQLite cubriendo Caracas, Maracaibo, Valencia, Barquisimeto, Puerto La Cruz, Maracay y San Cristóbal.
    - Fórmulas Haversine exactas, cálculo de distancias, estimación de tiempo a pie y en vehículo, y enlace dinámico de Google Maps.
    - Validación de Bounding Box Nacional WGS84 de Venezuela (`is_point_in_venezuela`) con rechazo perimetral `ERR_OUTSIDE_VENEZUELA`.
  * **Workflow de n8n (`viki_lpgtec_v2_ids_instant_dispatch.json`):**
    - `Edit Fields`: Extrae `msg.locationMessage` / `msg.liveLocationMessage`, asigna `messageType: 'ubicacion'`.
    - `Switch`: Salida `ubicacion` conectada a `Captura Texto`.
    - `Router - Consultas determinísticas`: Condición `telco_movilnet_fastpath` captura ubicaciones GPS y términos de oficinas.
    - `Movilnet Core & Marketing Router`: Cálculo geodésico Haversine en JavaScript y entrega directa formateada.
  * **Certificación Militar (100% PASS):**
    - `core/n8n_webhook_payload_extractor.py --test`: 5/5 pruebas formales OK.
    - `scripts/test_geo_spatial_offices.py`: 12/12 pruebas OK.
    - `scripts/test_edge_carrier_firewall.py`: 6/6 pruebas OK.
    - `scripts/test_pure_greeting_vs_compound_query.py`: 7/7 pruebas OK.
    - `scripts/demo_prueba_geolocalizacion.py`: 5/5 escenarios en vivo OK (Abonado 0416 en Altamira, Prospecto 0414 en Valencia, Consulta textual Maracaibo, Cero Adivinación, Fuera de frontera) en <4 ms y 0 tokens.
    - CLI autónomos (`core/geo_catalog.py --test`, `mcp/geo_tools.py --test`, `core/fastpath_intent_interceptor.py --test`): 100% PASS.

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
