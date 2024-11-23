import requests


class Api:

    def __init__(self, base_url: str = "https://demoqa.com"):
        self.base_url = base_url
        self.endpoints = {
            "create_user": "/Account/v1/User",
            "generate_token": "/Account/v1/GenerateToken",
        }

    def create_new_user(self, username: str, password: str):
        url = self.base_url + self.endpoints["create_user"]
        request_data = {"userName": username, "password": password}
        response = requests.post(url, data=request_data, timeout=5)
        status_code = response.status_code
        response_data = response.json()
        return status_code, response_data

    def get_access_token(self, username: str, password: str):
        url = self.base_url + self.endpoints["generate_token"]
        request_data = {"userName": username, "password": password}
        response = requests.post(url, data=request_data, timeout=5)
        status_code = response.status_code
        response_data = response.json()
        return status_code, response_data
