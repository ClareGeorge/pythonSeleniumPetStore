from selenium.webdriver.common.by import By

from pageobjects.OrderFormPage import OrderFormPage


class ShoppingCartPage:


    proceedtocheckout_link = (By.XPATH, "//a[@href='/actions/Order.action?newOrderForm=']")

    def __init__(self,driver):
        self.driver = driver
    def proceedToCheckout(self):

        self.driver.find_element(*ShoppingCartPage.proceedtocheckout_link).click()
        return OrderFormPage(self.driver)

