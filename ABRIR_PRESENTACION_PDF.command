#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_PDF.command — Lanzador 1-Clic de la Presentación en PDF HD (16:9)
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

PDF_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_MOVILNET_IA.pdf"

clear
echo "========================================================================"
echo "📄 ABRIENDO PRESENTACIÓN EJECUTIVA EN FORMATO PDF HD (16:9 WIDESCREEN)"
echo "========================================================================"
echo "📊 Formato: PDF de Alta Resolución (10 Láminas / Diapositivas)"
echo "🎯 Audiencia: Comité de Inversión, Economistas y Dpto. de Mercadeo"
echo "========================================================================"

if [ -f "$PDF_FILE" ]; then
    open "$PDF_FILE"
    echo "✅ Archivo abierto con éxito en Vista Previa / Navegador predeterminado."
    echo "📁 Ruta: $PDF_FILE"
else
    echo "❌ Error: No se encontró el archivo $PDF_FILE"
fi

echo "========================================================================"
read -t 5 -p "Cerrando ventana..." || true
echo ""
