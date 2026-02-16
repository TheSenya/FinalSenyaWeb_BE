import pytest
from app.main import app
from fastapi.testclient import TestClient

# Pytest fixtures are a way to setup reuseable code that the test need
# they are fresh per every isntance of the test, can be parametrized, scoped or overwritten
# ex.
# def client():
#     # SETUP — runs before the test
#     client = TestClient(app)
#     yield client
#     # TEARDOWN — runs after the test (even if it fails)
#     # e.g., close connections, clean up temp files


@pytest.fixture
def client():
    return TestClient(app)


def test_health_check(client):

    request = client.get("/health")

    assert request.status_code == 200
    assert request.json() == {"status": "ok"}
