from pytest_html_reporter import attach
from selenium.webdriver.common.by import By
from automation.utils.base_pages import BasePage
from automation.utils.selectors import Selectors


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.username_input = (By.CSS_SELECTOR, Selectors.profile["Userinput"])
        self.password_button = (By.CSS_SELECTOR, Selectors.profile["PasswordInput"])
        self.login_button = (By.CSS_SELECTOR, Selectors.profile["LoginButton"])

    def login(self, username, password, url_expect):
        self.type(self.username_input, username)
        self.type(self.password_button, password)
        attach(data=self.driver.get_screenshot_as_png())
        self.wait_for_time_seconds(3)
        self.click(self.login_button)
        self.wait_for_time_seconds(7)
        attach(data=self.driver.get_screenshot_as_png())
        self.assert_url(url_expect)
