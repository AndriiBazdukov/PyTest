from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.lesson_16_homework_framework.page_objects.base_page import BasePage
from tests.lesson_16_homework_framework.page_objects.shoping_cart_page import ShoppingCartPage


class GoodsDetailsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    __item_details_screen = (By.CSS_SELECTOR, ".p-card")
    __buy_button = (By.CSS_SELECTOR, ".p-buy .p-buy__btn.btn.btn--yellow")
    __navigate_to_characteristics_button = (By.CSS_SELECTOR, ".p-block__row.p-block__row--char .anchor--element")
    __characteristics_block = (By.CSS_SELECTOR, "#CHAR")
    __location_switch_to_list_button = (By.XPATH, "((//*[@class='_HzxbVh'])[2]//*)[1]")
    __location_switch_to_map_button = (By.XPATH, "((//*[@class='_HzxbVh'])[2]//*)[2]")
    __store_location_list_section = (By.CSS_SELECTOR, "._isQdA4")
    __store_location_map = (By.CSS_SELECTOR, "._OwX3Bl._ls5HUK")
    __add_to_compare_button = (By.CSS_SELECTOR, ".link.link--blue.link--inverted.p-buy__link:nth-child(2)")
    __add_to_wishes_button = (By.CSS_SELECTOR, ".link.link--blue.link--inverted.p-buy__link:nth-child(1)")
    __compare_counter = (By.CSS_SELECTOR, ".header__compare-link-counter")

    def is_item_details_page_opened(self):
        element = self.wait_element_is_visible(self.__item_details_screen)
        return element.is_displayed()

    def is_compare_counter_shown(self):
        try:
            self.wait_element_is_visible(self.__compare_counter)
            return True
        except NoSuchElementException:
            return False

    def click_buy_button(self):
        self.click(self.__buy_button)
        return ShoppingCartPage(self.driver)

    def click_add_to_compare_button(self):
        self.click(self.__add_to_compare_button)
        return self

    def click_add_to_wishes_button(self):
        self.click(self.__add_to_wishes_button)
        return self

    def click_switch_to_map_button(self):
        self.click(self.__location_switch_to_map_button)
        return self

    def click_char_button(self):
        self.click(self.__navigate_to_characteristics_button)
        return self

    def is_char_block_in_view(self):
        return self.is_element_in_view(self.__characteristics_block)

    def is_store_list_shown(self):
        element = self.wait_element_is_visible(self.__store_location_list_section)
        return element.is_displayed()

    def is_store_map_shown(self):
        element = self.wait_element_is_visible(self.__store_location_map)
        return element.is_displayed()
