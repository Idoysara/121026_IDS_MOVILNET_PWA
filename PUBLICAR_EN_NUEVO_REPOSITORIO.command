#!/bin/bash
# ==============================================================================
# PUBLICAR_EN_NUEVO_REPOSITORIO.command — Publicador en Nuevo Repo Público GitHub
# Proyecto: Movilnet Core PWA & Asistente 4GMAX — Telecomunicaciones Movilnet C.A.
# Gobernanza: Universal Best Practices Engineering Rule (Pilar VII: Cero Terminal)
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

clear
echo "========================================================================"
echo "🚀 PUBLICADOR EN NUEVO REPOSITORIO PÚBLICO GITHUB"
echo "========================================================================"
echo "Este script permite publicar el proyecto en un repositorio público nuevo"
echo "para que un asociado o auditor externo lo pueda revisar de forma aislada."
echo "========================================================================"
echo ""

DEFAULT_REPO="261026_IDS_MOVILNET_CORE_PUBLIC"
echo -n "Nombre del nuevo repositorio en GitHub [Por defecto: $DEFAULT_REPO]: "
read REPO_NAME
if [ -z "$REPO_NAME" ]; then
    REPO_NAME="$DEFAULT_REPO"
fi

echo ""
echo "📌 URL destino: https://github.com/Idoysara/${REPO_NAME}.git"
echo ""
echo "⚠️  NOTA PREVIA:"
echo "Si aún no has creado el repositorio en GitHub, puedes crearlo en 10 segundos:"
echo "👉 https://github.com/new"
echo "   - Owner: Idoysara"
echo "   - Repository name: ${REPO_NAME}"
echo "   - Public: ✅ (Seleccionar Público)"
echo ""
read -p "Presiona ENTER cuando el repositorio esté creado en GitHub para subirlo..."

SRC_DIR="/Users/ismael/Desktop/121026_CORE_MOVILNET/Movilnet_141026/141026_Movilnet_Core_PWA"

echo "🔄 Configurando y subiendo código a https://github.com/Idoysara/${REPO_NAME}.git..."
git -C "$SRC_DIR" remote add review_public "https://github.com/Idoysara/${REPO_NAME}.git" 2>/dev/null || git -C "$SRC_DIR" remote set-url review_public "https://github.com/Idoysara/${REPO_NAME}.git"

git -C "$SRC_DIR" push -u review_public main

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================================================"
    echo "🎉 ¡PROYECTO PUBLICADO CON ÉXITO EN EL NUEVO REPOSITORIO!"
    echo "========================================================================"
    echo "🔗 Enlace de revisión pública para el asociado:"
    echo "👉 https://github.com/Idoysara/${REPO_NAME}"
    echo "========================================================================"
else
    echo ""
    echo "❌ Error al subir. Verifica que el repositorio exista en https://github.com/Idoysara/${REPO_NAME} y sea público."
fi

echo ""
read -p "Presiona ENTER para cerrar esta ventana..."
