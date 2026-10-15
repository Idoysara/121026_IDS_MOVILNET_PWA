# 📡 AI_Movilnet_300926 — Asistente Cognitivo Carrier-Grade para Telecomunicaciones Movilnet C.A.

> **Ecosistema Inteligente Autónomo Nivel 5 Antigravity AI — Fases 0 a 5 Certificadas**  
> Microservicios REST TM Forum ODA, Orquestación Omnicanal en n8n Enterprise & MCP Server, Enjambre Swarm L5, Motor de Reglas Departamentales Hot-Reload (<3ms), Integración Google Suite, PWA Mobile-First y Lanzadores Autónomos.

---

## 🎯 Resumen del Proyecto

Este repositorio alberga la plataforma de producción de **Telecomunicaciones Movilnet C.A.** diseñada para atender a más de 4 millones de abonados (`0416` / `0426`) con arquitectura carrier-grade de nivel militar:

- **Tests Automatizados:** ✅ **499 / 499 pruebas certificadas (100% OK / 0 fallos)** (474 en `tests/` + 25 en `scripts/test_*.py`).
- **Capa de Datos:** PostgreSQL 15 particionado Hash/Range + failover transparente a SQLite WAL en $O(1)$ (0.053 ms) con 13 tablas normalizadas TM Forum ODA y Catálogo Geoespacial Nacional (`geo_pois`, 1.239 agencias indexadas).
- **Microservicio Core:** REST API con 31 endpoints certificados bajo OpenAPI 3.1.0 TM Forum (TMF620, TMF621, TMF676, TMF678, TMF680, TMF688), modo exclusivo de datos PWA (`DATA_PWA_EXCLUSIVE`).
- **Swarm Cognitivo L5 & Arquitectura Anti-Acumulador:**
  1. **Comercial / Ventas N1:** Planes Inteliplan 10GB/20GB/50GB, bonos de portabilidad 10GB y embudo eSIM.
  2. **FinTech C2P N2:** Pagos móviles interbancarios SUDEBAN (50 a 50.000 Bs), BCV oficial y receptor `0424-1533712`.
  3. **Atención / Soporte N1:** Fast-Path determinista en <15ms (0 tokens), horarios humanos y SLAs de reclamos.
  4. **Seguridad / CONATEL N3:** Validación IMEI por algoritmo de Luhn (15 dígitos), lista negra EIR y Zero-PII (<30ms RAM).
  5. **Operaciones de Red / NOC N5:** Detección de radiobases, boletines técnicos zonales y supresión de averías falsas.
  6. **Retención / Churn N4:** Modelo analítico Scikit-Learn de predicción de abandono y ofertas Next-Best-Action.
  7. **Compuerta de Dominio Telco:** `OFF_TOPIC_TELCO_GUARD` para desvío inmediato de gastronomía/comercio ajeno a directorios locales desde navegación 4GMAX.
- **Catálogo de Reglas Departamentales Hot-Reload:** Directorio declarativo `config/department_rules/` administrable en caliente en 2.14 ms vía cerrojo multihilo `threading.RLock()`.
- **Omnicanalidad & n8n Live MCP:** Workflow canónico en producción `sNMbtiEiTkuQ9OCY` conectado a Evolution API (`+58 424 153 3712` / **MOVI**).
- **Google Suite Enterprise:** Conectores MCP activos para Drive, Sheets, Docs, Calendar y Gmail con cuotas y circuit breakers.
- **Seguridad de Agentes (NVIDIA SkillSpector):** Escáner AST de malware, troyanos y jailbreaks para skills y tools.
- **Conversatorio & Monitoreo E2E:** Observabilidad del Webhook bot `+58 424 153 3712` en `:8010/ui/monitor/conversatorio.html` con flags de entrega verificada (`DELIVERY_ACK`).
- **Experiencia de Usuario (UI/UX/AX):** PWA Mobile-First responsive (`https://movilnet-core.onrender.com/prospect` y `/ui/pwa_stitch/index.html`) con continuidad de sesión en `sessionStorage` (`movilnet_pwa_session_id`) y simuladores nativos.
- **Despliegue en la Nube 24/7:** Servicio activo en Render (`movilnet-core.onrender.com`) y n8n Cloud (`n8n.lpgtec.net`).
- **Entregables Soberanos de Doble Clic:** Scripts `.command` para macOS (`reiniciar_todo_limpio.command`, `probar_geolocalizacion.command`, `verificar_whatsapp_sin_celular.command`).
- **Entorno de Trabajo:** Rama aislada **`develop`** (Rastreando `origin/develop`), físicamente desacoplada de la producción en Render Cloud.
- **Blindaje de Producción:** Protegido bajo la regla institucional `.agents/rules/regla-inviolable-pase-produccion.md` (Cero despliegue a producción sin orden humana directa y respaldo previo sellado con SHA-256).
- **Respaldo Soberano Certificado:** `141026_Movilnet_Core_PWA` sellado con hash SHA-256 (Capítulos 1 al 206).

