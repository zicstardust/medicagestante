FROM python:3.15.0rc2-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
COPY src/ .
COPY entrypoint.sh /entrypoint.sh

RUN apk update; \
    apk upgrade -a; \
    \
    chmod +x /entrypoint.sh; \
    \
    apk add --no-cache su-exec shadow; \
    \
    adduser -D -u 1000 -s /bin/nologin -h /home/medicagestante medicagestante; \
    su-exec medicagestante pip3 install --no-warn-script-location --user --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "server.py"]