import pytest


@pytest.yield_fixture()
def setUp():
    print("Running conftest demo method setUp")
    yield
    print("Running conftest demo method tearDown")


# @pytest.yield_fixture(scope="module")
# def oneTimeSetUp():
#     print("Running oneTimeSetUp")
#     yield
#     print("Running oneTimeTearDown")


#  used for test_command_line_args.py
@pytest.yield_fixture(scope="class")  # For particular module(ex test_case_demo1.py) use scope='module'
# for  particular class use scope='class'
def oneTimeSetUp(request,browser):
    print("Running oneTimeSetUp")
    if browser == 'firefox':
        print("Running Test on Firefox")
        value = 10
    else:
        value = 20
        print("Running Test on Chrome")
    if request.cls is not None:
        request.cls.value = value
    yield value
    print("Running oneTimeTearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operations")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