---

## 🏛️ Arquitectura de Carpetas

```
AI_Movilnet_300926 / 141026_Movilnet_Core_PWA/
├── MANIFIESTO_ARQUITECTURA_Y_COMPONENTES_141026.md # Manifiesto maestro y mapa de componentes
├── PUNTO_DE_CONTROL_SESION_ACTIVA.md               # Punto de control y memoria de sesión
├── ACTUALIZAR_REGLAS_DEPARTAMENTALES.command       # Lanzador 1-Clic de recarga en caliente de reglas
├── EJECUTAR_PRUEBA_REAL.command                    # Lanzador 1-Clic de prueba E2E
├── config/
│   └── department_rules/ # Catálogos JSON de 5 departamentos (Comercial, Finanzas, Atención, Seguridad, NOC)
├── api/                  # Microservicio REST, Contrato OpenAPI y Enjambre de Agentes
│   ├── agents/           # Agentes N1 a N5, Funnel Marketing y Geoespaciales
│   ├── n8n_workflows/    # Workflows Canónicos exportados en JSON
│   └── webhook_bridge.py # Puente de Webhooks HMAC con DLQ y backoff
├── core/                 # Motor de reglas hot-reload, enrutadores semánticos, trazador conversacional
├── db/                   # DDL ODA, conectores con pooling y repositorio seguro Zero-PII
├── docs/                 # Bitácora continua (Capítulos 1-180) y documentos maestros
├── mcp/                  # Suites MCP (Telco, Fintech, NOC, CRM, Privacy, Omnicanal, Geo, Google, SkillSpector)
├── reports/              # Certificados criptográficos SHA-256 y manifiesto de respaldo
├── scripts/              # Validador de reglas, pipelines de despliegue, SRE Watchdog y clientes CLI
├── tests/                # 430 tests unitarios, de estrés, de integración y live connectors (100% PASS)
└── ui/                   # Portal web, Conversatorio en vivo, Dashboard NOC y PWA Stitch
```

---

## 🚀 Despliegue y Ejecución

### Opción 1: Lanzadores de Doble Clic (macOS — Pilar VII: Cero Terminal)
- `EJECUTAR_PRUEBA_REAL.command`: Chequeo de salud del sistema y apertura de la Sala de Control sin abrir pestañas innecesarias.
- `ACTUALIZAR_REGLAS_DEPARTAMENTALES.command`: Valida y recarga en caliente las reglas de los 5 departamentos en 2.14 ms sin reiniciar el servidor.
- `REINICIAR_SERVICIOS_MOVILNET.command`: Reinicia en limpio los servicios locales del puerto 8010 y el supervisor de sincronización en vivo.
- `PROBAR_PWA_CELULAR.command`: Detecta la red Wi-Fi y genera el enlace y código QR para probar la PWA en celulares físicos.
- `ACTUALIZAR_RENDER_1CLIC.command`: Dispara el Deploy Hook de Render para actualizar la nube en 60 segundos.

### Opción 2: Consola de Comandos
```bash
# Ejecutar suite completa de 430 pruebas (100% PASS)
./venv/bin/pytest tests/

# Validar catálogo de reglas departamentales
./venv/bin/python3 scripts/validate_department_rules.py --test

# Arrancar microservicio REST API (puerto 8010, aislado por agy-port-guardian)
python3 api/service.py  # o doble clic en REINICIAR_SERVICIOS_MOVILNET.command
```

---
*Telecomunicaciones Movilnet C.A. — La señal que nos une.*
