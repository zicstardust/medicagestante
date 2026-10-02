# Medica Gestante

## Container
### Tags

| Tag | Description |
| :----: | :----: |
| [`latest`](https://github.com/zicstardust/medicagestante/blob/main/Dockerfile) | Default Tag |

### Registries
| Registry | Full image name | Description |
| :----: | :----: | :----: |
| [`ghcr.io`](https://github.com/zicstardust/medicagestante/pkgs/container/medicagestante) | `ghcr.io/zicstardust/medicagestante` | GitHub |


### Supported Architectures

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| amd64 | ✅ | latest |
| arm/v6 | ✅ | latest |
| arm/v7 | ✅ | latest |
| arm64 | ✅ | latest |
| ppc64le | ✅ | latest |
| riscv64 | ✅ | latest |
| s390x | ✅ | latest |


## Usage
### Compose
``` yml
services:
  medicagestante:
    container_name: medicagestante
    image: ghcr.io/zicstardust/medicagestante:latest
    restart: unless-stopped
    environment:
      TZ: America/Cuiaba
    ports:
      - 8080:8080/tcp #Web port
```

## Environment variables

| variables | Function | Default |
| :----: | --- | --- |
| `TZ` | Set Timezone | |
| `PUID` | Set UID with read permission on log files | 1000 |
| `PGID` | Set GID with read permission on log files | 1000 |


## Dev
### Install Dependencies
``` shell
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```


### Run App Debug mode:
``` shell
flask --app src/app.py --debug run
```

### Run App Production mode:
``` shell
python3 src/server.py
```