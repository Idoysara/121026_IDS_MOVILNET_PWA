#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_MERCADEO_PDF.command — Lanzador 1-Clic PDF (16:9)
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Audiencia: Vicepresidencia de Mercadeo, Marca, Producto & Growth
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

PDF_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_DEPARTAMENTO_MERCADEO.pdf"

clear
echo "========================================================================"
echo "🎯 PRESENTACIÓN MERCADEO, MARCA Y MONETIZACIÓN (PDF 16:9)"
echo "========================================================================"
echo "🎪 Enfoque: MOVI Protagonista, Material POP, Tours Movilnet y 5 Fuentes"
echo "========================================================================"

if [ -f "$PDF_FILE" ]; then
    open "$PDF_FILE"
    echo "✅ Archivo abierto en Vista Previa / Navegador predeterminado."
    echo "📁 Archivo: $PDF_FILE"
else
    echo "❌ No se encontró el archivo $PDF_FILE"
fi

echo "========================================================================"
read -t 5 -p "Cerrando ventana en 5 segundos..." || true
echo ""
