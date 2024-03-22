from selenium.webdriver.common.by import By

from pageobjects.SignOut import SignOut


class MyOrders:


    orderid_links = (By.XPATH, "//tr/td[1]/a")
    def __init__(self,driver):
        self.driver = driver
    def verifyOrder(self, order_no_str):
        all_order_id_links= self.driver.find_elements(*MyOrders.orderid_links)
        for an_order_id_link in all_order_id_links:
            if an_order_id_link.text == order_no_str:
                assert 1
                break
        return SignOut(self.driver)






