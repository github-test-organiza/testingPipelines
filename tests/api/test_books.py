import pytest
from api_resquest import Api


class TestBooksApi:

    @pytest.fixture
    def api_instance(self) -> Api:
        return Api()

    @pytest.mark.api
    def test_should_create_user(self, api_instance: Api):
        status_code, response = api_instance.create_new_user(
            "testing003", "Testing@1234"
        )
        user_id = response.get("userID")
        username = response.get("username")
        print("HTTP Status Code:", status_code)
        print(response)
        assert status_code == 201
        assert user_id is not None
        assert username is not None
