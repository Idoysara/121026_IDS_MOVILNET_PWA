#!/bin/bash
# ==============================================================================
# ABRIR_CONVERSATORIO_MONITOR.command — Lanzador Soberano 1-Clic para el Dashboard N <-> 1
# Proyecto: Telecomunicaciones Movilnet C.A. — Modelo N Usuarios <-> 1 Asistente (+58 424 153 3712)
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

PORT=8010
TS=$(date +%s)
CLOUD_URL="https://one21026-ids-movilnet-pwa-bxmz.onrender.com/ui/monitor/conversatorio.html?v=${TS}"
LOCAL_URL="http://localhost:${PORT}/ui/monitor/conversatorio.html?v=${TS}"

clear
echo "========================================================================"
echo "🌲 TABLERO CONVERSATORIO EN VIVO: (N) USUARIOS <--> (1) ASISTENTE MOVI"
echo "📱 Línea Central Webhook: +58 424 153 3712 (00584241533712)"
echo "========================================================================"
echo "✨ Visualiza en dos columnas todas las conversaciones de los abonados"
echo "   interactuando en tiempo real con la IA y el Gateway de WhatsApp."
echo "------------------------------------------------------------------------"
echo "☁️  Abriendo versión en la Nube 24/7 (Render Cloud):"
echo "👉 ${CLOUD_URL}"
echo "========================================================================"

# Abrir la versión en la nube directamente
open "${CLOUD_URL}"

# Si el puerto local 8010 está activo, notificar que también está disponible
if lsof -i :${PORT} >/dev/null 2>&1; then
    echo "🟢 Servidor local detectado activo en :${PORT} (${LOCAL_URL})"
fi

echo "✅ Tablero conversatorio abierto en tu navegador."
sleep 1
