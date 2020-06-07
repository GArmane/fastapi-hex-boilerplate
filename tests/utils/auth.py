from operator import attrgetter

from app.config.environment import get_settings

secret_key = attrgetter("JWT_SECRET_KEY")(get_settings())


def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}


def build_form_data(credentials):
    return {
        "grant_type": "password",
        "username": credentials.email,
        "password": credentials.password,
    }
