from locust import HttpUser, between, task
from faker import Faker

fake = Faker()

class MinAnvandare(HttpUser):
    wait_time = between(1, 3)
    host = "http://192.168.1.101:8000"

    @task
    def halla_hej(self):
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


