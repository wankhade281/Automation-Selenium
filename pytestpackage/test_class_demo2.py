import pytest

from pytestpackage.class_to_test import SomeClassToTest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)  # autouse=True is use to available a fixtures throughout(scope) of class
    def classSetup(self, oneTimeSetUp):
        self.c = SomeClassToTest(self.value)

    def test_methodA(self, classSetup):
        result = self.c.sumNumbers(2,3)
        assert result == 15
        print(result)
        print("Running method A")

    def test_methodB(self):
        print("Running method B")
