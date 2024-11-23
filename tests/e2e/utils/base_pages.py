import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def click(self, selector: str):
        locator = (By.CSS_SELECTOR, selector)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, selector: str, text: str):
        locator = (By.CSS_SELECTOR, selector)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_text(self, selector: str):
        locator = (By.CSS_SELECTOR, selector)
        return (
            WebDriverWait(self.driver, 10)
            .until(EC.visibility_of_element_located(locator))
            .text
        )

    def is_visible(self, selector: str):
        locator = (By.CSS_SELECTOR, selector)
        return (
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            is not None
        )

    def assert_url(self, expected_url: str):
        current_url = self.driver.current_url
        assert (
            current_url == expected_url
        ), f"Expected {expected_url}, but got {current_url}"

    def wait_for_time_seconds(self, seconds):
        time.sleep(seconds)
