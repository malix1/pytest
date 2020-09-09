import pytest
from StudentDB import StudentDB


"""
db = None

# runs before test
def setup_module(module):
    global db
    db = StudentDB()
    db.connect("data.json")

# runs after test
def teardown_module(module):
    db.close() 
"""


@pytest.fixture(scope="module")
def db():
    print("\nconnecting db")
    db = StudentDB()
    db.connect("data.json")
    yield db
    db.close()


def test_ali_data(db):
    student_data = db.get_data("ali")
    assert student_data["name"] == "ali"
