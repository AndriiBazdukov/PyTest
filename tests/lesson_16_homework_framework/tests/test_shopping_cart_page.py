import pytest

from tests.lesson_16_homework_framework.utilities.waiter import wait_until


@pytest.mark.regress
def test_shopping_cart_empty_state(open_main_page):
    shopping_cart_page = open_main_page.click_shopping_cart_button()
    assert shopping_cart_page.is_empty_state_shown(), "Empty state message not shown"


@pytest.mark.smoke
@pytest.mark.regress
def test_user_can_delete_item_from_cart(open_shopping_cart_with_item):
    shopping_cart = open_shopping_cart_with_item.click_delete_item_button()
    assert shopping_cart.is_empty_state_shown(), "Item is not deleted"


@pytest.mark.regress
def test_quantity_increased_by_1_when_increase_button_clicked(open_shopping_cart_with_item):
    cart = open_shopping_cart_with_item.click_increase_quantity_button()
    assert cart.get_items_quantity() == 2, "Item quantity is not increased"


@pytest.mark.regress
def test_user_can_decrease_quantity(open_shopping_cart_with_item):
    cart = open_shopping_cart_with_item.click_increase_quantity_button().click_increase_quantity_button()
    cart.click_decrease_quantity_button()
    assert cart.get_items_quantity() == 2, "Wrong item quantity"


@pytest.mark.regress
def test_total_amount(open_shopping_cart_with_item, random):
    quantity = random.randint(2, 5)
    cart = open_shopping_cart_with_item.input_quantity(quantity)
    item_price = cart.get_item_price()
    assert wait_until(lambda: cart.get_price_item_times_quantity() == item_price * quantity, timeout=10,
                      error_msg=f"Total is wrong: expected {item_price * quantity}, "
                                f"found {cart.get_price_item_times_quantity()}")


