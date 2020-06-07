import pytest
from fastapi.testclient import TestClient  # type: ignore

from tests.utils.database import clear_database
from app.config.environment import get_settings
from app.api import init_app


@pytest.fixture(name="env_settings")
def env_settings():
    return get_settings()


@pytest.fixture(name="web_app")
def web_app_fixture(env_settings):
    return init_app(env_settings)


@pytest.fixture(name="test_client")
def test_client_fixture(web_app):
    with clear_database():
        yield TestClient(web_app)
