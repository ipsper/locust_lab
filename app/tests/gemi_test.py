
import pytest
from locust import Environment
from locustfile import MinAnvandare  # Importera din Locust-klass

def test_api():
    # Skapa en Locust-miljö
    env = Environment(user_classes=[MinAnvandare])

    # Starta Locust-testet i bakgrunden
    env.create_local_runner()
    env.runner.start(100)  # Starta 100 användare

    # Vänta en stund så att testet hinner köra
    import time
    time.sleep(10)  # Justera tiden efter behov

    # Stoppa Locust-testet
    env.runner.quit()

    # Hämta statistiken från Locust
    stats = env.stats.get_current()

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Du kan också kolla på enskilda requests
    for request in stats.entries:
        assert request.name == "/hej" or request.name == "/annan"
        assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

