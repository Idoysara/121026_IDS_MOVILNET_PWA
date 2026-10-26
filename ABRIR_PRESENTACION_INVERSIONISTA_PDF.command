#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_INVERSIONISTA_PDF.command — Lanzador 1-Clic PDF (16:9)
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Audiencia: Comité de Inversión y Evaluadores Financieros (Economistas)
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

PDF_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_INVERSIONISTA_ECONOMISTA.pdf"

clear
echo "========================================================================"
echo "📊 PRESENTACIÓN FINANCIERA INVERSIONISTA / ECONOMISTA (PDF 16:9)"
echo "========================================================================"
echo "🎯 Enfoque: Retorno de Capital, Payback 6.2m, CAC=$0 y Waterfall 75/25"
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
