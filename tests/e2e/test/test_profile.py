import pytest
from tests.e2e.pages.profile import ProfilePage
from tests.e2e.utils.common_data import CommonData


@pytest.mark.parametrize(
    "username, password, expected_url",
    [
        (
            CommonData.saucedemo_credentials["correct_user"],
            CommonData.saucedemo_credentials["passwordPage"],
            "https://www.saucedemo.com/inventory.html",
        ),
        (
            "invalid_user",
            CommonData.saucedemo_credentials["passwordPage"],
            "https://www.saucedemo.com/",
        ),
    ],
)
@pytest.mark.web
def test_login_web(driver, username, password, expected_url):
    _test_login(driver, username, password, expected_url)


@pytest.mark.parametrize(
    "username, password, expected_url",
    [
        (
            CommonData.saucedemo_credentials["correct_user"],
            CommonData.saucedemo_credentials["passwordPage"],
            "https://www.saucedemo.com/inventory.html",
        ),
        (
            "invalid_user",
            CommonData.saucedemo_credentials["passwordPage"],
            "https://www.saucedemo.com/",
        ),
    ],
)
@pytest.mark.mobile
def test_login_mobile(driver, username, password, expected_url):
    _test_login(driver, username, password, expected_url)


def _test_login(driver, username, password, expected_url):
    profile_page = ProfilePage(driver)
    driver.get("https://www.saucedemo.com/")
    profile_page.login(username, password, expected_url)
