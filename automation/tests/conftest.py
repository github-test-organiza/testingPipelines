import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

logging.basicConfig(level=logging.INFO)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use: chrome or firefox",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode",
    )


@pytest.fixture(scope="function")
def driver(request):
    logging.info("Dentroooooooooo")
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    # Detectar marcadores específicos
    markers = [mark.name for mark in request.node.iter_markers()]
    device = "desktop"  # Valor por defecto

    if "mobile" in markers:
        device = "mobile"
    elif "web" in markers:
        device = "desktop"

    if browser == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        # Configuración del tamaño de ventana basado en el marcador
        if device == "mobile":
            options.add_argument("--window-size=375,667")
        else:
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        # Configuración del tamaño de ventana basado en el marcador
        driver = webdriver.Firefox(options=options)
        if device == "mobile":
            driver.set_window_size(375, 667)
        else:
            driver.set_window_size(1920, 1080)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    logging.info(f"Ejecutando en el navegador {browser} en versión {device} ")
    yield driver
    driver.quit()
