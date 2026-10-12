# 📡 AI_Movilnet_300926 — Asistente Cognitivo Carrier-Grade para Telecomunicaciones Movilnet C.A.

> **Ecosistema Inteligente Autónomo Nivel 5 Antigravity AI — Fases 0 a 5 Certificadas**  
> Microservicios REST TM Forum ODA, Orquestación Omnicanal en n8n Enterprise & MCP Server, Enjambre Swarm L5, Integración Google Suite, PWA Mobile-First y Lanzadores Autónomos.

---

## 🎯 Resumen del Proyecto

Este repositorio alberga la plataforma de producción de **Telecomunicaciones Movilnet C.A.** diseñada para atender a más de 4 millones de abonados (`0416` / `0426`) con arquitectura carrier-grade de nivel militar:

- **Tests Automatizados:** ✅ **388 / 388 pruebas certificadas (100% OK / 0 fallos)**.
- **Capa de Datos:** PostgreSQL 15 particionado Hash/Range + failover transparente a SQLite WAL en $O(1)$ (0.053 ms).
- **Microservicio Core:** REST API con 28 endpoints certificados bajo OpenAPI 3.1.0 TM Forum (TMF620, TMF621, TMF676, TMF678, TMF680, TMF688).
- **Swarm Cognitivo L5:** 4 Agentes Especializados (Atención N1 con Gemini 3.8 Flash, Fintech C2P N2, EIR Emergencias N3, Churn ML N4) + Subagentes Geoespaciales y Funnel Marketing Digital (NBA).
- **Omnicanalidad & n8n Live MCP:** Workflow canónico en producción `sNMbtiEiTkuQ9OCY` (80 nodos) conectado a Evolution API (`+58 416 625 1587`).
- **Google Suite Enterprise:** Conectores MCP activos para Drive, Sheets, Docs, Calendar y Gmail con cuotas y circuit breakers.
- **Seguridad de Agentes (NVIDIA SkillSpector):** Escáner AST de malware, troyanos y jailbreaks para skills y tools.
- **Conversatorio 2 Columnas & Monitoreo E2E:** Observabilidad del Webhook bot `+58 416 625 1587` con 50 interacciones indexadas en tiempo real en `:8010/ui/monitor/conversatorio.html`.
- **Experiencia de Usuario (UI/UX/AX):** PWA Mobile-First responsive con simuladores nativos independientes de WhatsApp, Telegram, Celular y Tablet.
- **Despliegue en la Nube 24/7 (Modo A):** Contenedores Docker multi-stage con usuario no-root, soporte IaC para Render (`render.yaml`) y Railway (`railway.json`) en Plan Free $0.00 USD.
- **Entregables Soberanos de Doble Clic:** Scripts `.command` para macOS (`INICIAR_MOVILNET_PWA.command`, `PROBAR_PWA_CELULAR.command`, `DESPLEGAR_A_LA_NUBE.command`, `INICIAR_MONITOR_SECUENCIAS.command`, `CONECTAR_N8N_EN_VIVO.command`).

---

## 🏛️ Arquitectura de Carpetas

```
AI_Movilnet_300926/
├── api/                  # Microservicio REST, Contrato OpenAPI y Enjambre de Agentes
│   ├── agents/           # Agentes N1 a N4, Funnel Marketing y Geoespaciales
│   ├── n8n_workflows/    # Workflows Canónicos exportados en JSON
│   └── webhook_bridge.py # Puente de Webhooks HMAC con DLQ y backoff
├── core/                 # Enrutadores semánticos, pasarela de modelos, trazador conversacional
├── db/                   # DDL ODA, conectores con pooling y repositorio seguro Zero-PII
├── docs/                 # Bitácora continua (Capítulos 1-138) y documentos maestros
├── mcp/                  # 8 Suites MCP (Telco, Fintech, CRM, Privacy, Omnicanal, Geo, Google, SkillSpector)
├── reports/              # Certificados criptográficos SHA-256 de todas las fases (0 a 5)
├── scripts/              # Pipelines de despliegue, SRE Watchdog, auditores y clientes CLI
├── tests/                # 322 tests unitarios, de estrés, de integración y live connectors
└── ui/                   # Portal web, Conversatorio 2 columnas, Dashboard NOC y PWA
```

---

## 🚀 Despliegue y Ejecución

### Opción 1: Lanzadores de Doble Clic (macOS)
- `INICIAR_MOVILNET_PWA.command`: Levanta el microservicio backend y la PWA con simulador móvil en el navegador.
- `PROBAR_PWA_CELULAR.command`: Detecta la red Wi-Fi y genera el enlace exacto para probar la PWA en el celular físico.
- `DESPLEGAR_A_LA_NUBE.command`: Guía de 1 clic para publicar el servicio 24/7 en Render o Railway ($0.00 USD).
- `INICIAR_MONITOR_SECUENCIAS.command`: Abre el Conversatorio de 2 Columnas (`http://localhost:8010/ui/monitor/conversatorio.html`).
- `CONECTAR_N8N_EN_VIVO.command`: Conecta y valida en vivo el servidor n8n MCP.

### Opción 2: Consola de Comandos
```bash
# Ejecutar suite completa de 388 pruebas
./venv/bin/pytest tests/

# Arrancar microservicio REST API (puerto 8010, aislado por agy-port-guardian)
python3 api/service.py  # o doble clic en INICIAR_MONITOR_SECUENCIAS.command

# Iniciar suite completa con Docker Compose
docker compose -f docker-compose.prod.yml up -d
```

---
*Telecomunicaciones Movilnet C.A. — La señal que nos une.*

