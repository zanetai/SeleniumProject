from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class CartPage(BasePage):
    __url = "https://kawaiherbata.com/koszyk"
    __product_grinding = (By.XPATH, "//div[@id='cartProductsWrapper']/table[@class='cart_products table']//div["
                                    "@class='cart_product_grinding']/span[@class='badge badge-light']")
    __product_packaging = (By.XPATH, "/html//div[@id='cartProductsWrapper']/table[@class='cart_products table']//div["
                                     "@class='cart_product_packaging']/span[@class='badge badge-light']")
    __product_quantity = (By.XPATH, "/html//input[@id='quantity_0']")

    __remove_item_button = (By.XPATH, "//div[@id='cartProductsWrapper']/table[@class='cart_products table']//a["
                                      "@href='/koszyk/usun?id=0']")
    __removal_confirmation = (By.XPATH, "//form[@id='form_cart']/div[1]")

    __product_type = (By.XPATH, "//div[@id='cartProductsWrapper']/table[@class='cart_products table']/tbody/tr[1]/td[3]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def get_product_type(self):
        product_string = super()._get_text(self.__product_type)
        return product_string.split("\n")[0]

    def get_product_grinding(self):
        return super()._get_text(self.__product_grinding)

    def get_product_packaging(self):
        return super()._get_text(self.__product_packaging)

    def get_product_quantity(self):
        return super()._get_attribute(self.__product_quantity, "value")

    def remove_item_from_cart(self):
        super()._click(self.__remove_item_button)

    def get_removal_confirmation(self):
        return super()._get_text(self.__removal_confirmation)

    @property
    def get_expected_url(self) -> str:
        return self.__url
