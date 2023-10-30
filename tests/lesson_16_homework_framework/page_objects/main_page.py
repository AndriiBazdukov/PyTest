from selenium.webdriver.common.by import By
from tests.lesson_16_homework_framework.page_objects.base_page import BasePage
from tests.lesson_16_homework_framework.page_objects.goods_details_page import GoodsDetailsPage
from tests.lesson_16_homework_framework.page_objects.shoping_cart_page import ShoppingCartPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_input = (By.CSS_SELECTOR, "._a5MACe._zpwZpb.header__search>input")
    __start_search_button = (By.CSS_SELECTOR, "._a5MACe._zpwZpb.header__search>._cvO7u1")
    __go_to_login_button = (By.CSS_SELECTOR, "[data-is='UserLogin']")
    __go_to_shopping_cart = (By.CSS_SELECTOR, "[data-is='SmallCart']")
    __global_site_header = (By.CSS_SELECTOR, "#global-site-header")
    __favorites_button = (By.CSS_SELECTOR, "[data-is='Favorites']")
    __compare_button = (By.CSS_SELECTOR, "[data-is='Compare']")
    __no_goods_warning = (By.CSS_SELECTOR, "._ysNrTN")
    # Find all goods on sale that visible on main page
    __goods_on_sale = (By.CSS_SELECTOR, "._Y3HNlP")
    # Finds purchase button for all goods on sale that visible on main page
    __goods_on_sale_purchase_button = (By.CSS_SELECTOR, "._Y3HNlP .add-product.card__button.btn.btn--yellow")

    def click_login_opener_button(self):
        from tests.lesson_16_homework_framework.page_objects.login_page import LoginPage
        self.click(self.__go_to_login_button)
        return LoginPage(self.driver)

    def click_shopping_cart_button(self):
        self.click(self.__go_to_shopping_cart)
        return ShoppingCartPage(self.driver)

    def click_favorites_button(self):
        from tests.lesson_16_homework_framework.page_objects.login_page import LoginPage
        self.click(self.__favorites_button)
        return LoginPage(self.driver)

    def click_compare_button(self):
        self.click(self.__compare_button)
        return self

    def is_main_page_opened(self):
        element = self.wait_element_is_visible(self.__global_site_header)
        return element.is_displayed()

    def is_warning_displayed(self):
        element = self.wait_element_is_visible(self.__no_goods_warning)
        return element.is_displayed()

    def get_user_displayed_name(self):
        name = self.get_element_text_content_property(self.__go_to_login_button)
        return name

    def click_on_random_item_on_sale(self):
        self.click_on_random_element_from_list(self.__goods_on_sale)
        return GoodsDetailsPage(self.driver)

    def click_purchase_on_random_item_on_sale(self):
        self.click_on_random_element_from_list(self.__goods_on_sale_purchase_button)
        return ShoppingCartPage(self.driver)

    def input_value_to_search(self, value="Праска"):
        self.send_keys(self.__search_input, value)
        return self

    def start_search(self):
        self.click(self.__start_search_button)
        return self

