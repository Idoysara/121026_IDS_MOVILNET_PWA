#!/bin/bash
# ==============================================================================
# ABRIR_PRESENTACION_MERCADEO.command — Lanzador 1-Clic Presentación Mercadeo
# Proyecto: Asistente MOVI 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "========================================================================"
echo "🎯 ABRIENDO PRESENTACIÓN ESTRATÉGICA PARA EL EQUIPO DE MERCADEO..."
echo "========================================================================"

# Abrir el slide deck interactivo de mercadeo en el navegador por defecto
open "$DIR/ui/presentacion_mercadeo.html"

echo "✅ Presentación abierta en el navegador."
echo "🔗 Documento maestro: docs/PRESENTACION_EJECUTIVA_DEPARTAMENTO_MERCADEO.md"
