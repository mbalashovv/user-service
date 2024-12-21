# User Service

User service is a simple CRUD Web API that follows the principles of Clean Architecture

![Endpoints](https://imgur.com/9WGhQrs.png)

## Endpoints

#### GET /healthcheck

```bash
curl -X "GET" "http://localhost:8000/healthcheck"
```

```json
{"status": "ok"}
```

#### POST /users

```bash
curl -X "POST" \
  "http://127.0.0.1:8000/users" \
  -d '{
      "username": "Matthew",
      "password": "qwerty123"
  }'
```

```json
{
  "id": "420cea35-3f8e-47c9-8df7-be28039598ed",
  "username": "Matthew",
  "created_at": 1734812913
}
```

#### GET /users

```bash
curl -X "GET" "http://127.0.0.1:8000/users"
```

```json
{
  "users": [
    {
      "id": "520cea35-3f8e-47c9-8df7-be28039598ed",
      "username": "Taylor",
      "created_at": 1734809284
    },
    {
      "id": "420cea35-3f8e-47c9-8df7-be28039598ed",
      "username": "Matthew",
      "created_at": 1734812913
    }
  ]
}
```

## Dependencies

### Infrastructure

- [PostgreSQL](https://www.postgresql.org/docs/current/index.html) — Database
- [Docker](https://docs.docker.com/) — For deployment

### Grafana stack

- [Grafana](https://grafana.com/docs/grafana/latest/) — Web view for logs
- [Loki](https://grafana.com/docs/loki/latest/) — A platform to store and query logs
- [Vector.dev](https://vector.dev) — A tool to collect logs and send them to Loki

###  Key python libs

- [FastAPI](https://fastapi.tiangolo.com/) — Async web framework
- [AIOPG](https://aiopg.readthedocs.io/en/stable/) — PostgreSQL driver for interaction with database
- [Yoyo](https://ollycope.com/software/yoyo/latest/) — Database schema migration tool
- [Dependency-Injector](https://python-dependency-injector.ets-labs.org/) — A dependency injection framework for Python
