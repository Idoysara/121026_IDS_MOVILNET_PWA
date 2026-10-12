#!/bin/bash
# ==============================================================================
# INICIAR_MOVILNET_PWA.command — Lanzador Soberano Movilnet PWA & Control 1-Clic
# Proyecto: Movilnet PWA & Asistente 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

cd "$(dirname "$0")"

PORT=8010
URL="http://localhost:${PORT}/ui/pwa_stitch/simulador.html"
RENDER_URL="https://movilnet-core.onrender.com"

clear
echo "========================================================================"
echo "📱 MOVILNET CORE 4GMAX — CENTRO DE CONTROL PWA & DESPLIEGUE"
echo "========================================================================"

# 1. Asegurar que el servidor local esté activo
if ! lsof -i :${PORT} >/dev/null 2>&1; then
    echo "⚙️  Iniciando Servidor Movilnet Core en puerto ${PORT}..."
    if [ -f "venv/bin/python3" ]; then
        nohup venv/bin/python3 api/service.py --port ${PORT} >/dev/null 2>&1 &
    else
        nohup python3 api/service.py --port ${PORT} >/dev/null 2>&1 &
    fi
    sleep 1.5
fi

# 2. Verificar estado del puerto
if lsof -i :${PORT} >/dev/null 2>&1; then
    STATUS_LOCAL="🟢 ACTIVO (0.8ms SQLite WAL)"
else
    STATUS_LOCAL="🔴 ERROR AL INICIAR"
fi

echo "🟢 Servidor Local :${PORT}  ➔ ${STATUS_LOCAL}"
echo "🌐 URL Local Simulador    ➔ ${URL}"
echo "☁️  URL Nube Render 24/7   ➔ ${RENDER_URL}/ui/pwa_stitch/index.html"
echo "========================================================================"
echo ""
echo "Selecciona una opción (se abrirá la PWA automáticamente en 5s):"
echo "  [1] 📱 Abrir Simulador PWA Móvil en el Navegador (Por defecto)"
echo "  [2] 🚀 Actualizar Servidor en la Nube Render (1 Clic)"
echo "  [3] 🔄 Reiniciar Servidor Local (Recargar últimos cambios)"
echo "  [4] 🚪 Salir"
echo ""

read -t 5 -p "Opción [1-4] (Enter para abrir PWA): " OPCION || true
echo ""

case "$OPCION" in
    2)
        echo "========================================================================"
        echo "🚀 EJECUTANDO DESPLIEGUE AUTOMÁTICO EN LA NUBE RENDER..."
        echo "========================================================================"
        
        # Sincronizar cambios a GitHub si hay alguno
        if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
            echo "📦 Sincronizando repositorio con GitHub..."
            git add .
            git commit -m "feat(ops): actualizacion de despliegue previa a Render"
            git push origin main
            echo "✅ GitHub actualizado."
        fi
        
        if [ -f "venv/bin/python3" ]; then
            venv/bin/python3 scripts/trigger_render_deploy.py --trigger
        else
            python3 scripts/trigger_render_deploy.py --trigger
        fi
        
        echo ""
        read -p "Presiona ENTER para continuar y abrir el Simulador PWA..."
        open "${URL}"
        ;;
    3)
        echo "🔄 Reiniciando Servidor Movilnet Core en puerto ${PORT}..."
        PIDS=$(lsof -t -i :${PORT} 2>/dev/null)
        if [ -n "$PIDS" ]; then
            kill -9 $PIDS 2>/dev/null
        fi
        sleep 1
        if [ -f "venv/bin/python3" ]; then
            nohup venv/bin/python3 api/service.py --port ${PORT} >/dev/null 2>&1 &
        else
            nohup python3 api/service.py --port ${PORT} >/dev/null 2>&1 &
        fi
        sleep 1.5
        echo "✅ Servidor reiniciado con éxito."
        open "${URL}"
        ;;
    4)
        echo "👋 ¡Hasta luego!"
        exit 0
        ;;
    *)
        echo "🌐 Abriendo Simulador PWA Móvil..."
        open "${URL}"
        ;;
esac

echo ""
echo "========================================================================"
echo "💡 TIP: También puedes pulsar el botón '🚀 Actualizar Render (1 Clic)'"
echo "   directamente en la barra superior del Simulador en tu navegador."
echo "========================================================================"
sleep 2
