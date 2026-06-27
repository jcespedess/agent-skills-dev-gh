# Todo: Login API — Example

## Phase 1: Fundación
- [x] Task 1: Setup del proyecto (estructura, requirements.txt, main.py + /health)
- [x] Task 2: Mock data y modelos Pydantic (users.json, models/user.py, data_loader.py)
- [x] CHECKPOINT: app arranca, modelos importan

## Phase 2: Endpoints
- [x] Task 3: POST /auth/login (credenciales válidas → token, inválidas → 401)
- [x] Task 4: GET /users/me (token válido → datos, sin token → 403)
- [x] CHECKPOINT: 4 escenarios del spec funcionan manualmente

## Phase 3: Tests y documentación
- [x] Task 5: Suite de tests pytest + httpx (6 casos)
- [x] Task 6: README.md
- [x] CHECKPOINT: pytest pasa, criterios de salida del spec verificados
