from selenium.webdriver.common.by import By

from pageobjects.OrderConfirmationPage import OrderConfirmationPage


class ConfirmOrderPage:

    confirm_link = (By.XPATH, "//a[@href='/actions/Order.action?newOrder=&confirmed=true']")

    def __init__(self,driver):
        self.driver = driver

    def confirmOrder(self):
        self.driver.find_element(*ConfirmOrderPage.confirm_link).click()
        return OrderConfirmationPage(self.driver)


