#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_INVERSIONISTA.command — Lanzador 1-Clic de la Presentación
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "========================================================================"
echo "📊 ABRIENDO PRESENTACIÓN EJECUTIVA PARA EL COMITÉ DE INVERSIÓN..."
echo "========================================================================"

# Abrir el slide deck interactivo en el navegador por defecto
open "$DIR/ui/presentacion_inversionista.html"

echo "✅ Presentación abierta en el navegador."
echo "🔗 También puedes ver el documento completo en: docs/PRESENTACION_EJECUTIVA_INVERSIONISTA_ECONOMISTA.md"
