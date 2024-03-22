from selenium.webdriver.common.by import By

from pageobjects.ShoppingCartPage import ShoppingCartPage


class ViewItemPage:

    item_name_text = (By.XPATH, "//tr[3]/td")
    item_add2cart_link = (By.XPATH, "//tr[7]/td/a[text()='Add to Cart']")
    backtoitem_link = (By.XPATH, "//div[@id='BackLink']/a")

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element(*ViewItemPage.item_add2cart_link).click()
        return ShoppingCartPage(self.driver)