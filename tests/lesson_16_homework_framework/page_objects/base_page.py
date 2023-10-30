from random import Random

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_is_visible(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def is_element_in_view(self, element_locator):
        try:
            wait = WebDriverWait(self.driver, 2)
            element = wait.until(EC.visibility_of_element_located(element_locator))
            return element.is_displayed()
        except Exception as e:
            return False

    def wait_element_is_clickable(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator)
        el.send_keys(value)

    def click(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.click()

    def clear(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.clear()

    def is_element_displayed(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.is_displayed()

    def get_element_attribute_value(self, locator: tuple, attribute: str):
        element = self.wait_element_is_visible(locator)
        value = element.get_attribute(attribute)
        return value

    def get_element_text_content_property(self, locator: tuple):
        element = self.wait_element_is_visible(locator)
        value = element.get_property("textContent")
        return value

    def get_element_property(self, locator: tuple, el_property):
        element = self.wait_element_is_visible(locator)
        value = element.get_property(el_property)
        return value

    def click_on_random_element_from_list(self, locator: tuple):
        self.wait_element_is_visible(locator)
        els = self.driver.find_elements(*locator)
        if len(els) == 0:
            raise NoSuchElementException()
        random = Random()
        random.choice(els).click()

    def get_elements_list(self, locator: tuple):
        self.wait_element_is_visible(locator)
        els = self.driver.find_elements(*locator)
        if len(els) == 0:
            raise NoSuchElementException()
        return els
