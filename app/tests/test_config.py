import pytest
from app.core.config import get_settings


def test_get_settings():
    settings = get_settings()

    assert settings.ENV is not None

    # TODO: assert more settings here
