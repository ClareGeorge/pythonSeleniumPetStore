from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


from pageobjects.SearchProductsPage import SearchProductsPage


class SignInPage:

    username_textbox = (By.XPATH, "//input[@name='username']")
    password_textbox = (By.XPATH, "//input[@name='password']")
    submit_button = (By.CSS_SELECTOR, "input[name='signon']")
    signonfail_msg = (By.XPATH, "//ul/li[text()='Invalid username or password.  Signon failed.']")
    signonsuccess_msg = (By.CSS_SELECTOR, "div#WelcomeContent")
    registernow_link = (By.XPATH, "//a[@href='/actions/Account.action?newAccountForm=']")

    def __init__(self, driver):
        self.driver = driver

    def signinUsing(self, username, password):

        self.driver.find_element(*SignInPage.username_textbox).clear()
        self.driver.find_element(*SignInPage.username_textbox).send_keys(username)
        self.driver.find_element(*SignInPage.password_textbox).clear()
        self.driver.find_element(*SignInPage.password_textbox).send_keys(password)
        self.driver.find_element(*SignInPage.submit_button).click()
        success = expected_conditions.visibility_of_element_located(SignInPage.signonsuccess_msg)
        fail = expected_conditions.visibility_of_element_located(SignInPage.signonfail_msg )
        wait = WebDriverWait(self.driver,10).until(expected_conditions.any_of(*[success,fail]))

        if  isinstance(wait, WebElement) :
            if "Welcome" in wait.text:
                print("Login is success")
                return Ca
            elif "Signon failed" in wait.text:
                print("login failed")
                self.driver.find_element(*SignInPage.registernow_link).click()
                return "fail"


