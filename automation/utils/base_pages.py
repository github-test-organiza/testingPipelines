import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_text(self, locator):
        return (
            WebDriverWait(self.driver, 10)
            .until(EC.visibility_of_element_located(locator))
            .text
        )

    def is_visible(self, locator):
        return (
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            is not None
        )

    def assert_url(self, expected_url: str):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected {expected_url}, but got {current_url}"
    
    def wait_for_time_seconds(self, seconds):
        time.sleep(seconds)
    


