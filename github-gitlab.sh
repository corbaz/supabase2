#!/bin/bash

# Obtener la fecha y hora actual en formato deseado
now=$(date +'%d de %B de %Y - %H:%M:%S')

# Mensaje por defecto si no se proporciona uno
default_commit_message="Commit realizado el $now"

# Obtener el mensaje y la rama de los argumentos, si se proporcionan
while getopts "m:b:" opt; do
  case ${opt} in
    m ) commit_message=$OPTARG;;
    b ) branch=$OPTARG;;
    \? ) echo "Opción inválida: -$OPTARG" 1>&2; exit 1;;
    : ) echo "La opción -$OPTARG requiere un argumento" 1>&2; exit 1;;
  esac
done

# Si no se proporcionó un mensaje, usar el mensaje por defecto
if [ -z "$commit_message" ]; then
  commit_message="$default_commit_message"
fi

# Ejecutar los comandos de git
git add .
git commit -m "$commit_message"
git push github $branch
git push gitlab $branch
# git push heroku $branch
# heroku open
