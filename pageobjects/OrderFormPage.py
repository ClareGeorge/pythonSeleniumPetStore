from selenium.webdriver.common.by import By

from pageobjects.ConfirmOrderPage import ConfirmOrderPage


class OrderFormPage:
    continue_button = (By.XPATH, "//input[@name='newOrder']")

    def __init__(self, driver):
        self.driver = driver

    def continueOrder(self):
        self.driver.find_element(*OrderFormPage.continue_button).click()
        return ConfirmOrderPage(self.driver)

