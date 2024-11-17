import pytest
from automation.pages.profile import ProfilePage
from automation.utils.common_data import CommonData

@pytest.mark.parametrize(
    "username, password, expected_url",
    [
        (CommonData.saucedemo_credentials["correct_user"], CommonData.saucedemo_credentials["passwordPage"], "https://www.saucedemo.com/inventory.html"),
        ("invalid_user", CommonData.saucedemo_credentials["passwordPage"], "https://www.saucedemo.com/"),
    ],
)
@pytest.mark.web
def test_login_web(driver, username, password, expected_url):
    # Instanciar la página de perfil
    profile_page = ProfilePage(driver)
    # Abrir la URL
    driver.get("https://www.saucedemo.com/")

    profile_page.login(username, password, expected_url)

@pytest.mark.parametrize(
    "username, password, expected_url",
    [
        (CommonData.saucedemo_credentials["correct_user"], CommonData.saucedemo_credentials["passwordPage"], "https://www.saucedemo.com/inventory.html"),
        ("invalid_user", CommonData.saucedemo_credentials["passwordPage"], "https://www.saucedemo.com/"),
    ],
)
@pytest.mark.mobile
def test_login_mobile(driver, username, password, expected_url):
    # Instanciar la página de perfil
    profile_page = ProfilePage(driver)
    # Abrir la URL
    driver.get("https://www.saucedemo.com/")

    profile_page.login(username, password, expected_url)
