import inspect
import logging

import pytest

from pageobjects.CatalogPage import CatalogPage
from pageobjects.HomePage import HomePage
from pageobjects.RegistrationPage import RegistrationPage

from testdata.TestData import TestData
from utilities.BaseClass import BaseClass


class TestLoginPage(BaseClass):
    def test_CreateUser(self,getTestData):

        log = BaseClass.getLogger(self.filehandler)
        self.driver.refresh()

        home_page = HomePage(self.driver)
        signin_page = home_page.navigateToHomePage(getTestData["petstore_url"])
        log.info("Navigated to page " + getTestData["petstore_url"] )

        result = signin_page.signinUsing(getTestData["user_name"],getTestData["password"])
        if result == "success":
            searchproduct_page =CatalogPage(self.driver)
        elif result == "fail":
            register_page = RegistrationPage(self.driver)
            signin_page = register_page.registerUserWith(getTestData)
            signin_page.signinUsing(getTestData["user_name"],getTestData["password"])

        log.removeHandler(log.handlers[0])



@pytest.fixture(params =TestData.getTestData("test_CreateUser"))
def getTestData(request):
    return request.param