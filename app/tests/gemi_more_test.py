from locust.env import Environment
from locustfile_k8_lab import MinAnvandare  # Importera din Locust-klass
from faker import Faker
import time

fake = Faker()

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
    time.sleep(2)  # Justera tiden efter behov
    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio <= 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/users":
            print(f"test_get_all_anvandare Request name: {request.name}")
            print(f"test_get_all_anvandare Number of requests: {request.num_requests}")
            print(f"test_get_all_anvandare Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

    # Hämta svaret från Locust-uppgiften
    response = MinAnvandare.responses.get("get_all_anvandare")
    print(f"test_get_all_anvandare response: {response}")  # Lägg till loggning
    assert response is not None, "Response should not be None"

    # Lägg till assert på antalet element i JSON-svaret
    json_data = response.json()
    assert isinstance(json_data, dict)  # Kontrollera att svaret är ett objekt
    assert "users" in json_data  # Kontrollera att 'users' finns i objektet
    assert isinstance(json_data["users"], list)  # Kontrollera att 'users' är en lista
    assert len(json_data["users"]) >= 0  # Kontrollera att listan inte är tom

def test_delete_all_anvandare():
    env = setup_environment()
    user = MinAnvandare(env)  # Skapa en instans av MinAnvandare

    # Kör uppgiften för att ta bort alla användare
    user.delete_all_anvandare()

    teardown_environment(env)

    # Kontrollera att alla användare är borttagna
    response = user.client.get("/users")
    assert response.status_code == 200, "Failed to get users"
    users = response.json()["users"]
    assert len(users) == 0, "Not all users were deleted"

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/users/":
            print(f"test_delete_all_anvandare Request name: {request.name}")
            print(f"test_delete_all_anvandare Number of requests: {request.num_requests}")
            print(f"test_delete_all_anvandare Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

    # Kontrollera att alla kort är borttagna
    response = user.client.get("/users")
    assert response.status_code == 200, "Failed to get users"
    users = response.json()["users"]
    assert len(users) == 0, "Not all users were deleted"


def test_skapa_anvandare():
    env = setup_environment()
    user = MinAnvandare(env)  # Skapa en instans av MinAnvandare

    # Skapa 100 användare
    for i in range(100):
        namn = fake.name()
        email = f"{fake.email().split('@')[0]}_{i}@example.com"  # Generera unika e-postadresser
        user_data = {"name": namn, "email": email}
        user.skapa_anvandare(user_data)  # Skicka data till Locust-uppgiften
        time.sleep(0.1)  # Justera tiden efter behov
    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests >= 100
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/users":
            print(f"test_skapa_anvandare Request name: {request.name}")
            print(f"test_skapa_anvandare Number of requests: {request.num_requests}")
            print(f"test_skapa_anvandare Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

    # Hämta svaret från Locust-uppgiften
    response = MinAnvandare.responses.get("skapa_anvandare")
    print(f"test_skapa_anvandare response: {response}")  # Lägg till loggning
    assert response is not None, "Response should not be None"

    # Lägg till assert på JSON-svaret
    json_data = response.json()
    print(f"test_skapa_anvandare JSON response: {json_data}")
    assert "user" in json_data  # Kontrollera att 'user' finns i JSON-svaret
    assert "name" in json_data["user"] and "email" in json_data["user"]  # Kontrollera att 'name' och 'email' finns i 'user'-objektet

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
            print(f"test_rakna_anvandare Request name: {request.name}")
            print(f"test_rakna_anvandare Number of requests: {request.num_requests}")
            print(f"test_rakna_anvandare Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid
            
    # Hämta svaret från Locust-uppgiften
    response = MinAnvandare.responses.get("rakna_anvandare")
    print(f"test_rakna_anvandare response: {response}")  # Lägg till loggning
    assert response is not None, "Response should not be None"

    # Lägg till assert på JSON-svaret
    json_data = response.json()
    print(f"test_rakna_anvandare JSON response: {json_data}")
    assert "count" in json_data  # Kontrollera att 'count' finns i JSON-svaret
    assert json_data["count"] >= 0  # Kontrollera att 'count' är ett icke-negativt tal

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
            print(f"test_get_all_kort Request name: {request.name}")
            print(f"test_get_all_kort Number of requests: {request.num_requests}")
            print(f"test_get_all_kort Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

    # Hämta svaret från Locust-uppgiften
    response = MinAnvandare.responses.get("get_all_kort")
    print(f"test_get_all_kort response: {response}")  # Lägg till loggning
    assert response is not None, "Response should not be None"

    # Lägg till assert på antalet element i JSON-svaret
    json_data = response.json()
    assert isinstance(json_data, dict)  # Kontrollera att svaret är ett objekt
    assert "cards" in json_data  # Kontrollera att 'cards' finns i objektet
    assert isinstance(json_data["cards"], list)  # Kontrollera att 'cards' är en lista
    assert len(json_data["cards"]) >= 0  # Kontrollera att listan inte är tom
    print(f"test_get_all_kort Number of elements in response: {len(json_data['cards'])}")

def test_skapa_kort():
    env = setup_environment()
    card = MinAnvandare(env)  # Skapa en instans av MinAnvandare

    # Skapa 100 kort
    for i in range(100):
        title = f"Card Title {i}"
        description = f"Card Description {i}"
        card_data = {"title": title, "description": description}
        card.skapa_kort(card_data)  # Skicka data till Locust-uppgiften
        time.sleep(0.1)  # Justera tiden efter behov

    teardown_environment(env)

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/cards":
            print(f"test_skapa_kort Request name: {request.name}")
            print(f"test_skapa_kort Number of requests: {request.num_requests}")
            print(f"test_skapa_kort Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

    # Hämta svaret från Locust-uppgiften
    response = MinAnvandare.responses.get("skapa_kort")
    print(f"test_skapa_kort response: {response}")  # Lägg till loggning
    assert response is not None, "Response should not be None"

    # Lägg till assert på JSON-svaret
    json_data = response.json()
    print(f"test_skapa_kort JSON response: {json_data}")
    assert "card" in json_data  # Kontrollera att 'card' finns i JSON-svaret
    assert "title" in json_data["card"] and "description" in json_data["card"]  # Kontrollera att 'title' och 'description' finns i 'card'-objektet


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
            print(f"test_rakna_kort Request name: {request.name}")
            print(f"test_rakna_kort Number of requests: {request.num_requests}")
            print(f"test_rakna_kort Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

    # Hämta svaret från Locust-uppgiften
    response = MinAnvandare.responses.get("rakna_kort")
    print(f"test_rakna_kort response: {response}")  # Lägg till loggning
    assert response is not None, "Response should not be None"

    # Lägg till assert på JSON-svaret
    json_data = response.json()
    print(f"test_rakna_kort JSON response: {json_data}")
    assert "count" in json_data  # Kontrollera att 'count' finns i JSON-svaret
    assert json_data["count"] >= 0  # Kontrollera att 'count' är ett icke-negativt tal

def test_delete_all_kort():
    env = setup_environment()
    user = MinAnvandare(env)  # Skapa en instans av MinAnvandare

    # Kör uppgiften för att ta bort alla kort
    user.delete_all_kort()

    teardown_environment(env)

    # Kontrollera att alla kort är borttagna
    response = user.client.get("/cards")
    assert response.status_code == 200, "Failed to get cards"
    cards = response.json()["cards"]
    assert len(cards) == 0, "Not all cards were deleted"

    # Hämta statistiken från Locust
    stats = env.stats

    # Använd pytest för att göra asserts på resultatet
    assert stats.total.num_requests > 0
    assert stats.total.fail_ratio < 0.1  # Exempel: Max 10% fel

    # Kolla på enskilda requests
    for request in stats.entries.values():
        if request.name == "/cards/":
            print(f"test_delete_all_kort Request name: {request.name}")
            print(f"test_delete_all_kort Number of requests: {request.num_requests}")
            print(f"test_delete_all_kort Average response time: {request.avg_response_time}")
            assert request.avg_response_time < 500  # Exempel: Max 500ms svarstid

    # Kontrollera att alla kort är borttagna
    response = user.client.get("/cards")
    assert response.status_code == 200, "Failed to get cards"
    cards = response.json()["cards"]
    assert len(cards) == 0, "Not all cards were deleted"
