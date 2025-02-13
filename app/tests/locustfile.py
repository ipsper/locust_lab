from locust import HttpUser, between, task

class MinAnvandare(HttpUser):
    wait_time = between(1, 3)
    host = "https://min-api.com"  # Ersätt med din API-adress

    @task
    def halla_hej(self):
        self.client.get("/hej")

    @task
    def annan_endpoint(self):
        self.client.post("/annan", json={"data": "något"})

