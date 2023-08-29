import pytest
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage


class TestLogin:
    @pytest.mark.login
    def test_go_to_login_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(driver)
        assert login_page.get_expected_url == login_page.current_url

    @pytest.mark.login
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("zaneta.ignatz@o2.pl", "password123")
        main_page = MainPage(driver)
        assert main_page.is_logout_button_displayed()
        assert not main_page.is_login_button_displayed()

    @pytest.mark.login
    @pytest.mark.parametrize("username, password",
                             [("IncorrectUser", "password123"),
                              ("zaneta.ignatz@o2.pl", "IncorrectPassword")])
    def test_negative_login(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == "Nieprawidłowy login lub hasło"

    @pytest.mark.login
    def test_log_out(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("zaneta.ignatz@o2.pl", "password123")
        main_page = MainPage(driver)
        main_page.execute_logout()
        assert main_page.is_login_button_displayed()
        assert not main_page.is_logout_button_displayed()




