# Implementation Plan: Login API — Example (FastAPI)

## Overview

API REST de autenticación con usuario y contraseña usando Python + FastAPI y datos mock en archivo.
Objetivo: validar el ciclo completo spec→plan→build→test→review→ship del equipo de desarrollo.
Ubicación: `examples/login-api/`.

## Architecture Decisions

- **Sin JWT:** token mock simple (`mock-token-{id}`) — suficiente para validar el flujo de auth
- **Mock en archivo:** `data/users.json` — evita dependencia de BD, fácil de editar
- **Token en header:** `Authorization: Bearer <token>` — convención REST estándar
- **Tokens activos en memoria:** dict `active_tokens` en runtime — no persiste entre reinicios (aceptable para ejemplo)

---

## Phase 1: Fundación

### Task 1: Setup del proyecto

**Description:** Crear la estructura de carpetas y archivos base. La app debe arrancar con `uvicorn` sin errores aunque no tenga endpoints todavía.

**Acceptance criteria:**
- [ ] Existe `examples/login-api/` con la estructura definida en el spec
- [ ] `requirements.txt` incluye fastapi, uvicorn, httpx, pytest, pytest-asyncio
- [ ] `main.py` crea la app FastAPI y retorna 200 en `GET /health`
- [ ] `uvicorn main:app --reload` arranca sin errores desde `examples/login-api/`

**Verification:**
- [ ] `uvicorn main:app` arranca sin ImportError ni SyntaxError
- [ ] `curl http://localhost:8000/health` retorna `{"status": "ok"}`

**Dependencies:** None

**Files:**
- `examples/login-api/main.py`
- `examples/login-api/requirements.txt`
- `examples/login-api/routers/__init__.py`
- `examples/login-api/models/__init__.py`
- `examples/login-api/data/.gitkeep`
- `examples/login-api/tests/__init__.py`

**Scope:** S

---

### Task 2: Mock data y modelos Pydantic

**Description:** Crear el archivo de usuarios mock y los schemas Pydantic para request/response. Es la base que todos los endpoints necesitan.

**Acceptance criteria:**
- [ ] `data/users.json` tiene al menos 2 usuarios con campos: `id`, `username`, `password`, `name`
- [ ] `models/user.py` define `LoginRequest`, `LoginResponse`, `UserMe` con type hints
- [ ] Función `load_users()` lee y retorna los usuarios del archivo JSON
- [ ] Función `find_user(username, password)` busca usuario por credenciales

**Verification:**
- [ ] `python -c "from models.user import LoginRequest; print('OK')"` sin errores
- [ ] `python -c "from data_loader import load_users; print(load_users())"` retorna lista

**Dependencies:** Task 1

**Files:**
- `examples/login-api/data/users.json`
- `examples/login-api/models/user.py`
- `examples/login-api/data_loader.py`

**Scope:** S

---

### Checkpoint: Fundación

- [ ] App arranca con uvicorn sin errores
- [ ] `GET /health` retorna 200
- [ ] Modelos importan sin errores
- [ ] Revisar con el usuario antes de continuar

---

## Phase 2: Endpoints

### Task 3: POST /auth/login

**Description:** Endpoint de login que valida credenciales contra el archivo mock y retorna un token simple. Incluye caso de error 401.

**Acceptance criteria:**
- [ ] `POST /auth/login` con credenciales válidas retorna `{"token": "mock-token-{id}", "username": "..."}`  con status 200
- [ ] `POST /auth/login` con credenciales inválidas retorna 401 con mensaje de error
- [ ] El token generado se almacena en memoria para validaciones posteriores

**Verification:**
- [ ] `curl -X POST /auth/login -d '{"username":"admin","password":"1234"}'` → 200 + token
- [ ] `curl -X POST /auth/login -d '{"username":"admin","password":"wrong"}'` → 401

**Dependencies:** Task 2

**Files:**
- `examples/login-api/routers/auth.py`
- `examples/login-api/main.py` (montar router)

**Scope:** S

---

### Task 4: GET /users/me

**Description:** Endpoint protegido que retorna los datos del usuario autenticado. Valida el token del header `Authorization: Bearer <token>`.

**Acceptance criteria:**
- [ ] `GET /users/me` con token válido retorna `{"id": ..., "username": "...", "name": "..."}`
- [ ] `GET /users/me` sin header `Authorization` retorna 403
- [ ] `GET /users/me` con token inválido retorna 403

**Verification:**
- [ ] `curl -H "Authorization: Bearer mock-token-1" /users/me` → 200 + datos usuario
- [ ] `curl /users/me` → 403
- [ ] `curl -H "Authorization: Bearer token-falso" /users/me` → 403

**Dependencies:** Task 3

**Files:**
- `examples/login-api/routers/auth.py`

**Scope:** S

---

### Checkpoint: Endpoints

- [ ] Los 4 escenarios de los criterios de éxito del spec funcionan manualmente
- [ ] App no lanza excepciones no manejadas
- [ ] Revisar con el usuario antes de continuar

---

## Phase 3: Tests y documentación

### Task 5: Suite de tests con pytest + httpx

**Description:** Tests de integración que cubren todos los criterios de éxito del spec usando `httpx.AsyncClient` contra la app en memoria.

**Acceptance criteria:**
- [ ] Test: login exitoso → 200 + token
- [ ] Test: login con password incorrecto → 401
- [ ] Test: login con usuario inexistente → 401
- [ ] Test: GET /users/me con token válido → 200 + datos
- [ ] Test: GET /users/me sin token → 403
- [ ] Test: GET /users/me con token inválido → 403
- [ ] `pytest tests/ -v` pasa todos sin errores

**Verification:**
- [ ] `pytest tests/ -v` → 6 passed, 0 failed
- [ ] No warnings de pytest-asyncio

**Dependencies:** Task 4

**Files:**
- `examples/login-api/tests/test_auth.py`
- `examples/login-api/pytest.ini` (config asyncio_mode=auto)

**Scope:** M

---

### Task 6: README.md

**Description:** Documentación mínima del ejemplo: cómo instalarlo, ejecutarlo, correr los tests y qué endpoints tiene.

**Acceptance criteria:**
- [ ] Instrucciones de instalación (`pip install -r requirements.txt`)
- [ ] Instrucciones de ejecución (`uvicorn main:app --reload`)
- [ ] Tabla de endpoints con método, ruta, descripción y ejemplo curl
- [ ] Instrucciones para correr tests (`pytest tests/ -v`)
- [ ] Credenciales de los usuarios mock documentadas

**Verification:**
- [ ] README.md existe y cubre los 5 puntos anteriores

**Dependencies:** Task 5

**Files:**
- `examples/login-api/README.md`

**Scope:** XS

---

### Checkpoint: Completo

- [ ] `pytest tests/ -v` → todos los tests pasan
- [ ] Los 4 criterios de salida del spec verificados
- [ ] README.md claro y usable
- [ ] Listo para /review y /ship

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| pytest-asyncio config incorrecta | Med | Usar `pytest.ini` con `asyncio_mode = auto` |
| Ruta de `data/users.json` relativa al cwd | Med | Usar `Path(__file__).parent` para ruta absoluta |
| Token "activo" se pierde entre tests | Low | Limpiar `active_tokens` en fixture de setup |

## Open Questions

- Ninguna — spec completo y aprobado.
