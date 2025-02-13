from locust.env import Environment
from locust.clients import HttpSession
from locust.user.users import User
import pytest

class MockUser(User):  # Skapa en dummy User-klass för testning
    def __init__(self, environment):
        super().__init__(environment)
        self.client = HttpSession(  # Ta bort 'environment' från initieringen
            base_url="http://example.com",  # Ange base_url direkt här
            request_event=environment.events.request,
            user=self
        )

@pytest.fixture
def locust_client():
    env = Environment(user_classes=[MockUser])  # Skapa en Locust-miljö
    env.create_local_runner()  # Skapa en Locust-runner
    mock_user = MockUser(env)  # Skapa en instans av MockUser
    return mock_user.client  # Returnera en fungerande HTTP-klient

def test_locust_api(locust_client):
    response = locust_client.get("/api/resource")
    assert response.status_code == 200
    assert "expected_key" in response.json()
