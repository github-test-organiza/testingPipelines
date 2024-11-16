import json
import pytest
from selenium.webdriver.common.by import By
from tests.automation.pages.profile_page import ProfilePage

# Carga datos comunes
with open("./tests/utils/common_data.json", encoding="utf-8") as f:
    test_data = json.load(f)


@pytest.mark.usefixtures("driver")
def login_in_swag_page(driver):
    # Abrir la URL
    driver.get("https://www.saucedemo.com/")

    # Instanciar la página de perfil
    profile_page = ProfilePage(driver)

    # Buscar trabajo
    username = test_data["saucedemo"]["correct_user"]
    password = test_data["saucedemo"]["passwordPage"]

    profile_page.login(username, password)

    # Verificar resultados


# results = profile_page.get_results()
# assert len(results) > 0, "No se encontraron resultados para el trabajo buscado"
