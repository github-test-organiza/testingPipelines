import json
from selenium.webdriver.common.by import By
from tests.automation.utils.base_pages import BasePage

# Carga selectores desde JSON
with open("./tests/data/selectors.json", encoding="utf-8") as f:
    selectors = json.load(f)


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.CSS_SELECTOR, selectors["profile"]["Userinput"])
        self.password_button = (By.CSS_SELECTOR, selectors["profile"]["PasswordInput"])
        self.login_button = (By.CSS_SELECTOR, selectors["profile"]["LoginButton"])

    # self.results = (By.CSS_SELECTOR, selectors["jobs"]["results"])

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_button, password)
        self.click(self.login_button)


# def get_results(self):
#   return self.driver.find_elements(*self.results)
