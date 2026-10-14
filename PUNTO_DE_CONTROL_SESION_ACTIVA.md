# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 18:58 VET | **Capítulos Bitácora:** 183 al 200 (Desacoplamiento Celular Físico Zero-Phone, Regla Única Línea Central +58 424 153 3712, Supresión de Tarjetas Falsas `linkPreview`, Despliegue en Render, Centro de Monitoreo :8010, Blindaje Inmutable de Producción `v1.0.0-prod-sealed`, Diagnóstico Forense Estado 'PENDING' en Evolution API, Regla General de Cero Adivinación y Datos Faltantes, Clasificador "Saludo Puro" vs "Consulta Compuesta", Módulo Exclusivo NO_USUARIOS_MOVILNET, Erradicación Total de Secuestro Comercial Ciego, Releases `v1.0.1-prod-sealed`, `v1.0.2-prod-sealed`, `v1.0.3-prod-sealed`, `v1.0.4-prod-sealed`, Firewall Booleano `IS_MOVILNET_SUBSCRIBER` 0416/0426, Hardware GPS WhatsApp Nativo, e Ingesta Integral Certificada del Censo Nacional de 1.017 Puntos de Atención Oficiales Movilnet con Sello Inmutable SHA-256).
- **Estado de Producción:** 🔒 **PROD_LOCKED_AND_SHIELDED** (Rama `main` congelada bajo tag inmutable `v1.0.4-prod-sealed`, sincronizado en GitHub `Idoysara/121026_IDS_MOVILNET_PWA`, Render Cloud y n8n Cloud).
- **Entorno de Trabajo Activo:** 🏛️ Rama Git **`main`** (Promovido formalmente tras autorización humana en Capítulo 200).
- **Versión de Producción:** `v1.0.4-carrier-enterprise` (Tag `v1.0.4-prod-sealed`).
- **Estado de Calidad:** 100% PASS en todas las suites de arquitectura (28/28 pruebas unitarias e integración en <0.3s, 5/5 casos de demo en vivo, 0 fallos).
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

- **Avances Fundamentales Capítulo 199 (Ingesta y Certificación del Censo Nacional Movilnet - 1.017 Puntos Físicos):**
  * **Fuentes Oficiales Auditadas y Parseadas:**
    - `http://www.movilnet.com.ve/sitio/minisitios/atencion_cliente/` (Oficinas de Servicio y Atención al Cliente - OSAC).
    - `http://www.movilnet.com.ve/sitio/minisitios/agentes_autorizados` (Directorio Nacional de Agentes Autorizados por estado).
    - `http://www.movilnet.com.ve/sitio/minisitios/aci` (Directorio Nacional de Agentes Comerciales Integrales por estado).
    - Mapa Oficial Google My Maps: `https://www.google.com/maps/d/viewer?mid=1s5YtrIng5l2BkgUoAxf1ZLR7sBYSDbw`.
  * **Estructura Consolidada en Base de Datos (`db/local_movilnet.db` -> `geo_pois`):**
    - **1 Sede Central Corporativa:** Torre Movilnet (Torre Sur CC El Recreo, Sabana Grande / Bello Monte, Caracas).
    - **31 Oficinas de Servicio y Atención al Cliente (OSAC):** Despliegue en todos los polos comerciales del país (El Recreo, Metrocenter, CCCT, Sambil La Candelaria, Sambil Chacao, Centro Plaza, Buenaventura Guatire, Charallave, San Antonio, Torre Valencia Kerdell, Metrópolis Valencia, Las Américas Maracay, San Juan de los Morros, San Fernando de Apure, Barinas El Dorado, Mérida Tibisay, San Cristóbal Barrio Obrero, Metrópolis Barquisimeto, Las Trinitarias, Buenaventura Araure, Puerto Ordaz, Orinoco Ciudad Bolívar, Monagas Plaza Maturín, Sambil Paraguaná, Valera Plaza, 5 de Julio Maracaibo, Bella Vista Maracaibo, Cabimas Center, Plaza Mayor Lechería/PLC, Porlamar AB, Cumaná Plaza).
    - **500 Agentes Autorizados (AA):** Distribuidos en los 24 estados federales.
    - **485 Agentes Comerciales Integrales (ACI):** Distribuidos a nivel nacional.
    - **TOTAL GENERAL:** **1.017 puntos físicos certificados**.
  * **Sello Inmutable Criptográfico:**
    - Archivo exportado: `data/censo_oficial_movilnet_puntos_atencion.json` (1.017 registros estructurados).
    - **Hash SHA-256:** `a9d3578b5dbfa52b16f5692dfdbe4f713d0f7829ea97d2fec749220eea4eb492`.
  * **Priorización de Respuesta en el Asistente:**
    - Ante consultas geográficas o pines GPS, el FastPath prioriza OSACs y Sedes Corporativas directas (para trámites de alta complejidad como eSIM/USIM, cambio de titularidad, planes Conapdis/Solidario/Juventud) y entrega además los Agentes Autorizados/ACIs más cercanos para compras rápidas y recargas.
  * **Certificación Militar (100% PASS):**
    - `scripts/build_certified_movilnet_geo_dataset.py --test`: 100% PASS.
    - `core/geo_catalog.py --test`: 100% PASS.
    - `core/n8n_webhook_payload_extractor.py --test`: 100% PASS.
    - `scripts/test_geo_spatial_offices.py`: 12/12 pruebas OK.
    - `scripts/test_edge_carrier_firewall.py`: 6/6 pruebas OK.
    - `scripts/test_pure_greeting_vs_compound_query.py`: 7/7 pruebas OK.
    - `core/fastpath_intent_interceptor.py --test`: 11/11 pruebas OK.
    - `scripts/demo_prueba_geolocalizacion.py`: 5/5 escenarios en vivo OK en <18 ms y 0 tokens LLM.
    - `scripts/probar_geolocalizacion_interactivo.py --test`: 3/3 pruebas OK.

- **Avances Fundamentales Capítulo 200 (Promoción Oficial y Despliegue en Producción v1.0.4-prod-sealed):**
  * **Autorización Humana Soberana:** El usuario validó en vivo el simulador interactivo con `04142554590` + consulta en Caracas (29.02 ms, 0 tokens, oferta de portabilidad 10GB + agencias OSAC CCCT/Centro Plaza/El Recreo) y emitió la orden formal: *"opcion C , autorizo pase produccion"*.
  * **Integración en Rama Principal (`main`):** Fast-forward merge limpio de `develop` a `main`.
  * **Sello Criptográfico Inmutable:** Etiqueta Git inmutable `v1.0.4-prod-sealed` creada con hash SHA-256 del censo `a9d3578b5dbfa52b16f5692dfdbe4f713d0f7829ea97d2fec749220eea4eb492`.
  * **Lanzador Soberano macOS:** `scripts/probar_geolocalizacion.command` para ejecución de pruebas en caliente con doble clic en Finder sin terminal.

- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.

