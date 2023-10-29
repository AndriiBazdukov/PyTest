from selenium.webdriver.common.by import By
from tests.lesson_16_homework_framework.page_objects.base_page import BasePage
from tests.lesson_16_homework_framework.page_objects.main_page import MainPage
from tests.lesson_16_homework_framework.page_objects.registration_page import RegistrationPage


class LoginPage:
    def __init__(self, driver):
        self.base_page = BasePage(driver)

    __login_pop_up = (By.CSS_SELECTOR, "#popup-login")
    __close_icon = (By.CSS_SELECTOR, "[class*='fancybox-close-small']")
    __restore_password_link = (By.CSS_SELECTOR, ".anchor--element")
    __login_input = (By.CSS_SELECTOR, "#user_login")
    __password_input = (By.CSS_SELECTOR, "#user_pass")
    __submit_button = (By.CSS_SELECTOR, "[type='submit']")
    __hide_password_icon = (By.CSS_SELECTOR, ".input-wrapper__show-password")
    __google_login_link = (By.CSS_SELECTOR, ".social-enter__item")
    __registration_link = (By.CSS_SELECTOR, ".popup-auth__footer .link.link--big.link--inverted")
    __remember_me_checkbox = (By.CSS_SELECTOR, ".checkbox__input")
    __warning_message = (By.CSS_SELECTOR, ".animated.zoomIn.auth-error-message")

    def is_login_page_opened(self):
        element = self.base_page.wait_element_is_visible(self.__login_pop_up)
        return element.is_displayed()

    def click_close_icon(self):
        self.base_page.click(self.__close_icon)
        return MainPage(self.base_page.driver)

    def click_registration_link(self):
        self.base_page.click(self.__registration_link)
        return RegistrationPage(self.base_page.driver)

    def click_submit_button(self):
        self.base_page.click(self.__submit_button)
        return MainPage(self.base_page.driver)

    def click_restore_password_button(self):
        self.base_page.click(self.__restore_password_link)

    def is_warning_message_shown(self):
        element = self.base_page.wait_element_is_visible(self.__warning_message)
        return element.is_displayed()

    def enter_user_login(self, login):
        self.base_page.send_keys(self.__login_input, login)
        return self

    def enter_user_password(self, password):
        self.base_page.send_keys(self.__password_input, password)
        return self

    def log_in(self, login, password):
        self.enter_user_login(login)
        self.enter_user_password(password)
        self.click_submit_button()
        return MainPage(self.base_page.driver)

    def click_hide_show_password_icon(self):
        self.base_page.click(self.__hide_password_icon)
        return self

    def is_password_hidden(self):
        if self.base_page.get_element_attribute_value(self.__password_input, "type") == "password":
            return True
        else:
            return False
