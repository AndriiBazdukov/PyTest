from locators import Locators
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


def test_locators():
    locators_inst = Locators()
    driver = Chrome()
    driver.get(locators_inst.page_URL)
    driver.maximize_window()
    sleep(2)

    for key in dir(locators_inst):
        if key.startswith("xpath"):
            value = getattr(locators_inst, key)
            element = driver.find_element(By.XPATH, value)
            assert element.is_displayed(), F"{key} is not found"

            elements = driver.find_elements(By.XPATH, value)
            assert len(elements) == 1

        if key.startswith("css"):
            value = getattr(locators_inst, key)
            element = driver.find_element(By.CSS_SELECTOR, value)
            assert element.is_displayed(), F"{key} is not found"

            elements = driver.find_elements(By.CSS_SELECTOR, value)
            assert len(elements) == 1
