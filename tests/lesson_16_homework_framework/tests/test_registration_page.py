from time import sleep

import pytest

from tests.lesson_16_homework_framework.utilities.testdata_generator import TestDataGenerator


@pytest.mark.smoke
@pytest.mark.regress
def test_password_helper_section_visibility(open_registration_page):
    registration_page = open_registration_page
    assert not registration_page.is_password_helper_section_shown(), "Password helper section is shown by default"
    registration_page.click_password_input()
    assert registration_page.is_password_helper_section_shown(), "Pass helper section is not shown after click om it"


# 4 Tests here
@pytest.mark.regress
@pytest.mark.parametrize("test_params", TestDataGenerator.testdata_for_password_helpers_check())
def test_password_helpers(open_registration_page, test_params):
    registration_page = open_registration_page.input_password(test_params["password"])
    for success_line in test_params["helpers_successful"]:
        assert registration_page.is_password_validation_line_successful(success_line), "Line is not marked as success"
    for fail_line in test_params["helpers_failed"]:
        assert not registration_page.is_password_validation_line_successful(fail_line), "Line should remain failed"


