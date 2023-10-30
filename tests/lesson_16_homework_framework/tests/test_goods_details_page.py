import pytest


@pytest.mark.smoke
@pytest.mark.regress
def test_buy_button_transfers_to_cart(open_random_item_details):
    shopping_cart = open_random_item_details.click_buy_button()
    assert shopping_cart.is_shopping_cart_page_opened(), "Shopping cart is not opened"


@pytest.mark.regress
@pytest.mark.skip(reason="Test is Falls-positive")
def test_navigation_to_char_section(open_random_item_details):
    assert open_random_item_details.click_char_button().is_char_block_in_view(), "Characteristics block not in view"


@pytest.mark.regress
def test_store_list_shown_by_default(open_random_item_details):
    item_details = open_random_item_details
    assert item_details.is_store_list_shown(),  "Store list is not shown"


@pytest.mark.regress
def test_user_can_open_store_map(open_random_item_details):
    item_details = open_random_item_details.click_switch_to_map_button()
    assert item_details.is_store_map_shown(),  "Store map is not shown"


@pytest.mark.regress
def test_user_can_add_item_to_compare(open_random_item_details):
    assert open_random_item_details.click_add_to_compare_button().is_compare_counter_shown(), "Counter not shown"
    