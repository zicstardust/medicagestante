#!/bin/sh
set -e
PUID="${PUID:-1000}"
PGID="${PGID:-1000}"

if [ "$(id -g medicagestante)" != "${PGID}" ]; then
    groupmod -o -g "${PGID}" medicagestante
fi


if [ "$(id -u medicagestante)" != "${PUID}" ]; then
    usermod -o -u "${PUID}" medicagestante
fi

chown -R medicagestante:medicagestante /home/medicagestante /app

exec su-exec medicagestante "$@"