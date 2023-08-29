from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://kawaiherbata.com/login"
    __username_field = (By.XPATH, "//div[@id='login-page']//form[@action='/login']//input[@name='email']")
    __password_field = (By.XPATH, "//div[@id='login-page']//form[@action='/login']//input[@name='password']")
    __login_button = (By.XPATH, "//div[@id='login-page']//form[@action='/login']/button[@type='submit']")
    __error_message = (By.XPATH, "//div[@id='login-page']//form[@action='/login']/div[@role='alert']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    @property
    def get_expected_url(self) -> str:
        return self.__url

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__login_button)

    def get_error_message(self):
        return super()._get_text(self.__error_message, 3)
