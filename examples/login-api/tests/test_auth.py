"""
Suite de integración — cubre los 6 criterios de salida del spec.
Usa httpx.AsyncClient contra la app FastAPI en memoria.
"""
import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from routers.auth import active_tokens


@pytest.fixture(autouse=True)
def reset_tokens():
    active_tokens.clear()
    yield
    active_tokens.clear()


# ── POST /auth/login ──────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_login_credenciales_validas_retorna_200_y_token():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/auth/login", json={"username": "admin", "password": "admin123"})
    assert response.status_code == 200
    body = response.json()
    assert body["token"] == "mock-token-1"
    assert body["username"] == "admin"


@pytest.mark.asyncio
async def test_login_credenciales_invalidas_retorna_401():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/auth/login", json={"username": "admin", "password": "mal"})
    assert response.status_code == 401


# ── GET /users/me ─────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_users_me_con_token_valido_retorna_200_y_datos():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        login = await client.post("/auth/login", json={"username": "demo", "password": "devpass2024"})
        token = login.json()["token"]
        response = await client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    body = response.json()
    assert body["username"] == "demo"
    assert body["name"] == "Usuario Demo"


@pytest.mark.asyncio
async def test_users_me_sin_token_retorna_403():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/users/me")
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_users_me_token_invalido_retorna_403():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/users/me", headers={"Authorization": "Bearer token-falso"})
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_flujo_completo_login_y_perfil():
    """Flujo end-to-end: login → obtener perfil → verificar datos coherentes."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        login = await client.post("/auth/login", json={"username": "admin", "password": "admin123"})
        assert login.status_code == 200
        token = login.json()["token"]

        me = await client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
        assert me.status_code == 200
        assert me.json()["username"] == login.json()["username"]
