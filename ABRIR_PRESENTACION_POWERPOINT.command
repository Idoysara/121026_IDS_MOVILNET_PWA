#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_POWERPOINT.command — Lanzador 1-Clic de PowerPoint (.pptx)
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "========================================================================"
echo "📊 ABRIENDO PRESENTACIÓN OFICIAL POWERPOINT (PPTX)..."
echo "========================================================================"

# Abrir el archivo .pptx con la aplicación predeterminada (PowerPoint / Keynote)
open "$DIR/docs/PRESENTACION_EJECUTIVA_MOVILNET_IA.pptx"

echo "✅ Archivo abierto: docs/PRESENTACION_EJECUTIVA_MOVILNET_IA.pptx"
echo "========================================================================"
