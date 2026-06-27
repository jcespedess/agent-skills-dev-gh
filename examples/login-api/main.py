from fastapi import FastAPI
from routers.auth import router as auth_router

app = FastAPI(title="Login API Example")
app.include_router(auth_router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
