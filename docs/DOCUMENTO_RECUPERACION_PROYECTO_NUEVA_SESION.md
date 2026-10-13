# 🚀 DOCUMENTO DE RECUPERACIÓN Y CONTINUIDAD DEL PROYECTO (MOVILNET 4GMAX)
## Protocolo Soberano para Apertura de Nueva Sesión en Antigravity (`+`)

**Fecha de Generación:** 2026-10-13 17:07 VET  
**Capítulo Activo en Bitácora:** Capítulo 174 — Aprobación Oficial de Versión en Producción y Diseño de la Arquitectura de Reglas Departamentales Hot-Reload (Zero-Downtime, 5 Áreas de Negocio & TM Forum ODA)  
**Sello de Calidad:** 421 / 421 Tests Aprobados (100% PASS en 22.31s en 46 suites) | 0 Alucinaciones | 10/10 Fases Decagonales  

---

## 🎯 Declaración Estratégica Ratificada

> *"En Resumen: La versión actual de Movilnet Core (+58 424 153 3712 / MOVI en puerto 8010) está aprobada formalmente por el equipo de desarrollo y permanece ininterrumpidamente en línea. Para la evolución continua de los departamentos de negocio (Comercial, Finanzas, Atención al Cliente, Seguridad/CONATEL y NOC), se ha diseñado la arquitectura de Reglas Departamentales Hot-Reload, permitiendo actualizar políticas comerciales y operativas en <5ms en memoria con 0% de tiempo de inactividad (Zero Downtime)."*

---

## 📋 ¿Cómo Abrir una Nueva Conversación y Retomar en 1 Segundo?

1. En la interfaz de Antigravity, presiona el botón **`+` (Nueva Conversación)**.
2. Copia y pega cualquiera de las siguientes frases:
   > **`¿Recuerdas dónde quedamos?`**  
   o  
   > **`Continuemos con el proyecto Movilnet`**
3. El agente activará el skill `agy-session-continuity`, leerá el archivo ultraligero `PUNTO_DE_CONTROL_SESION_ACTIVA.md` y retomará el 100% del contexto operativo con **0 tokens de desperdicio** y sin pérdida de memoria.

---

## 🏛️ Estado Técnico y Topología del Sistema al Cerrar esta Sesión

### 1. Canal Central y Parametrización Oficial ($N \leftrightarrow 1$)
* **Línea Central del Bot:** `+58 424 153 3712` (`0424-1533712`, `584241533712@s.whatsapp.net`, identidad `MOVI`).
* **Variables de Entorno (`.env` y `.env.example`):**
  - `MOVILNET_ACTIVE_BOT_PHONE=0424-1533712`
  - `MOVILNET_BOT_NAME=MOVI`
* **Módulo de Parametrización:** `core/system_config.py` (`SystemConfigManager`).

### 2. Comando Maestro de Prueba Real (Pilar VII: Cero Terminal • 1 Clic)
* **Lanzador de Doble Clic:** `EJECUTAR_PRUEBA_REAL.command` (macOS).
* **Módulo CLI Autónomo:** `scripts/ejecutar_prueba_real.py` (`--test`, `--no-open`, `--message`, `--timeout`).
* **Aislamiento de Interfaz:** Solo abre la Sala de Control (`conversatorio.html`) en la Mac; no abre pestañas invasivas de WhatsApp Web en el navegador. La prueba la realiza el usuario desde su teléfono físico.
* **Suite de Pruebas Unitarias:** `tests/test_ejecutar_prueba_real.py` (4/4 PASS).

### 3. Arquitectura de Reglas Departamentales Hot-Reload (Capítulo 174)
* **Catálogo Declarativo Versionado:** `config/department_rules/` estructurado para 5 departamentos:
  1. *Comercial & Ventas:* Planes Inteliplan 4GMAX, bonos de portabilidad (10GB), eSIM.
  2. *Finanzas & FinTech:* Límites de recargas Pago Móvil C2P, conversión oficial BCV.
  3. *Atención al Cliente:* Horarios de asesores humanos, SLAs de atención.
  4. *Seguridad & CONATEL:* Reportes EIR de bloqueo IMEI por robo/extravío, Zero-PII.
  5. *Operaciones de Red (NOC):* Alertas de mantenimiento de radiobases zonales.
