from locust import HttpUser, between, task
from logger_config import logger

class MinAnvandare(HttpUser):
    wait_time = between(1, 3)
    host = "http://192.168.1.101:8000"
    responses = {}  # Klassvariabel för att lagra svaren

    @task
    def get_all_anvandare(self):
        response = self.client.get("/users")
        MinAnvandare.responses["get_all_anvandare"] = response  # Lagra svaret
        logger.info(f"get_all_anvandare response: {response.status_code}")
        self.environment.events.request_success.fire(
            request_type="GET",
            name="/users",
            response_time=response.elapsed.total_seconds() * 1000,
            response_length=len(response.content),
            response=response
        )

    @task
    def skapa_anvandare(self, user_data):
        response = self.client.post("/users", json=user_data)
        MinAnvandare.responses["skapa_anvandare"] = response  # Lagra svaret
        logger.info(f"skapa_anvandare response: {response.status_code}")
        self.environment.events.request.fire(
            request_type="POST",
            name="/users",
            response_time=response.elapsed.total_seconds() * 1000,
            response_length=len(response.content),
            response=response
        )

    @task
    def rakna_anvandare(self):
        response = self.client.get("/users/count")
        MinAnvandare.responses["rakna_anvandare"] = response  # Lagra svaret
        logger.info(f"rakna_anvandare response: {response.status_code}")
        self.environment.events.request_success.fire(
            request_type="GET",
            name="/users/count",
            response_time=response.elapsed.total_seconds() * 1000,
            response_length=len(response.content),
            response=response
        )

    @task
    def delete_all_anvandare(self):
        # Ta bort alla anvandare
        response = self.client.delete("/users/")
        MinAnvandare.responses["delete_all_anvandare"] = response  # Lagra svaret
        logger.info(f"delete_all_anvandare response: {response.status_code}")
        self.environment.events.request.fire(
            request_type="DELETE",
            name="/users/",
            response_time=response.elapsed.total_seconds() * 1000,
            response_length=len(response.content),
            response=response
        )

    @task
    def get_all_kort(self):
        response = self.client.get("/cards")
        MinAnvandare.responses["get_all_kort"] = response  # Lagra svaret
        logger.info(f"get_all_kort response: {response.status_code}")
        self.environment.events.request_success.fire(
            request_type="GET",
            name="/cards",
            response_time=response.elapsed.total_seconds() * 1000,
            response_length=len(response.content),
            response=response
        )

    @task
    def skapa_kort(self, card_data):
        response = self.client.post("/cards", json=card_data)
        MinAnvandare.responses["skapa_kort"] = response  # Lagra svaret
        logger.info(f"skapa_kort response: {response.status_code}")
        self.environment.events.request.fire(
            request_type="POST",
            name="/cards",
            response_time=response.elapsed.total_seconds() * 1000,
            response_length=len(response.content),
            response=response
        )

    @task
    def rakna_kort(self):
        response = self.client.get("/cards/count")
        MinAnvandare.responses["rakna_kort"] = response  # Lagra svaret
        logger.info(f"rakna_kort response: {response.status_code}")
        self.environment.events.request_success.fire(
            request_type="GET",
            name="/cards/count",
            response_time=response.elapsed.total_seconds() * 1000,
            response_length=len(response.content),
            response=response
        )

    @task
    def delete_all_kort(self):
        # Ta bort alla kort
        response = self.client.delete("/cards/")
        MinAnvandare.responses["delete_all_kort"] = response  # Lagra svaret
        logger.info(f"delete_all_kort response: {response.status_code}")
        self.environment.events.request.fire(
            request_type="DELETE",
            name="/cards/",
            response_time=response.elapsed.total_seconds() * 1000,
            response_length=len(response.content),
            response=response
        )
