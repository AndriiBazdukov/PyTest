from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.lesson_16_homework_framework.page_objects.base_page import BasePage


class ShoppingCartPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    __shopping_cart_screen = (By.CSS_SELECTOR, ".basket")
    __back_to_shopping_link = (By.CSS_SELECTOR, ".basket-empty__message.basket-empty__message--link.link")
    __quantity_input = (By.CSS_SELECTOR, ".form-quantity input")
    __decrease_quantity_button = (By.CSS_SELECTOR, ".form-quantity button:nth-child(1)")
    __increase_quantity_button = (By.CSS_SELECTOR, ".form-quantity button:nth-child(3)")
    __total_price_for_item = (By.CSS_SELECTOR, ".basket-product__price-main")
    __delete_item_button = (By.CSS_SELECTOR, ".basket-product__del--link")
    __delete_all_items_button = (By.CSS_SELECTOR, "#js-trigger-del")
    __close_button = (By.CSS_SELECTOR, ".fancybox-button.fancybox-close-small")
    __continue_shopping_button = (By.CSS_SELECTOR, ".btn.btn--3.btn--white")
    __price_loader = (By.CSS_SELECTOR, "[alt='loadPrice']")

    def is_shopping_cart_page_opened(self):
        element = self.wait_element_is_visible(self.__shopping_cart_screen)
        return element.is_displayed()

    def is_empty_state_shown(self):
        element = self.wait_element_is_visible(self.__back_to_shopping_link)
        return element.is_displayed()

    def input_quantity(self, quantity: int):
        self.clear(self.__quantity_input)
        self.send_keys(self.__quantity_input, quantity)
        return self

    def get_item_price(self):
        return float(self.get_element_attribute_value(self.__quantity_input, "data-price"))

    def get_items_quantity(self):
        return self.get_element_property(self.__quantity_input, "valueAsNumber")

    def click_increase_quantity_button(self):
        self.click(self.__increase_quantity_button)
        return self

    def click_decrease_quantity_button(self):
        self.click(self.__decrease_quantity_button)
        return self

    def click_delete_item_button(self):
        self.click(self.__delete_item_button)
        return self

    def click_delete_all_items_button(self):
        self.click(self.__delete_all_items_button)
        return self

    def get_price_item_times_quantity(self):
        price = self.get_element_property(self.__total_price_for_item, "textContent")
        result = float(price.replace('₴', '').replace(' ', ''))
        return result
