# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 17:45 VET | **Capítulos Bitácora:** 183 al 197 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712, Supresión de Tarjetas Falsas `linkPreview`, Despliegue en Render, Centro de Monitoreo :8010, Blindaje Inmutable de Producción `v1.0.0-prod-sealed`, Diagnóstico Forense Estado 'PENDING' en Evolution API, Regla General de Cero Adivinación y Datos Faltantes, Clasificador "Saludo Puro" vs "Consulta Compuesta", Módulo Exclusivo NO_USUARIOS_MOVILNET, Erradicación Total de Secuestro Comercial Ciego, Releases `v1.0.1-prod-sealed`, `v1.0.2-prod-sealed`, `v1.0.3-prod-sealed`, Firewall Booleano `IS_MOVILNET_SUBSCRIBER` 0416/0426, e Implementación Integral Opción A: Geolocalización Oficial de Oficinas Comerciales Movilnet con Skills Locales, Protocolo MCP y Zero-Token Fast-Path).
- **Estado de Producción:** 🔒 **PROD_LOCKED_AND_SHIELDED** (Rama `main` congelada bajo tag inmutable `v1.0.3-prod-sealed`, sincronizado en GitHub `Idoysara/121026_IDS_MOVILNET_PWA`, Render Cloud y n8n Cloud).
- **Entorno de Trabajo Activo:** 🛠️ Rama Git **`develop`** (Desarrollo y pruebas locales activas).
- **Versión de Producción:** `v1.0.3-carrier-enterprise` (Tag `v1.0.3-prod-sealed`, Health 200 OK en Render).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura (25/25 pruebas unitarias e integración en 0.136s, 0 fallos).
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

- **Avances Fundamentales Capítulo 197 (Geolocalización Oficial de Oficinas Movilnet - Opción A):**
  * **Catálogo Geoespacial (`core/geo_catalog.py`):**
    - Red de 14 Agencias Comerciales Oficiales sembradas en SQLite (`geo_pois` bajo categoría `oficina_comercial_movilnet`) cubriendo Caracas (Centro Plaza, El Rosal, Sambil Chacao, CCCT, Sambil La Candelaria, El Recreo), Maracaibo (5 de Julio, Lago Mall), Valencia (Metrópolis, Sambil Valencia), Barquisimeto (Las Trinitarias), Puerto La Cruz (Plaza Mayor), Maracay (Las Américas) y San Cristóbal (Sambil).
    - Fórmulas Haversine exactas, cálculo de distancias, estimación de tiempo a pie (~80 m/min) y en vehículo (~500 m/min), y enlace dinámico de Google Maps.
    - Validación de Bounding Box Nacional WGS84 de Venezuela (`is_point_in_venezuela`: Lat 0.60°N a 12.50°N | Lon -73.50°W a -59.80°W) con rechazo perimetral `ERR_OUTSIDE_VENEZUELA`.
  * **Suite MCP JSON-RPC 2.0 (`mcp/geo_tools.py`):**
    - Herramientas expuestas: `mcp_geo_find_nearest_agency`, `mcp_geo_find_agencies_by_city`, `mcp_geo_spatial_search`, `mcp_geo_validate_boundaries`.
  * **Sub-Agentes Autónomos (`api/agents/`):**
    - `GeoSpatialAgent`: Cálculo de rutas y resolución de distancias.
    - `GeoValidationAgent`: Auditoría territorial y certificación INE/IGVSB.
  * **Interceptor Fast-Path ODA Zero-Token (`core/fastpath_intent_interceptor.py`):**
    - Intención `LOCALIZADOR_OFICINAS_TELCO`: resuelve en <15 ms y 0 tokens LLM.
    - **Regla Inviolable de Cero Adivinación y Datos Faltantes:** Si el usuario no envía GPS ni menciona una ciudad, solicita educadamente que comparta su pin o escriba su ciudad. Nunca adivina ni asume Caracas.
    - Diferenciación de copy comercial: Abonados `0416/0426` reciben trámites de autogestión (reposición SIM, planes, C2P); No-usuarios reciben captación de Portabilidad con bono de 10GB.
  * **Workflow de n8n (`viki_lpgtec_v2_ids_instant_dispatch.json`):**
    - Nodo `Edit Fields`: Extrae `msg.locationMessage` o `liveLocationMessage`, asigna `messageType: 'ubicacion'` y genera payload estructurado `location`.
    - Nodo `Switch`: Regla para `ubicacion` enrutada a `Captura Texto`.
    - Nodo `Router - Consultas determinísticas`: Condición `telco_movilnet_fastpath` ampliada para capturar ubicaciones GPS y términos de oficinas.
    - Nodo `Movilnet Core & Marketing Router`: Cálculo geodésico Haversine en JavaScript y entrega directa formateada.
  * **Certificación Militar (100% PASS):**
    - `scripts/test_geo_spatial_offices.py`: 12/12 pruebas OK.
    - Suite completa combinada (`test_geo_spatial_offices.py`, `test_edge_carrier_firewall.py`, `test_pure_greeting_vs_compound_query.py`): 25/25 pruebas OK en 0.136s.
    - CLI autónomos (`core/geo_catalog.py --test`, `mcp/geo_tools.py --test`, `api/agents/agent_geo_spatial.py --test`, `api/agents/agent_geo_validation.py --test`, `core/fastpath_intent_interceptor.py --test`): 100% PASS.
  * **Documentación Técnica:**
    - Generada en `Documento/ARQUITECTURA_GEOLOCALIZACION_MOVILNET.md` con matriz de trazabilidad Mermaid de 5 capas (`Inputs <--> Nodos n8n <--> Python Core <--> MCP/Agentes/Skills <--> Outputs`).

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
