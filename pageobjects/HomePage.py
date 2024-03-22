from time import sleep

from selenium.webdriver.common.by import By

from pageobjects.SignInPage import SignInPage


class HomePage:

    enterstore_url = (By.XPATH, "//a[@href='actions/Catalog.action']")
    signin_url = (By.XPATH, "//a[text()='Sign In' and contains(@href,'/actions/Account.')]")

    def __init__(self, driver):
        self.driver = driver

    def navigateToHomePage(self, petstore_url):
        self.driver.get(petstore_url)
        self.driver.find_element(*HomePage.enterstore_url).click()
        self.driver.find_element(*HomePage.signin_url).click()
        sleep(1)
        return SignInPage(self.driver)


