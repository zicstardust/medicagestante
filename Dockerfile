FROM python:3.14.8-alpine

ENV PYTHONUNBUFFERED=1
ENV PATH="/home/medicagestante/.local/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml .
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
    chown -R medicagestante:medicagestante /home/medicagestante; \
    chown -R medicagestante:medicagestante /app; \
    \
    su-exec medicagestante pip3 install --no-cache-dir --user .

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "server.py"]
