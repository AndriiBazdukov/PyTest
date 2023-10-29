import pytest

from tests.lesson_16_homework_framework.utilities.waiter import wait_until


@pytest.mark.regress
def test_close_icon_login_page(open_login_page):
    main_page = open_login_page.click_close_icon()
    assert main_page.is_main_page_opened(), "User is not redirected to main page when login pop up is closed"


@pytest.mark.regress
def test_warning_message_is_shown_when_credentials_empty(open_login_page):
    login_page = open_login_page
    login_page.click_submit_button()
    assert login_page.is_warning_message_shown(), "Warning message is not displayed"


@pytest.mark.regress
def test_warning_message_is_shown_when_credentials_incorrect(open_login_page, random):
    login_page = open_login_page
    random_value = random.randint(10**9, (10**10)-1)
    login_page.log_in(random_value, str(random_value))
    assert login_page.is_warning_message_shown(), "Warning message is not displayed"


@pytest.mark.smoke
@pytest.mark.regress
def test_successful_log_in(open_login_page, configs):
    main_page = open_login_page.log_in(configs.login, configs.password)
    assert wait_until(lambda: main_page.get_user_displayed_name() not in ("Увійти", "Войти"),
                      error_msg='User name is not found')


@pytest.mark.regress
def test_user_can_unhide_password(open_login_page):
    login_page = open_login_page
    assert login_page.is_password_hidden(), "Password field should be in hidden state by default"
    assert not login_page.click_hide_show_password_icon().is_password_hidden(), "Password should be shown"


