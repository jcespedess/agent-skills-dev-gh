import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from routers.auth import active_tokens


@pytest.fixture(autouse=True)
def clear_tokens():
    active_tokens.clear()
    yield
    active_tokens.clear()


@pytest.mark.asyncio
async def test_users_me_with_valid_token():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Obtener token via login
        login = await client.post("/auth/login", json={"username": "admin", "password": "admin123"})
        token = login.json()["token"]
        # Usar token
        response = await client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "admin"
    assert data["name"] == "Administrador"
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_users_me_without_token():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/users/me")
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_users_me_with_invalid_token():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/users/me", headers={"Authorization": "Bearer token-falso"})
    assert response.status_code == 403
