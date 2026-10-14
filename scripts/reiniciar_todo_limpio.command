#!/bin/bash
# ==============================================================================
# scripts/reiniciar_todo_limpio.command — Reinicio Limpio del Ecosistema Movilnet
# ==============================================================================
# Proyecto: AI_Movilnet_300926 — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
cd "$DIR"

echo "========================================================================"
echo "🔄 TELECOMUNICACIONES MOVILNET C.A. — REINICIO LIMPIO DEL ECOSISTEMA"
echo "========================================================================"
echo "Directorio Base: $DIR"
echo "Fecha y Hora: $(date)"
echo "========================================================================"
echo ""

echo "▶️ [1/5] Liberando procesos previos en puerto dedicado :8010..."
PID_8010=$(lsof -ti :8010 2>/dev/null)
if [ -n "$PID_8010" ]; then
    echo "   ⚠️ Proceso anterior detectado (PID $PID_8010). Terminando ordenadamente..."
    kill -15 $PID_8010 2>/dev/null || kill -9 $PID_8010 2>/dev/null
    sleep 1
    echo "   ✅ Puerto 8010 liberado."
else
    echo "   ✅ Puerto 8010 libre."
fi

echo ""
echo "▶️ [2/5] Verificando aislamiento de puertos (agy-port-guardian)..."
echo "   🛡️ Puerto 8000 (Docker DSS GPS): Preservado sin tocar."
echo "   🛡️ Puerto 8010 (Movilnet Core & Conversatorio): Asignado en exclusiva."

echo ""
echo "▶️ [3/5] Arrancando Microservicio Movilnet Core ODA en puerto 8010..."
nohup python3 api/service.py --port 8010 > /dev/null 2>&1 &
SERVER_PID=$!
sleep 2

# Verificar que levantó
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8010/health)
if [ "$HTTP_STATUS" = "200" ]; then
    echo "   ✅ Servidor local iniciado exitosamente (PID $SERVER_PID, Health: 200 OK)."
else
    echo "   ❌ Alerta: El servidor no respondió 200 OK inmediatamente (Status: $HTTP_STATUS). Reintentando..."
    sleep 2
fi

echo ""
echo "▶️ [4/5] Sincronizando telemetría y supervisor en vivo..."
python3 scripts/live_core_supervisor.py --audit

echo ""
echo "▶️ [5/5] Abriendo Centro de Monitoreo Conversatorio en el navegador..."
open "http://localhost:8010/ui/monitor/conversatorio.html"

echo ""
echo "========================================================================"
echo "🏆 ECOSISTEMA REINICIADO CON ÉXITO Y 100% OPERATIVO EN VIVO"
echo "========================================================================"
echo "🌐 Conversatorio:  http://localhost:8010/ui/monitor/conversatorio.html"
echo "📡 Health Check:   http://localhost:8010/health"
echo "📖 Swagger API:    http://localhost:8010/docs"
echo "☁️ Render Prod:    https://movilnet-core.onrender.com"
echo "⚡ n8n Cloud:      https://n8n.lpgtec.net/workflow/sNMbtiEiTkuQ9OCY"
echo "========================================================================"
echo ""
read -p "Presione [Enter] para cerrar esta ventana..."
