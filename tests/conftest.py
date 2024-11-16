import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="function")
def driver():
    # Configurar WebDriver con webdriver-manager
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar sin GUI (opcional)
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    yield driver
    driver.quit()
