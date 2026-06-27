from fastapi import APIRouter, Header, HTTPException
from models.user import LoginRequest, LoginResponse, UserMe
from data_loader import find_user, load_users

router = APIRouter()

# Tokens activos en memoria: token → user_id
active_tokens: dict[str, int] = {}


@router.post("/auth/login", response_model=LoginResponse)
# En producción agregar rate limiting (ej. slowapi) para prevenir fuerza bruta
async def login(credentials: LoginRequest) -> LoginResponse:
    user = find_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    # Token predecible a propósito — solo para ejemplos; en producción usar JWT u OAuth2
    token = f"mock-token-{user['id']}"
    active_tokens[token] = user["id"]
    return LoginResponse(token=token, username=user["username"])


@router.get("/users/me", response_model=UserMe)
async def users_me(authorization: str | None = Header(default=None)) -> UserMe:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Token requerido")
    token = authorization.removeprefix("Bearer ")
    user_id = active_tokens.get(token)
    if user_id is None:
        raise HTTPException(status_code=403, detail="Token inválido")
    user = next((u for u in load_users() if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=403, detail="Usuario no encontrado")
    return UserMe(id=user["id"], username=user["username"], name=user["name"])
