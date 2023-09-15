import pytest
from page_objects.cart_page import CartPage
from page_objects.coffee_page import CoffeePage
from page_objects.main_page import MainPage


class TestLogin:
    @pytest.mark.cart
    def test_go_to_coffee_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_coffee_page()
        coffee_page = CoffeePage(driver)
        assert coffee_page.get_expected_url == coffee_page.current_url

    @pytest.mark.cart
    def test_add_to_cart(self, driver):
        coffee_page = CoffeePage(driver)
        coffee_page.open()
        coffee_page.show_add_to_cart_field()
        coffee_page.select_options("drobno mielona", "200", "5")
        coffee_page.add_to_cart()
        assert coffee_page.is_card_field_displayed()
        coffee_page.go_to_cart()
        cart_page = CartPage(driver)
        assert cart_page.get_expected_url == cart_page.current_url
        assert cart_page.get_product_type() == "Advocat"
        assert cart_page.get_product_grinding() == "drobno mielona"
        assert cart_page.get_product_packaging() == "200 g"
        assert cart_page.get_product_quantity() == "5"

    @pytest.mark.cart
    def test_remove_from_cart(self, driver):
        coffee_page = CoffeePage(driver)
        coffee_page.open()
        coffee_page.show_add_to_cart_field()
        coffee_page.select_options("drobno mielona", "200", "5")
        coffee_page.add_to_cart()
        coffee_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.remove_item_from_cart()
        assert cart_page.get_removal_confirmation() == "Usunięto produkt z koszyka"
