import pytest


@pytest.yield_fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")


def test_demo2_methodA(setUp):
    print("Running demo2 method A")


def test_demo2_methodB(setUp):
    print("Running demo2 method B")