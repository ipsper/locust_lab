from locust import HttpUser, between, task
from faker import Faker

fake = Faker()

class MinAnvandare(HttpUser):
    wait_time = between(1, 3)
    host = "http://192.168.1.101:8000"

    @task
    def get_all_anvandare(self):
        self.client.get("/users")

    @task
    def skapa_anvandare(self):
        namn = fake.name()
        email = fake.email()
        user_data = {"name": namn, "email": email}
        print(f"Skickar POST-begäran till /users med data: {user_data}")
        response = self.client.post("/users", json=user_data)
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")

    @task
    def rakna_anvandare(self):
        self.client.get("/users/count")

    @task
    def get_all_kort(self):
        self.client.get("/cards")

    @task
    def skapa_anvandare(self):
        namn = fake.name()
        email = fake.email()
        cards_data = {"title": namn, "description": email}
        response = self.client.post("/cards", json=cards_data)
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")

    @task
    def rakna_anvandare(self):
        self.client.get("/cards/count")

