from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class MainPage(BasePage):
    __url = "https://kawaiherbata.com/"
    __login_button = (By.CLASS_NAME, "link-login-text")
    __logout_button = (By.CLASS_NAME, "link-logout-text")
    __coffee_button = (By.XPATH, "//div[@id='header-menu']//ul[@class='menu']//a[@title='Kawy']/h2[.='Kawy']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def go_to_login_page(self):
        super()._click(self.__login_button)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logout_button)

    def is_login_button_displayed(self) -> bool:
        return super()._is_displayed(self.__login_button)

    def execute_logout(self):
        super()._click(self.__logout_button)

    def go_to_coffee_page(self):
        super()._click(self.__coffee_button)
