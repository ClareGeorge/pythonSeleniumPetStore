from selenium.webdriver.common.by import By

from pageobjects.MyOrders import MyOrders


class MyAccountPage:

    myorders_link = (By.XPATH, "//a[@href='/actions/Order.action?listOrders=']")
    def __init__(self, driver):
        self.driver= driver

    def navigateToMyOrders(self):
        self.driver.find_element(*MyAccountPage.myorders_link).click()
        return MyOrders(self.driver)