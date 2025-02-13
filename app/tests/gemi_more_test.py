from locust.env import Environment
from locustfile_k8_lab import MinAnvandare  # Importera din Locust-klass
import time

def setup_environment():
    # Skapa en Locust-miljö
    env = Environment(user_classes=[MinAnvandare])
    env.create_local_runner()
    return env

def teardown_environment(env):
    # Stoppa Locust-testet
    env.runner.quit()

def test_get_all_anvandare():
    env = setup_environment()
    env.runner.start(user_count=100, spawn_rate=10)  # Starta 100 användare med en spawn rate på 10
    time.sleep(1)  # Justera tiden efter behov
    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/users":
            print(f"Request name: {request.name}")
            print(f"Number of requests: {request.num_requests}")
            print(f"Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

def test_skapa_anvandare():
    env = setup_environment()
    env.runner.start(user_count=100, spawn_rate=10)  # Starta 100 användare med en spawn rate på 10
    time.sleep(1)  # Justera tiden efter behov
    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/users":
            print(f"Request name: {request.name}")
            print(f"Number of requests: {request.num_requests}")
            print(f"Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

def test_rakna_anvandare():
    env = setup_environment()
    env.runner.start(user_count=100, spawn_rate=10)  # Starta 100 användare med en spawn rate på 10
    time.sleep(1)  # Justera tiden efter behov
    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/users/count":
            print(f"Request name: {request.name}")
            print(f"Number of requests: {request.num_requests}")
            print(f"Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

def test_get_all_kort():
    env = setup_environment()
    env.runner.start(user_count=100, spawn_rate=10)  # Starta 100 användare med en spawn rate på 10
    time.sleep(1)  # Justera tiden efter behov
    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/cards":
            print(f"Request name: {request.name}")
            print(f"Number of requests: {request.num_requests}")
            print(f"Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

def test_skapa_kort():
    env = setup_environment()
    env.runner.start(user_count=100, spawn_rate=10)  # Starta 100 användare med en spawn rate på 10
    time.sleep(1)  # Justera tiden efter behov
    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/cards":
            print(f"Request name: {request.name}")
            print(f"Number of requests: {request.num_requests}")
            print(f"Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

def test_rakna_kort():
    env = setup_environment()
    env.runner.start(user_count=100, spawn_rate=10)  # Starta 100 användare med en spawn rate på 10
    time.sleep(1)  # Justera tiden efter behov
    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/cards/count":
            print(f"Request name: {request.name}")
            print(f"Number of requests: {request.num_requests}")
            print(f"Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid