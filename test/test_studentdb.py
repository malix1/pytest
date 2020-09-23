import pytest
from Databases.StudentDB import StudentDB


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


""" @pytest.fixture(scope="module")
def db():
    print("\nconnecting db")
    db = StudentDB()
    db.connect("data.json")
    yield db
    db.close() """

""" 
@pytest.fixture(scope="module")
def db2(request):
    db = StudentDB()
    db.connect("data.json")

    def fin():
        db.close()
    request.addfinalizer(fin)
    return db
 """

# if your fixtures in conftest.py file you dont need to import pytest
# auto detects and use it
#  if you make scope module, it runs for every file
# if you make scope session, it runs just one time


def test_ali_data(db):
    student_data = db.get_data("ali")
    assert student_data["name"] == "ali"
