#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_INVERSIONISTA_PPTX.command — Lanzador 1-Clic PowerPoint (.pptx)
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Audiencia: Comité de Inversión y Evaluadores Financieros (Economistas)
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

PPTX_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_INVERSIONISTA_ECONOMISTA.pptx"
PDF_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_INVERSIONISTA_ECONOMISTA.pdf"
HTML_FILE="$DIR/ui/presentacion_inversionista.html"

clear
echo "========================================================================"
echo "📊 PRESENTACIÓN POWERPOINT INVERSIONISTA / ECONOMISTA (.PPTX)"
echo "========================================================================"
echo "📁 Archivo: docs/PRESENTACION_EJECUTIVA_INVERSIONISTA_ECONOMISTA.pptx"
echo "========================================================================"

if open "$PPTX_FILE" 2>/dev/null; then
    echo "✅ Presentación abierta en tu suite ofimática nativa."
else
    echo "ℹ️  DIAGNÓSTICO: No se detectó PowerPoint ni Keynote instalado."
    echo "🚀 Activando visualizadores automáticos de alta fidelidad:"
    if [ -f "$PDF_FILE" ]; then
        echo "📄 1. Abriendo versión ejecutiva en PDF (16:9 HD)..."
        open "$PDF_FILE"
    fi
    if [ -f "$HTML_FILE" ]; then
        echo "🌐 2. Abriendo presentación interactiva en el navegador..."
        open "$HTML_FILE"
    fi
    echo "📁 3. Resaltando el archivo .pptx en Finder..."
    open -R "$PPTX_FILE"
fi

echo "========================================================================"
read -t 10 -p "Cerrando ventana en 10 segundos..." || true
echo ""
