# 📡 AI_Movilnet_300926 — Asistente Cognitivo Carrier-Grade para Telecomunicaciones Movilnet C.A.

> **Ecosistema Inteligente Autónomo Nivel 5 Antigravity AI — Fases 0 a 5 Certificadas**  
> Microservicios REST TM Forum ODA, Orquestación Omnicanal en n8n Enterprise & MCP Server, Enjambre Swarm L5, Integración Google Suite, PWA Mobile-First y Lanzadores Autónomos.

---

## 🎯 Resumen del Proyecto

Este repositorio alberga la plataforma de producción de **Telecomunicaciones Movilnet C.A.** diseñada para atender a más de 4 millones de abonados (`0416` / `0426`) con arquitectura carrier-grade de nivel militar:

- **Tests Automatizados:** ✅ **423 / 423 pruebas certificadas (100% OK / 0 fallos)** en 46 suites.
- **Capa de Datos:** PostgreSQL 15 particionado Hash/Range + failover transparente a SQLite WAL en $O(1)$ (0.053 ms) con 13 tablas normalizadas TM Forum ODA.
- **Microservicio Core:** REST API con 28 endpoints certificados bajo OpenAPI 3.1.0 TM Forum (TMF620, TMF621, TMF676, TMF678, TMF680, TMF688), modo exclusivo de datos PWA (`DATA_PWA_EXCLUSIVE`).
- **Swarm Cognitivo L5:** 4 Agentes Especializados (Atención N1 con Gemini 2.5 Flash / Fast-Path ODA Zero-Token, Fintech C2P N2, EIR Emergencias N3, Churn ML N4) + Subagentes Geoespaciales y Funnel Marketing Digital (NBA).
- **Omnicanalidad & n8n Live MCP:** Workflow canónico en producción `sNMbtiEiTkuQ9OCY` conectado a Evolution API (`+58 424 153 3712` / **MOVI**).
- **Google Suite Enterprise:** Conectores MCP activos para Drive, Sheets, Docs, Calendar y Gmail con cuotas y circuit breakers.
- **Seguridad de Agentes (NVIDIA SkillSpector):** Escáner AST de malware, troyanos y jailbreaks para skills y tools.
- **Conversatorio & Monitoreo E2E:** Observabilidad del Webhook bot `+58 424 153 3712` en `:8010/ui/monitor/conversatorio.html` con flags de entrega verificada (`DELIVERY_ACK`).
- **Experiencia de Usuario (UI/UX/AX):** PWA Mobile-First responsive (`https://movilnet-core.onrender.com/prospect` y `/ui/pwa_stitch/index.html`) con simuladores nativos independientes de WhatsApp, Celular y Tablet.
- **Despliegue en la Nube 24/7:** Servicio activo en Render (`movilnet-core.onrender.com`) y n8n Cloud (`n8n.lpgtec.net`).
- **Entregables Soberanos de Doble Clic:** Scripts `.command` para macOS (`EJECUTAR_PRUEBA_REAL.command`, `REINICIAR_SERVICIOS_MOVILNET.command`, `PROBAR_PWA_CELULAR.command`, `ACTUALIZAR_RENDER_1CLIC.command`).
- **Respaldo Soberano Certificado:** `141026_Movilnet_Core_PWA` (`/Users/ismael/Desktop/121026_CORE_MOVILNET/Movilnet_141026/`) sellado con hash SHA-256 (`dd3e1a6cd7b921acf712c5ac8c237f370716fcb4718e7b0a57cbc2cb8dfbcbde`).

---

## 🏛️ Arquitectura de Carpetas

```
AI_Movilnet_300926 / Movilnet_PWA/
├── MANIFIESTO_ARQUITECTURA_Y_COMPONENTES_141026.md # Manifiesto maestro y mapa de componentes
├── PUNTO_DE_CONTROL_SESION_ACTIVA.md               # Punto de control y memoria de sesión
├── api/                  # Microservicio REST, Contrato OpenAPI y Enjambre de Agentes
│   ├── agents/           # Agentes N1 a N4, Funnel Marketing y Geoespaciales
│   ├── n8n_workflows/    # Workflows Canónicos exportados en JSON
│   └── webhook_bridge.py # Puente de Webhooks HMAC con DLQ y backoff
├── core/                 # Enrutadores semánticos, pasarela de modelos, trazador conversacional
├── db/                   # DDL ODA, conectores con pooling y repositorio seguro Zero-PII
├── docs/                 # Bitácora continua (Capítulos 1-177) y documentos maestros
├── mcp/                  # Suites MCP (Telco, Fintech, CRM, Privacy, Omnicanal, Geo, Google, SkillSpector)
├── reports/              # Certificados criptográficos SHA-256 y manifiesto de respaldo
├── scripts/              # Pipelines de despliegue, SRE Watchdog, auditores y clientes CLI
├── tests/                # 423 tests unitarios, de estrés, de integración y live connectors
└── ui/                   # Portal web, Conversatorio en vivo, Dashboard NOC y PWA Stitch
```

---

## 🚀 Despliegue y Ejecución

### Opción 1: Lanzadores de Doble Clic (macOS — Pilar VII: Cero Terminal)
- `EJECUTAR_PRUEBA_REAL.command`: Chequeo de salud del sistema y apertura de la Sala de Control sin abrir pestañas innecesarias.
- `REINICIAR_SERVICIOS_MOVILNET.command`: Reinicia en limpio los servicios locales del puerto 8010 y el supervisor de sincronización en vivo.
- `PROBAR_PWA_CELULAR.command`: Detecta la red Wi-Fi y genera el enlace y código QR para probar la PWA en celulares físicos.
- `ACTUALIZAR_RENDER_1CLIC.command`: Dispara el Deploy Hook de Render para actualizar la nube en 60 segundos.

### Opción 2: Consola de Comandos
```bash
# Ejecutar suite completa de 423 pruebas
./venv/bin/pytest tests/

# Arrancar microservicio REST API (puerto 8010, aislado por agy-port-guardian)
python3 api/service.py  # o doble clic en REINICIAR_SERVICIOS_MOVILNET.command
```

# Iniciar suite completa con Docker Compose
docker compose -f docker-compose.prod.yml up -d
```

---
*Telecomunicaciones Movilnet C.A. — La señal que nos une.*

