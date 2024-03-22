from selenium.webdriver.common.by import By


class SignOut:
    signoff_link = (By.PARTIAL_LINK_TEXT, "Sign Out")

    def __init__(self, driver):
        self.driver = driver
    def signOff(self):
        self.driver.find_element(*SignOut.signoff_link).click()
