#!/bin/bash
# ==============================================================================
# SUBIR_A_GITHUB.command — Sincronizador Soberano con GitHub (IDS_MOVILNET_PWA)
# Proyecto: Movilnet PWA & Asistente 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

cd "$(dirname "$0")"

clear
echo "========================================================================"
echo "🚀 RESPALDO EN GITHUB — MOVILNET PWA (IDS_MOVILNET_PWA)"
echo "========================================================================"
echo "📡 Destino: https://github.com/Idoysara/IDS_MOVILNET_PWA"
echo "🌿 Rama:    main"
echo "========================================================================"
echo ""

# 1. Asegurar que git tenga los cambios locales confirmados
if [ -n "$(git status --porcelain)" ]; then
    echo "📦 Preparando archivos locales pendientes..."
    git add .
    git commit -m "feat(pwa): actualizacion automatica de respaldo Movilnet PWA"
fi

# 2. Intentar push con credenciales almacenadas
echo "🔄 Intentando subir a GitHub con credenciales del sistema..."
git push -u origin main 2>/dev/null

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 ¡SUBIDA COMPLETADA CON ÉXITO A GITHUB!"
    echo "🔗 Repositorio actualizado: https://github.com/Idoysara/IDS_MOVILNET_PWA"
    echo ""
    read -p "Presiona ENTER para finalizar..."
    exit 0
fi

echo ""
echo "⚠️  GitHub requiere autenticación mediante Personal Access Token (PAT)."
echo "------------------------------------------------------------------------"
echo "Si aún no has creado el repositorio en GitHub:"
echo "👉 1. Entra a: https://github.com/new"
echo "👉 2. Escribe de nombre exacto: IDS_MOVILNET_PWA"
echo "👉 3. Déjalo vacío (no marques README, ni .gitignore) y haz clic en 'Create repository'."
echo ""
echo "Si tienes tu Token de GitHub (empieza por ghp_...):"
echo -n "Pega tu GitHub Token aquí (o presiona ENTER para omitir): "
read GITHUB_TOKEN

if [ -n "${GITHUB_TOKEN}" ]; then
    echo ""
    echo "🚀 Subiendo con token proporcionado..."
    git push "https://${GITHUB_TOKEN}@github.com/Idoysara/IDS_MOVILNET_PWA.git" main
    if [ $? -eq 0 ]; then
        echo ""
        echo "🎉 ¡SUBIDA COMPLETADA CON ÉXITO A GITHUB!"
        echo "🔗 Repositorio: https://github.com/Idoysara/IDS_MOVILNET_PWA"
    else
        echo ""
        echo "❌ No se pudo subir. Verifica que el repositorio exista en GitHub y el token sea válido."
    fi
else
    echo "Operación cancelada. Puedes ejecutar este lanzador cuando tengas tu token listo."
fi

echo ""
read -p "Presiona ENTER para cerrar esta ventana..."
