import pytest

from tests.lesson_20_homework_api_testing.api_collections.apis.users_api import UsersApi
from tests.lesson_20_homework_api_testing.api_collections.data.data_generator import DataGenerator


def test_post_new_user(get_auth_token, get_static_user):
    user_api = UsersApi()
    resp = user_api.post_new_user(user_data=get_static_user)
    if resp.status_code == 201:
        assert True
    elif resp.json()["message"] == "An account already exists with the same email address":
        user_api.delete_user(get_auth_token)
        resp = user_api.post_new_user(user_data=get_static_user)
        assert resp.status_code == 201


def test_login_user(get_static_creds):
    user_api = UsersApi()
    resp = user_api.post_login_user(user_data=get_static_creds)
    assert len(resp.json()["data"]["token"]) == 64


def test_user_can_update_name_in_profile(get_auth_token, random):
    auth_token = get_auth_token
    name = DataGenerator.get_string_of_length(length=random.randint(4, 30))
    user_api = UsersApi()
    user_api.patch_update_user_profile(auth_token, UsersApi.update_profile_data(name=name))
    new_name = user_api.get_user_profile(auth_token).json()["data"]["name"]
    assert new_name == name


@pytest.mark.parametrize("start, stop", [(1, 3), (31, 33)])
def test_user_name_field_validation(get_auth_token, random, start, stop):
    auth_token = get_auth_token
    name = DataGenerator.get_string_of_length(length=random.randint(start, stop))
    user_api = UsersApi()
    resp = user_api.patch_update_user_profile(auth_token, UsersApi.update_profile_data(name=name)).json()
    assert resp["message"] == "User name must be between 4 and 30 characters"


def test_user_can_update_phone_in_profile(get_auth_token, random):
    auth_token = get_auth_token
    phone = str(random.randint(10 ** 7, (10 ** 20) - 1))
    user_api = UsersApi()
    user_api.patch_update_user_profile(auth_token, UsersApi.update_profile_data(phone=phone))
    new_phone = user_api.get_user_profile(auth_token).json()["data"]["phone"]
    assert new_phone == phone


def test_phone_field_can_not_accept_letters(get_auth_token, random):
    auth_token = get_auth_token
    user_api = UsersApi()
    resp = user_api.patch_update_user_profile(auth_token,
                                              UsersApi.update_profile_data(phone="Some text of proper length")).json()
    assert resp["message"] == "Phone number should be between 8 and 20 digits"


def test_user_can_update_company_in_profile(get_auth_token, random):
    auth_token = get_auth_token
    company = DataGenerator.get_string_of_length(length=random.randint(4, 30))
    user_api = UsersApi()
    user_api.patch_update_user_profile(auth_token, UsersApi.update_profile_data(company=company))
    new_company = user_api.get_user_profile(auth_token).json()["data"]["company"]
    assert new_company == company


@pytest.mark.parametrize("start, stop", [(1, 3), (31, 33)])
def test_user_company_field_validation(get_auth_token, random, start, stop):
    auth_token = get_auth_token
    company = DataGenerator.get_string_of_length(length=random.randint(start, stop))
    user_api = UsersApi()
    resp = user_api.patch_update_user_profile(auth_token, UsersApi.update_profile_data(company=company)).json()
    assert resp["message"] == "Company name must be between 4 and 30 characters"


def test_logout(get_auth_token):
    auth_token = get_auth_token
    user_api = UsersApi()
    resp_before = user_api.get_user_profile(auth_token)
    assert resp_before.status_code == 200
    user_api.delete_current_session(auth_token)
    resp_after = user_api.get_user_profile(auth_token).json()
    assert resp_after["message"] == "Access token is not valid or has expired, you will need to login"


def test_delete_user(get_auth_token, get_static_creds):
    auth_token = get_auth_token
    user_api = UsersApi()
    user_api.delete_user(auth_token)
    result = user_api.post_login_user(get_static_creds).json()
    assert result["message"] == "Incorrect email address or password"
