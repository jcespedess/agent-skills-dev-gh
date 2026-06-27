# Spec: Login API — Example

## Objetivo

API REST de autenticación con usuario y contraseña para validar el ciclo completo
spec→plan→build→test→review→ship en el stack Python + FastAPI del equipo de desarrollo.

Usuarios: desarrolladores del equipo verificando que el proceso funciona end-to-end.

Criterios de éxito:
- POST /auth/login con credenciales válidas retorna token simple
- POST /auth/login con credenciales inválidas retorna 401
- GET /users/me con token válido retorna datos del usuario
- GET /users/me sin token retorna 403
- Todos los tests pasan con pytest

## Tech Stack

- Python 3.11+
- FastAPI 0.110+
- Uvicorn (dev server)
- pytest + httpx (tests)

## Comandos

Dev:   uvicorn main:app --reload
Test:  pytest tests/ -v
Lint:  ruff check .

## Estructura del proyecto

```
examples/login-api/
├── main.py              → app FastAPI + routers
├── routers/
│   └── auth.py          → POST /auth/login, GET /users/me
├── data/
│   └── users.json       → usuarios mock (id, username, password, name)
├── models/
│   └── user.py          → esquemas Pydantic
├── tests/
│   └── test_auth.py     → casos de prueba con httpx
├── requirements.txt
└── README.md
```

## Estilo de código

```python
# Convención: snake_case, type hints obligatorios, respuestas tipadas con Pydantic
@router.post("/auth/login", response_model=LoginResponse)
async def login(credentials: LoginRequest) -> LoginResponse:
    user = find_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return LoginResponse(token=f"mock-token-{user['id']}", username=user['username'])
```

## Estrategia de testing

Framework: pytest + httpx (AsyncClient)
Ubicación: examples/login-api/tests/
Cobertura mínima: happy path + caso de error por endpoint
Niveles: integración (cliente HTTP contra app en memoria)

## Boundaries

- Always: type hints en todas las funciones, validar inputs con Pydantic
- Ask first: agregar dependencias nuevas, cambiar estructura de carpetas
- Never: hardcodear credenciales fuera de data/users.json, lógica real de auth

## Criterios de salida

- [ ] POST /auth/login retorna 200 + token con credenciales válidas
- [ ] POST /auth/login retorna 401 con credenciales inválidas
- [ ] GET /users/me retorna 200 + datos de usuario con token válido
- [ ] GET /users/me sin token retorna 403
- [ ] pytest pasa sin errores
- [ ] Código revisado y commiteado en examples/login-api/
