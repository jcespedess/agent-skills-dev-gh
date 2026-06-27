# Login API — Example

API REST de autenticación con usuario y contraseña usando **Python + FastAPI** y datos mock en archivo. Generada con el ciclo completo spec→plan→build→test→review→ship del equipo de desarrollo.

## Instalación

```bash
cd examples/login-api
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn main:app --reload
```

API disponible en `http://localhost:8000`. Documentación interactiva en `http://localhost:8000/docs`.

## Endpoints

| Método | Ruta | Descripción | Auth |
|--------|------|-------------|------|
| `GET` | `/health` | Estado de la API | No |
| `POST` | `/auth/login` | Login con usuario y contraseña | No |
| `GET` | `/users/me` | Datos del usuario autenticado | Sí |

### POST /auth/login

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

Respuesta exitosa (200):
```json
{"token": "mock-token-1", "username": "admin"}
```

Error de credenciales (401):
```json
{"detail": "Credenciales inválidas"}
```

### GET /users/me

```bash
curl http://localhost:8000/users/me \
  -H "Authorization: Bearer mock-token-1"
```

Respuesta exitosa (200):
```json
{"id": 1, "username": "admin", "name": "Administrador"}
```

Sin token (403):
```json
{"detail": "Token requerido"}
```

## Usuarios mock

Definidos en `data/users.json`:

| username | password | name |
|----------|----------|------|
| `admin` | `admin123` | Administrador |
| `demo` | `devpass2024` | Usuario Demo |

## Tests

```bash
pytest tests/ -v
```

Resultado esperado: **19 passed, 0 failed**.
