import pytest
from StudentDB import StudentDB

@pytest.fixture(scope="session")
def db():
    print("\nconnecting db")
    db = StudentDB()
    db.connect("data.json")
    yield db
    db.close()