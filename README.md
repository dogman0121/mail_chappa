#### docker-compose.yml
```
version: "3.8"

services:
  mail_chappa:
    container-name: mail_chappa
    build: <path_to_dockerfile>
    restart: always
    ports:
      - <internal_port>:<external_port>
    environment:
      - ADDRESS=0.0.0.0
      - PORT=25
      - REDIRECT_URL="https://example.com"
```
