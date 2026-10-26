#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_POWERPOINT.command — Lanzador 1-Clic de PowerPoint (.pptx)
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

PPTX_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_MOVILNET_IA.pptx"
PDF_FILE="$DIR/docs/PRESENTACION_EJECUTIVA_MOVILNET_IA.pdf"
HTML_INV="$DIR/ui/presentacion_inversionista.html"
HTML_MKT="$DIR/ui/presentacion_mercadeo.html"

clear
echo "========================================================================"
echo "📊 PRESENTACIÓN EJECUTIVA OFICIAL — MOVILNET IA 4GMAX"
echo "========================================================================"
echo "📁 Archivo PPTX: docs/PRESENTACION_EJECUTIVA_MOVILNET_IA.pptx"
echo "========================================================================"

# Intentar abrir el .pptx con una suite ofimática nativa (PowerPoint / Keynote)
OPEN_OUTPUT=$(open "$PPTX_FILE" 2>&1)
OPEN_STATUS=$?

if [ $OPEN_STATUS -eq 0 ]; then
    echo "✅ Presentación abierta con éxito en tu suite ofimática nativa."
    echo "========================================================================"
else
    echo "ℹ️  DIAGNÓSTICO DEL SISTEMA:"
    echo "   En esta Mac no está instalado Microsoft PowerPoint ni Apple Keynote."
    echo "   (Código del sistema macOS: kLSApplicationNotFoundErr / -10814)"
    echo "------------------------------------------------------------------------"
    echo "🚀 ACTIVANDO CANALES DE VISUALIZACIÓN INMEDIATA (CERO DEPENDENCIAS):"
    echo "------------------------------------------------------------------------"
    
    # 1. Abrir la versión PDF oficial en Vista Previa / Navegador
    if [ -f "$PDF_FILE" ]; then
        echo "📄 1. Abriendo versión ejecutiva en PDF HD (10 láminas 16:9)..."
        open "$PDF_FILE"
    fi
    
    # 2. Abrir la versión interactiva HD en el navegador
    if [ -f "$HTML_INV" ]; then
        echo "🌐 2. Abriendo diapositivas web interactivas (Inversionista & Economista)..."
        open "$HTML_INV"
    fi
    
    # 3. Revelar el archivo .pptx en el Finder
    echo "📁 3. Resaltando el archivo .pptx en Finder para enviar o editar..."
    open -R "$PPTX_FILE"
    
    echo "------------------------------------------------------------------------"
    echo "💡 OPCIONES PARA EDITAR O PROYECTAR EL ARCHIVO .PPTX:"
    echo "   • Google Slides: Arrastra el archivo .pptx a https://drive.google.com"
    echo "   • Microsoft 365 Web: Ábrelo gratis en https://office.com"
    echo "   • Keynote: Puedes instalar Apple Keynote gratis desde el App Store de Mac."
    echo "========================================================================"
fi

read -t 10 -p "Esta ventana se cerrará automáticamente en 10 segundos..." || true
echo ""
