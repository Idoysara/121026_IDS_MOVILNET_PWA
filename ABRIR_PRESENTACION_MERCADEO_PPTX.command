#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_MERCADEO_PPTX.command — Lanzador 1-Clic PowerPoint (.pptx)
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Audiencia: Vicepresidencia de Mercadeo, Marca, Producto & Growth
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

PPTX_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_DEPARTAMENTO_MERCADEO.pptx"
PDF_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_DEPARTAMENTO_MERCADEO.pdf"
HTML_FILE="$DIR/ui/presentacion_mercadeo.html"

clear
echo "========================================================================"
echo "🎯 PRESENTACIÓN POWERPOINT MERCADEO & MONETIZACIÓN (.PPTX)"
echo "========================================================================"
echo "📁 Archivo: docs/PRESENTACION_EJECUTIVA_DEPARTAMENTO_MERCADEO.pptx"
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