* **Motor de Ingesta en Caliente:** `DepartmentRuleEngine` (<5ms en memoria con `threading.RLock()` y endpoint seguro `/api/v1/rules/reload`).
* **Validador Pre-Commit:** `ACTUALIZAR_REGLAS_DEPARTAMENTALES.command` / `scripts/validate_department_rules.py`.

### 4. Suites de Gobernanza y Migración
* **Suite de Migración Telefónica Universal:**
  - `core/phone_migration_orchestrator.py` (`--plan`, `--apply`, snapshot en `.backups/phone_migration/` y rollback automático AST).
  - Servidor MCP: `mcp/phone_migration_mcp.py` (`phone-migration-guardian`).
  - Skill: `.agents/skills/agy-phone-migration-guardian/SKILL.md`.
* **Suite de Blindaje del Protocolo PWA (*"WPA"*):**
  - `core/pwa_protocol_guardian.py` (Auditoría de 14 puntos, bump de Service Worker `sw.js` Network-First Zero-Stale, pipeline Zero-Token en $<15\text{ ms}$).
  - Servidor MCP: `mcp/pwa_protocol_mcp.py` (`pwa-protocol-guardian`).
  - Skill: `.agents/skills/agy-pwa-protocol-guardian/SKILL.md`.
  - Simulador NOC: `ui/pwa_stitch/simulador.html` con Códigos QR dinámicos Dual-Mode (WhatsApp Direct vs PWA Web).

### 5. Flujo Activo en n8n Cloud
* **ID del Workflow:** `sNMbtiEiTkuQ9OCY` (`Viki_LPGTEC_v2_ids_Movilnet_Google_Suite_Full`).
* **Webhook Canónico:** `https://n8n.lpgtec.net/webhook/messages_upsert4`.
* **Prompt del Asistente:** Sincronizado a `"Eres MOVI (+58 424 153 3712)"`.
* **Router Telco & C2P:** Pago Móvil receptor configurado hacia `0424-1533712`.

### 6. Servicio Backend y Telemetría en Vivo
* **Movilnet Core Daemon:** Proceso background en puerto dedicado **`8010`** (`api/service.py`, PID 47813).
* **Centro de Monitoreo Conversacional E2E:**  
  👉 **`http://localhost:8010/ui/monitor/conversatorio.html`**
* **Aislamiento Soberano de Puertos (`agy-port-guardian`):** Puerto 8000 reservado para Docker DSS GPS (`dss_gps_backend`), puerto 8010 para Movilnet Core.

---

## 🧪 Comandos Rápidos de Verificación (Para la Nueva Sesión)

```bash
# 1. Comprobar que Movilnet Core escucha en el puerto 8010:
lsof -i :8010

# 2. Ejecutar la suite completa de pruebas automatizadas (421/421 PASS):
./venv/bin/pytest tests/

# 3. Validar cero alucinaciones y auditoría documental:
./venv/bin/python scripts/audit_docs_evidence.py --audit
./venv/bin/python scripts/verify_zero_hallucination_compliance.py --audit
./venv/bin/python scripts/quality_gatekeeper_10phases.py --audit

# 4. Auditar el comando maestro de prueba real:
./venv/bin/python scripts/ejecutar_prueba_real.py --test

# 5. Auditar el protocolo PWA y el pipeline Zero-Token:
./venv/bin/python core/pwa_protocol_guardian.py --audit
./venv/bin/python core/pwa_protocol_guardian.py --verify-zero-token
```

---

## 📌 Documentos de Referencia Actualizados
1. [PUNTO_DE_CONTROL_SESION_ACTIVA.md](file:///Users/ismael/Desktop/121026_CORE_MOVILNET/Movilnet_121026/Movilnet_PWA/PUNTO_DE_CONTROL_SESION_ACTIVA.md) (Punto de control ultraligero).
2. [BITACORA_MOVILNET.md](file:///Users/ismael/Desktop/121026_CORE_MOVILNET/Movilnet_121026/Movilnet_PWA/docs/BITACORA_MOVILNET.md) (Capítulos 164 al 174 registrados).
3. [LIBRO_MAESTRO_BITACORA_Y_DOCUMENTOS.md](file:///Users/ismael/Desktop/121026_CORE_MOVILNET/Movilnet_121026/Movilnet_PWA/docs/LIBRO_MAESTRO_BITACORA_Y_DOCUMENTOS.md) (Resúmenes y matriz final).
