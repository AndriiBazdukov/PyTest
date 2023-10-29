from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from tests.lesson_16_homework_framework.page_objects.base_page import BasePage
from tests.lesson_16_homework_framework.utilities.waiter import wait_until


class RegistrationPage:
    def __init__(self, driver):
        self.base_page = BasePage(driver)

    __phone_registration_input = (By.CSS_SELECTOR, "#PERSONAL_PHONE")
    __name_registration_input = (By.CSS_SELECTOR, "#NAME")
    __password_registration_input = (By.CSS_SELECTOR, "#PASSWORD")
    __confirm_password_registration_input = (By.CSS_SELECTOR, "#CONFIRM_PASSWORD")
    __email_registration_input = (By.CSS_SELECTOR, "#EMAIL")
    __captcha_registration_input = (By.CSS_SELECTOR, "[name='captcha_word']")
    __submit_registration_button = (By.CSS_SELECTOR, "#submit_input")
    __password_validation_helper_section = (By.CSS_SELECTOR, ".input-wrapper__password-validate")
    __password_validation_helper_length = (By.CSS_SELECTOR, "[class*='password-validate-item input']:nth-child(1)")
    __password_validation_helper_capital = (By.CSS_SELECTOR, "[class*='password-validate-item input']:nth-child(2)")
    __password_validation_helper_digits = (By.CSS_SELECTOR, "[class*='password-validate-item input']:nth-child(3)")
    __password_all_validation_helpers = (By.CSS_SELECTOR, ".input-wrapper__password-validate-list>li")
    __password_validation_helper_special_symbols = \
        (By.CSS_SELECTOR, "[class*='password-validate-item input']:nth-child(4)")

    def click_password_input(self):
        self.base_page.click(self.__password_registration_input)
        return self

    def click_submit(self):
        self.base_page.click(self.__submit_registration_button)
        return self

    def is_password_helper_section_shown(self):
        try:
            self.base_page.wait_element_is_visible(self.__password_validation_helper_section, 1)
            return True
        except TimeoutException:
            return False

    def input_password(self, password):
        self.base_page.send_keys(self.__password_registration_input, password)
        return self

    def input_phone(self, password):
        self.base_page.send_keys(self.__phone_registration_input, password)
        return self

    def input_password_confirmation(self, password):
        self.base_page.send_keys(self.__confirm_password_registration_input, password)
        return self

    def input_name(self, password):
        self.base_page.send_keys(self.__name_registration_input, password)
        return self

    def input_email(self, password):
        self.base_page.send_keys(self.__email_registration_input, password)
        return self

    def input_captcha(self, password):
        self.base_page.send_keys(self.__captcha_registration_input, password)
        return self

    def is_password_validation_line_successful(self, line_index: int):
        wait_until(lambda: len(self.base_page.get_elements_list(self.__password_all_validation_helpers)) == 4)
        els = self.base_page.get_elements_list(self.__password_all_validation_helpers)
        if 0 <= line_index < len(els):
            attribute_class = els[line_index].get_attribute("class")
            if attribute_class.endswith("success"):
                return True
        return False
