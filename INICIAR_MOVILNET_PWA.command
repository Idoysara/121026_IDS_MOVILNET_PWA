#!/bin/bash
# ==============================================================================
# INICIAR_MOVILNET_PWA.command — Lanzador Soberano Movilnet PWA (121026_CORE)
# Proyecto: Movilnet PWA & Asistente 4GMAX — Telecomunicaciones Movilnet C.A.
# ==============================================================================

cd "$(dirname "$0")"

PORT=8010
URL="http://localhost:${PORT}/ui/pwa_stitch/simulador.html"

echo "========================================================================"
echo "📱 INICIANDO NÚCLEO MOVILNET Y PWA MOBILE-FIRST (PAQUETE SOBERANO)"
echo "========================================================================"

if lsof -i :${PORT} >/dev/null 2>&1; then
    echo "🟢 Servidor Movilnet Core ya está activo en el puerto ${PORT}."
    echo "🌐 Abriendo Simulador PWA Móvil: ${URL}"
    open "${URL}"
    exit 0
fi

echo "🌐 URL de Acceso: ${URL}"
echo "------------------------------------------------------------------------"
echo "🚀 Abriendo en tu navegador predeterminado..."

(sleep 1.5 && open "${URL}") &

if [ -f "venv/bin/python3" ]; then
    venv/bin/python3 api/service.py --port ${PORT}
else
    python3 api/service.py --port ${PORT}
fi
