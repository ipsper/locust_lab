from locust.env import Environment
from locustfile_k8_lab import MinAnvandare  # Importera din Locust-klass

def test_api():
    # Skapa en Locust-miljö
    env = Environment(user_classes=[MinAnvandare])

    # Starta Locust-testet i bakgrunden
    env.create_local_runner()
    env.runner.start(user_count=100, spawn_rate=10)  # Starta 100 användare med en spawn rate på 10

    # Vänta en stund så att testet hinner köra
    import time
    time.sleep(1)  # Justera tiden efter behov

    # Stoppa Locust-testet
    env.runner.quit()

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Du kan också kolla på enskilda requests
    for request in stats.entries.values():
        print(f"Request name: {request.name}")
        print(f"Number of requests: {request.num_requests}")
        print(f"Average response time: {request.avg_response_time}")
        assert request.name in ["/users", "/users/count", "/cards", "/cards/count"]  # Exempel: Kolla bara på vissa requests
        assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid