import pytest
from constants import ROOT_PATH
from tests.lesson_23_homework_db.company_repo import CompanyRepo


@pytest.fixture(scope='module')
def company_repo():
    return CompanyRepo(f"{ROOT_PATH}\\tests\\lesson_23_homework_db\\db\\my.db")


@pytest.fixture()
def fake_product(faker):
    data = {
        "name": faker.first_name(),  # Didn't find fake product
        "quantity": faker.pyint(0, 60),
        "description": faker.text(50),
        "price": float(faker.pyint(0, 60000))
    }
    return data
