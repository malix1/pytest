from test import func
import pytest
import sys

"""
 -x => exit test if there is failed test
 -maxfail="number" => exit test if there is more than maxfail
 -m "mark_name" => just run test that test mark name is mark_name
 -k "name" => run test that name includes "name"
 --tb=no => removes the track state of failed tests
 -s, --capture=no => run the print statements
 -v => give detail info of tests
 -q => just shows the passed and failed test numbers and execution time

"""
###
###


@pytest.mark.parametrize("arg1, arg2, result", [
    (7, 3, 10),
    ("hello", "world", "helloworld"),
    (10.5, 10.5, 21)
])
def test_add_parms(arg1, arg2, result):
    assert func.add(arg1, arg2) == result


@pytest.mark.skipif(sys.version_info > (3, 9), reason="version is bigger than python 3.9")
def test_add():
    assert func.add(7, 3) == 10
    assert func.add(6) == 8


@pytest.mark.number
def test_product():
    assert func.product(7, 3) == 21
    assert func.product(6) == 12


@pytest.mark.string
def test_add_string():
    assert func.add("hello", "world") == "helloworld"
