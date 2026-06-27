from models.user import LoginRequest, LoginResponse, UserMe
from data_loader import load_users, find_user


def test_load_users_returns_list():
    users = load_users()
    assert isinstance(users, list)
    assert len(users) >= 2


def test_find_user_valid():
    user = find_user("admin", "admin123")
    assert user is not None
    assert user["username"] == "admin"


def test_find_user_invalid():
    assert find_user("admin", "wrong") is None
    assert find_user("noexiste", "pass") is None


def test_login_request_schema():
    req = LoginRequest(username="admin", password="admin123")
    assert req.username == "admin"


def test_login_response_schema():
    res = LoginResponse(token="mock-token-1", username="admin")
    assert res.token == "mock-token-1"


def test_user_me_schema():
    u = UserMe(id=1, username="admin", name="Administrador")
    assert u.id == 1
