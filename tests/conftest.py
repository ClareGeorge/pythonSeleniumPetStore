import logging

import pytest
from selenium import webdriver

browser_driver = filehandler = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default = "chrome",
        help = "only 2 options : chrome or edge"
    )


def pytest_collection_modifyitems(config, items):
    # called after collection is completed
    # you can modify the ``items`` list

    print(items)

@pytest.fixture(scope="class")
def initial_setup(request):
    global filehandler
    filehandler = logging.FileHandler("C:\\2.Code\\PythonSelenium\\pythonProjectPetStore\\logs\\logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    request.cls.filehandler = filehandler

    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser_driver = webdriver.Chrome()
    elif browser_name == "edge":
        browser_driver = webdriver.Edge()

    browser_driver.implicitly_wait(5)
    browser_driver.maximize_window()

    request.cls.driver = browser_driver
    yield
    browser_driver.close()
