import json
from random import Random
import pytest
from tests.lesson_16_homework_framework.constants import ROOT_PATH
from tests.lesson_16_homework_framework.page_objects.main_page import MainPage
from tests.lesson_16_homework_framework.utilities.dict_to_class import DictToClass
from tests.lesson_16_homework_framework.utilities.driver_factory import DriverFactory


@pytest.fixture
def configs():
    with open(f"{ROOT_PATH}\\configs\\config.json") as file:
        conf_dict = json.load(file)
        return DictToClass(**conf_dict)


@pytest.fixture
def create_driver(configs):
    driver = DriverFactory(configs.browser).get_driver()
    driver.maximize_window()
    driver.get(configs.url)
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(create_driver):
    return MainPage(create_driver)


@pytest.fixture
def open_login_page(open_main_page):
    login_page = open_main_page.click_login_opener_button()
    return login_page


@pytest.fixture
def open_registration_page(open_login_page):
    registration = open_login_page.click_registration_link()
    return registration


@pytest.fixture
def open_random_item_details(open_main_page):
    goods_details = open_main_page.click_on_random_item_on_sale()
    return goods_details


@pytest.fixture
def open_shopping_cart_with_item(open_random_item_details):
    shopping_cart = open_random_item_details.click_buy_button()
    return shopping_cart


@pytest.fixture
def random():
    random = Random()
    return random


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )
    config.addinivalue_line(
        "markers", "regress: mark test regress"
    )