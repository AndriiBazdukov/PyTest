from sqlite3 import OperationalError
import pytest


@pytest.fixture
def setup_data(company_repo):
    company_repo.drop_all_tables()
    yield


def test_table_can_be_created(company_repo, setup_data):
    db = company_repo
    db.create_table()
    assert db.table_exists()


def test_table_can_be_deleted(company_repo, setup_data):
    db = company_repo
    db.create_table()
    db.delete_table()
    assert not db.table_exists()


def test_cant_insert_table_with_name_that_exists(company_repo, setup_data):
    db = company_repo
    db.create_table()
    try:
        db.create_table()
        assert False
    except OperationalError:
        assert True


def test_spaces_not_allowed_in_table_name(company_repo, setup_data):
    name = "Test name"
    db = company_repo
    try:
        db.create_table(name)
        assert False
    except OperationalError:
        assert True


def test_record_can_be_inserted(company_repo, fake_product, setup_data):
    db = company_repo
    db.create_table()
    db.insert_one(**fake_product)
    result = db.get_all()
    assert len(result) == 1


def test_record_can_be_updated(company_repo, faker, fake_product, setup_data):
    new_name = faker.last_name()
    db = company_repo
    employee_data = fake_product

    db.create_table()
    db.insert_one(**employee_data)
    employee_data["name"] = new_name
    db.update_record_by_id(**employee_data, record_id=1)

    result = db.get_one_by_id(1)
    assert result[1] == new_name


def test_record_can_be_deleted(company_repo, fake_product, setup_data):
    db = company_repo
    db.create_table()
    db.insert_one(**fake_product)
    db.delete_record_by_id(1)
    result = db.get_all()
    assert len(result) == 0
