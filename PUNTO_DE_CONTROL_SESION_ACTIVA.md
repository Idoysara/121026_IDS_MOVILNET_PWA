# PUNTO DE CONTROL — SESIÓN ACTIVA (MOVILNET ↔ PROTOCOLO DECAGONAL CERO ERRORES)
- **Fecha/Hora:** 2026-10-14 06:15 VET | **Capítulo Bitácora:** 177 (Generación del Respaldo Soberano Integral 141026_Movilnet_Core_PWA, Manifiesto Criptográfico SHA-256 de 945 Archivos, Autonomía de Entorno y Arquitectura N <-> 1)
- **Declaración Estratégica Ratificada:**
  > *"Respaldo Soberano 141026 Certificado: Se generó el respaldo completo, ordenado y lógicamente desacoplado en '/Users/ismael/Desktop/121026_CORE_MOVILNET/Movilnet_141026/141026_Movilnet_Core_PWA' con 945 archivos (41.48 MB) sellados bajo el hash maestro SHA-256 'dd3e1a6cd7b921acf712c5ac8c237f370716fcb4718e7b0a57cbc2cb8dfbcbde'. Se construyó el Manifiesto de Arquitectura y Componentes MANIFIESTO_ARQUITECTURA_Y_COMPONENTES_141026.md y se certificó la autonomía total de pruebas (15/15 PASS en el respaldo y 423/423 PASS en la suite global)."*
- **Estado de Calidad:** 423 / 423 tests aprobados (100% PASS, 0 fallos en 51.75s en 46 suites).
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
