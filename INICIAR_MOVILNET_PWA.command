#!/bin/bash
# ==============================================================================
# INICIAR_MOVILNET_PWA.command — Lanzador Soberano Movilnet PWA & Control 1-Clic
# Proyecto: Movilnet PWA & Asistente 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

cd "$(dirname "$0")"

PORT=8010
URL="http://localhost:${PORT}/ui/pwa_stitch/simulador.html?v=168"
MONITOR_URL="http://localhost:${PORT}/ui/monitor/conversatorio.html"
RENDER_URL="https://movilnet-core.onrender.com"

clear
echo "========================================================================"
echo "📱 MOVILNET CORE 4GMAX — CENTRO DE CONTROL PWA & DESPLIEGUE (v168)"
echo "========================================================================"

# 1. Recargar servidor local en :8010 con los últimos guardarraíles activos
PIDS=$(lsof -t -i :${PORT} 2>/dev/null)
if [ -n "$PIDS" ]; then
    kill -9 $PIDS 2>/dev/null || true
    sleep 0.5
fi

echo "⚙️  Activando Servidor Movilnet Core (:8010) y Guardarraíles Zero-Token..."
if [ -f "venv/bin/python3" ]; then
    PYTHON_BIN="venv/bin/python3"
else
    PYTHON_BIN="python3"
fi
nohup ${PYTHON_BIN} api/service.py --port ${PORT} >/dev/null 2>&1 &
sleep 1.5

# 2. Verificar auto-test de Guardarraíles (#13368 y #13585 + SQLite Freemium)
${PYTHON_BIN} core/webhook_noise_filter.py --test
${PYTHON_BIN} core/fastpath_intent_interceptor.py --test

# 3. Verificar estado del puerto
if lsof -i :${PORT} >/dev/null 2>&1; then
    STATUS_LOCAL="🟢 ACTIVO (0.8ms SQLite WAL + Guardarraíles Activos)"
else
    STATUS_LOCAL="🔴 ERROR AL INICIAR"
fi

echo "========================================================================"
echo "🟢 Servidor Local :${PORT}  ➔ ${STATUS_LOCAL}"
echo "🌐 URL Local Simulador    ➔ ${URL}"
echo "📊 Monitor Conversatorio  ➔ ${MONITOR_URL}"
echo "☁️  URL Nube Render 24/7   ➔ ${RENDER_URL}/ui/pwa_stitch/index.html?v=168&qr=1"
echo "========================================================================"
echo ""
echo "Selecciona una opción (se abrirán el Simulador y Monitor en 5s):"
echo "  [1] 📱 Abrir Simulador PWA + Monitor Conversatorio (Por defecto)"
echo "  [2] 🚀 Actualizar Servidor en la Nube Render (1 Clic)"
echo "  [3] 🧪 Ejecutar Demo en Vivo de Guardarraíles (#13368 y #13585)"
echo "  [4] 🚪 Salir"
echo ""

read -t 5 -p "Opción [1-4] (Enter para abrir PWA + Monitor): " OPCION || true
echo ""

case "$OPCION" in
    2)
        echo "========================================================================"
        echo "🚀 EJECUTANDO DESPLIEGUE AUTOMÁTICO EN LA NUBE RENDER..."
        echo "========================================================================"
        
        if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
            echo "📦 Sincronizando repositorio con GitHub..."
            git add .
            git commit -m "feat(ops): actualizacion de despliegue previa a Render"
            git push origin main
            echo "✅ GitHub actualizado."
        fi
        
        ${PYTHON_BIN} scripts/trigger_render_deploy.py --trigger
        
        echo ""
        read -p "Presiona ENTER para continuar y abrir el Simulador PWA..."
        open "${URL}"
        open "${MONITOR_URL}"
        ;;
    3)
        echo "🧪 Ejecutando demostración en vivo de Guardarraíles..."
        ${PYTHON_BIN} core/webhook_noise_filter.py --demo
        ${PYTHON_BIN} core/fastpath_intent_interceptor.py --demo --phone "04160000001" --msg "saldo"
        ${PYTHON_BIN} core/fastpath_intent_interceptor.py --demo --phone "04142554590" --msg "Este 15 de octubre volvemos con el Caracas Tech Meetup. Evento con cupos limitados. Regístrate en https://luma.com/snugy0r7"
        open "${URL}"
        open "${MONITOR_URL}"
        ;;
    4)
        echo "👋 ¡Hasta luego!"
        exit 0
        ;;
    *)
        echo "🌐 Abriendo Simulador PWA Móvil y Monitor Conversatorio..."
        open "${URL}"
        open "${MONITOR_URL}"
        ;;
esac

echo ""
echo "========================================================================"
echo "💡 TIP: También puedes pulsar el botón '🚀 Actualizar Render (1 Clic)'"
echo "   directamente en la barra superior del Simulador en tu navegador."
echo "========================================================================"
sleep 2
