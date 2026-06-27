import json
from pathlib import Path


def load_users() -> list[dict]:
    path = Path(__file__).parent / "data" / "users.json"
    return json.loads(path.read_text())


def find_user(username: str, password: str) -> dict | None:
    return next(
        (u for u in load_users() if u["username"] == username and u["password"] == password),
        None,
    )
