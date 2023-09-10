from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class CoffeePage(BasePage):
    __url = "https://kawaiherbata.com/kawy-1/"
    __add_to_cart_advocat_button = (By.XPATH,
                                    "//div[@id='content']/div[@class='container']/div[@class='row']/div[2]/div["
                                    "3]/div[@class='row']/div[1]/div[@class='pb-shadow']/div["
                                    "@class='pb-shadow-inner']/div[@class='pb-price']/span[@class='add-to-cart']")
    __grinding_select_form = (By.XPATH, "//select[@id='grindingSelect']")
    __packaging_select_form = (By.XPATH, "//select[@id='packagingSelect']")
    __quantity_select_form = (By.XPATH, "//select[@id='quantitySelect']")
    __add_to_cart_button = (By.CSS_SELECTOR, ".btn-addtocart-ajax-form")
    __cart_field = (By.ID, "headerCartPopup")
    __go_to_cart_button = (By.XPATH, "//div[@id='top_pasek']/div[@class='row']//div[@class='col-12 col-md-6 "
                                     "text-left']/a[@href='/koszyk']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def show_add_to_cart_field(self):
        super()._click(self.__add_to_cart_advocat_button)

    def select_options(self, value_grinding: str, value_packaging: str, value_quantity: str):
        super()._dropdown(self.__grinding_select_form, value_grinding)
        super()._dropdown(self.__packaging_select_form, value_packaging)
        super()._dropdown(self.__quantity_select_form, value_quantity)

    def add_to_cart(self):
        super()._click(self.__add_to_cart_button)

    def is_card_field_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__cart_field)
        return super()._is_displayed(self.__cart_field)

    def go_to_cart(self):
        super()._click(self.__go_to_cart_button)

    @property
    def get_expected_url(self) -> str:
        return self.__url




