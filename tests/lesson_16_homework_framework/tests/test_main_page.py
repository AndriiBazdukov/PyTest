import pytest


@pytest.mark.regress
def test_login_button(open_main_page):
    login_page = open_main_page.click_login_opener_button()
    assert login_page.is_login_page_opened(), "Login page is not opened"


@pytest.mark.regress
def test_wishes_button_redirects_to_login_when_unauthorized(open_main_page):
    login_page = open_main_page.click_login_opener_button()
    assert login_page.is_login_page_opened(), "Login page is not opened"


@pytest.mark.regress
def test_warning_is_shown_when_empty_compare_clicked(open_main_page):
    assert open_main_page.click_compare_button().is_warning_displayed(), "Warning is not displayed"


@pytest.mark.regress
def test_click_on_item_opens_details(open_main_page):
    details_page = open_main_page.click_on_random_item_on_sale()
    assert details_page.is_item_details_page_opened(), "Item details is not opened"


@pytest.mark.smoke
@pytest.mark.regress
def test_click_on_purchase_item_redirects_to_cart(open_main_page):
    shopping_cart = open_main_page.click_purchase_on_random_item_on_sale()
    assert shopping_cart.is_shopping_cart_page_opened(), "Cart is not opened"

