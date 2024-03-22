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
        while result == "fail":
            signin_page = RegistrationPage(self.driver).registerUserWith(getTestData)
            result = signin_page.signinUsing(getTestData["user_name"], getTestData["password"])
        else:
            if result  == "success":
                category_page = CatalogPage(self.driver).selectCategory(getTestData["category"])
                product_page = category_page.selectProduct(getTestData["product"])
                item_page = product_page.selectItem(getTestData["item"])
                shoppingcart_page = item_page.addToCart()
                orderform_page = shoppingcart_page.proceedToCheckout()
                confirmorder_page = orderform_page.continueOrder()
                orderconfirmation_page = confirmorder_page.confirmOrder()
                myaccount_page , order_no_str = orderconfirmation_page.verifyOrderDetails()
                myorders_page = myaccount_page.navigateToMyOrders()
                signout = myorders_page.verifyOrder(order_no_str )
                log.info( "Order " + order_no_str + " has been placed")
                signout.signOff()
                log.info("customer " + getTestData["user_name"] + " has been signed out" )





        log.removeHandler(log.handlers[0])



@pytest.fixture(params =TestData.getTestData("test_CreateUser"))
def getTestData(request):
    return request.param