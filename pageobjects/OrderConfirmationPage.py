from selenium.webdriver.common.by import By

from pageobjects.MyAccountPage import MyAccountPage


class OrderConfirmationPage:
    order_no_str =""
    confirmation_msg_text = (By.XPATH, "//ul[@class='messages']/li")
    order_no_text = (By.XPATH, "//tr/th[1]")
    myaccount_link = (By.XPATH, "//a[@href='/actions/Account.action?editAccountForm=']")

    def __init__(self,driver):
        self.driver = driver
    def verifyOrderDetails(self):
        confirmation_msg = self.driver.find_element(*OrderConfirmationPage.confirmation_msg_text).text
        assert "Thank you" in confirmation_msg
        OrderConfirmationPage.order_no_str = self.driver.find_element(*OrderConfirmationPage.order_no_text).text.split()[1][1:]
        self.driver.find_element(*OrderConfirmationPage.myaccount_link).click()
        return MyAccountPage(self.driver), OrderConfirmationPage.order_no_str

