# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-13 18:50 VET | **Capítulo Bitácora:** 175 (Resolución DEFCON 1: Erradicación de Enlace Inexistente pwa.movilnet.com.ve, Nube Render 24/7 y Portabilidad In-Chat WhatsApp)
- **Declaración Estratégica Ratificada:**
  > *"Incidente DEFCON 1 Resuelto: El dominio inexistente 'pwa.movilnet.com.ve' (NXDOMAIN en celulares móviles 3G/4G/5G) fue erradicado y reemplazado en n8n Cloud y en el Core por la URL pública funcional 24/7 en Render: 'https://movilnet-core.onrender.com/ui/pwa_stitch/index.html'. Adicionalmente, se habilitó la Portabilidad Express directamente en el chat de WhatsApp ('Responde Portabilidad por aquí') para máxima accesibilidad sin depender de navegación externa."*
- **Estado de Calidad:** 422 / 422 tests aprobados (100% PASS, 0 fallos en 25.05s en 46 suites).
- **Línea Activa Oficial del Bot (El '1' en N <-> 1):** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
- **Comando Maestro de Prueba Real (1 Clic / Cero Terminal):**
  * Lanzador macOS: `EJECUTAR_PRUEBA_REAL.command` (Doble clic directo).
  * Script CLI Autónomo: `scripts/ejecutar_prueba_real.py` (`--test`, `--no-open`, `--message`, `--timeout`).
  * Suite de Pruebas: `tests/test_ejecutar_prueba_real.py` (4/4 PASS).
  * Aislamiento de Interfaz: Solo abre la Sala de Control (`conversatorio.html`) en la Mac; no abre pestañas de WhatsApp Web, preservando la interacción en el móvil físico.
- **Arquitectura de Reglas Departamentales Hot-Reload (Capítulo 174):**
  * Catálogo Declarativo: `config/department_rules/` (5 departamentos: Comercial, Finanzas C2P, Soporte, Seguridad/CONATEL y NOC).
  * Motor de Recarga: `DepartmentRuleEngine` (<5ms en memoria volátil, `threading.RLock()`, endpoint `/api/v1/rules/reload`).
  * Validador Soberano: `ACTUALIZAR_REGLAS_DEPARTAMENTALES.command` / `scripts/validate_department_rules.py`.
- **Parametrización Central de Entorno:**
  * Variables en `.env` y `.env.example`: `MOVILNET_ACTIVE_BOT_PHONE=0424-1533712` y `MOVILNET_BOT_NAME=MOVI`.
  * Gestor Singleton: `core/system_config.py` (`SystemConfigManager`, `get_active_bot_phone()`, `get_allowed_bot_senders()`).
- **Suite Universal de Migración Telefónica:**
  * Módulo de Dominio: `core/phone_migration_models.py` (`PhoneDescriptor`, 7 formatos canónicos, clasificación CONATEL).
  * Orquestador Transaccional: `core/phone_migration_orchestrator.py` (`--plan`, `--apply`, rollback automático AST en `.backups/phone_migration/`).
  * Servidor MCP: `mcp/phone_migration_mcp.py` (`phone-migration-guardian`).
  * Skill: `.agents/skills/agy-phone-migration-guardian/SKILL.md`.
- **Suite de Blindaje del Protocolo PWA (*"WPA"*):**
  * Motor Central: `core/pwa_protocol_guardian.py` (Auditoría de 14 puntos, bump de Service Worker `sw.js` Network-First Zero-Stale, verificación Zero-Token en $<15\text{ ms}$).
  * Servidor MCP: `mcp/pwa_protocol_mcp.py` (`pwa-protocol-guardian`).
  * Skill: `.agents/skills/agy-pwa-protocol-guardian/SKILL.md`.
  * Simulador NOC: `ui/pwa_stitch/simulador.html` con Códigos QR dinámicos Dual-Mode (WhatsApp Direct vs PWA Web).
- **Flujo n8n en Producción:** `sNMbtiEiTkuQ9OCY` (Webhook canónico `/webhook/messages_upsert4`, Prompt `AI Agent` sincronizado a `MOVI (+58 424 153 3712)` y router Pago Móvil C2P a `0424-1533712`).
- **Líneas Externas de Prueba Auditadas:** `+58 414 255 4590` (Movistar, remitente `Ids`), `+58 414 265 0088` (remitente `Francisco Landaeta`) y `04160000001` (Movilnet 4GMAX).
- **Servicios Activos en Background:**
  * Movilnet Core activo en puerto dedicado 8010 (`api/service.py`, PID 47813).
  * Supervisor en Vivo activo (`scripts/live_core_supervisor.py --daemon`).
- **Centro de Monitoreo Conversacional E2E:** `http://localhost:8010/ui/monitor/conversatorio.html`.
- **Guardarraíles Anti-Alucinación y Seguridad Activos:**
  1. Reglas Always-On: `.agents/rules/zh-mhep-zero-hallucination.md` y `.agents/rules/protocolo-decagonal-garantia-calidad.md`.
  2. Guardián 10 Fases: `scripts/quality_gatekeeper_10phases.py --audit` (10/10 PASS).
  3. Auditor Documental: `scripts/audit_docs_evidence.py --audit` (0 hallazgos).
  4. Escáner de Seguridad: `scripts/scan_skill_security.py --test` (5/5 PASS, SAFE 0.0/100).
- **Aislamiento de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS. Movilnet Core en puerto dedicado 8010.
- **Instrucción para Nueva Conversación (`+`):** Al abrir una nueva sesión, escribir simplemente:
  > *"¿Recuerdas dónde quedamos?"* o *"Continuemos con el proyecto Movilnet"*. El agente leerá este punto de control en 1 segundo con 0 tokens de desperdicio.
