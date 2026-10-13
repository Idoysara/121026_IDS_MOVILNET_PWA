# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-13 12:10 VET | **Capítulo Bitácora:** 171 (Resolución E2E #13810, Enrutamiento Canónico messages_upsert4, Erradicación de Falsa Telemetría ZH-MHEP y Humanización de PWA v169)
- **Declaración Estratégica Ratificada:**
  > *"En Resumen: Diagnóstico forense y solución integral tras la auditoría E2E de EXEC #13810. Se comprobó mediante telemetría dura que el tráfico de Render QR se dirigía al workflow obsoleto WdWU8G9EggQDMack (/webhook/messages_upsert) debido a desalineación en render.yaml. Se corrigió render.yaml hacia el endpoint canónico /webhook/messages_upsert4, se construyó el módulo core/n8n_webhook_resolver.py con auto-promoción defensiva y reintentos en api/service.py, se corrigió el motor de trazas core/conversation_trace_engine.py para erradicar la alucinación de acuses SERVER_ACK en fallos de n8n, se actualizó la PWA index.html eliminando jerga técnica de 'SQLite WAL' con respuestas empáticas, humanas y con indicador de cold start de Render, y se sincronizó el flujo en la nube sNMbtiEiTkuQ9OCY (100% de éxito en ejecuciones #13835-#13839). Suite completa: 397/397 tests aprobados (100% PASS), 10/10 Fases Decagonales APROBADAS y 0 hallazgos en auditoría documental."*
- **Estado de Calidad:** 397 / 397 tests unitarios e integrados aprobados (100% PASS, 0 fallos), 10/10 Fases Decagonales APROBADAS.
- **Módulos del Núcleo Auditados y Actualizados:**
  1. `render.yaml`: Webhook actualizado a `https://n8n.lpgtec.net/webhook/messages_upsert4`.
  2. `core/n8n_webhook_resolver.py`: Módulo autónomo tipado con auto-promoción defensiva y CLI `--test`.
  3. `core/conversation_trace_engine.py`: Cálculo matemático de timers en estado ERROR corregido conforme a ZH-MHEP.
  4. `ui/monitor/conversatorio.html`: Modal de timers con alerta forense RCA específica y sin checks falsos.
  5. `ui/pwa_stitch/index.html` & `simulador.html`: Respuestas de autoservicio humanizadas, detector de cold-start y cache-busting v169.
  6. `tests/test_n8n_webhook_resolver.py` & `tests/test_process_timers.py`: Tests unitarios añadidos y validados.
- **Reportes Sellados Criptográficamente:**
  * Replicación PWA: `reports/pwa_replication_certification.json` (`SHA256:5d93d2a84a2ed7928e0173e741afe5cf2c999d59853ed9cd1ed433a1387c8425`).
  * Despliegue en la Nube: `reports/cloud_deployment_readiness_report.json` (`SHA256:28ab5135faf0db8f4c8405f56b9bcd611f10a976c06f576ff8ab50a6d0dd0dc8`).
- **Enlaces Mágicos de WhatsApp ➔ Nube Validados:**
  * Local Conversatorio: `http://localhost:8010/ui/monitor/conversatorio.html`
  * Simulador QR: `http://localhost:8010/ui/pwa_stitch/simulador.html?v=169`
  * Render: `https://movilnet-core.onrender.com/ui/pwa_stitch/index.html?phone=04142554590&v=169`
  * n8n Cloud Canvas: `https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY`
- **Servicios Activos en Background:**
  * Movilnet Core Activo en puerto dedicado 8010 (`api/service.py`, PID 47813).
  * Supervisor en Vivo activo como demonio (`scripts/live_core_supervisor.py --daemon`), operando en estado `ACTIVE_SUPERVISING`.
- **Guardarraíles Anti-Alucinación Activos:**
  1. Reglas Always-On: `.agents/rules/zh-mhep-zero-hallucination.md` y `.agents/rules/protocolo-decagonal-garantia-calidad.md`.
  2. Guardián 10 Fases: `scripts/quality_gatekeeper_10phases.py --audit` (10/10 PASS, 82 módulos AST).
  3. Auditor Documental: `scripts/audit_docs_evidence.py --audit` (0 hallazgos).
  4. Escáner de Seguridad: `scripts/scan_skill_security.py --test` (5/5 PASS, SAFE 0.0/100).
- **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.
- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*.
