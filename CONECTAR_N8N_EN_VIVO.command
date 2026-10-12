#!/bin/bash
# ==============================================================================
# CONECTAR_N8N_EN_VIVO.command — Lanzador de Doble Clic para Conexión con n8n
# Proyecto: AI_Movilnet_300926 — Telecomunicaciones Movilnet C.A.
# ==============================================================================

cd "$(dirname "$0")"

# Determinar directorio raíz de la aplicación
if [ -d "AI_Movilnet_300926-main" ]; then
    cd "AI_Movilnet_300926-main"
fi

echo "========================================================================"
echo "🚀 INICIANDO CONEXIÓN EN VIVO: MOVILNET ↔ n8n LPGTEC"
echo "========================================================================"

if [ -f "venv/bin/python3" ]; then
    venv/bin/python3 scripts/connect_n8n_live.py
else
    python3 scripts/connect_n8n_live.py
fi

echo ""
read -p "Presiona ENTER para cerrar esta ventana..."
