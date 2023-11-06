from random import Random
import pytest
from faker import Faker
from tests.lesson_20_homework_api_testing.api_collections.apis.users_api import UsersApi


@pytest.fixture()
def get_fake_user_enroll_payload(fake):
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password()
    }


@pytest.fixture()
def get_static_user():
    return {
        "name": "Static User",
        "email": "static@user.com",
        "password": "Staticp0o9P)O()"
    }


@pytest.fixture()
def get_static_creds():
    return {
        "email": "static@user.com",
        "password": "Staticp0o9P)O()"
    }


@pytest.fixture()
def get_auth_token(get_static_creds, get_static_user):
    user_api = UsersApi()
    resp = user_api.post_login_user(user_data=get_static_creds)
    if resp.status_code == 200:
        return resp.json()["data"]["token"]
    else:
        user_api.post_new_user(get_static_user)
        resp = user_api.post_login_user(user_data=get_static_creds)
        return resp.json()["data"]["token"]


@pytest.fixture
def fake():
    fake = Faker()
    return fake


@pytest.fixture
def random():
    random = Random()
    return random
