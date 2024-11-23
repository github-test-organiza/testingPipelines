from pytest_html_reporter import attach
from selenium.webdriver.common.by import By
from tests.e2e.utils.base_pages import BasePage
from tests.e2e.utils.selectors import Selectors
from selenium.webdriver.remote.webdriver import WebDriver


class ProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def login(self, username, password, url_expect):
        self.type(Selectors.profile["Userinput"], username)
        self.type(Selectors.profile["PasswordInput"], password)
        attach(data=self.driver.get_screenshot_as_png())
        self.wait_for_time_seconds(3)
        self.click(Selectors.profile["LoginButton"])
        self.wait_for_time_seconds(7)
        attach(data=self.driver.get_screenshot_as_png())
        self.assert_url(url_expect)
