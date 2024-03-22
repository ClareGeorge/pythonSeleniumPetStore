from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.SignInPage import SignInPage


class RegistrationPage:

    userid_textbox = (By.XPATH, "//input[@name='username']")
    password_textbox = (By.XPATH, "//input[@name='password']")
    repeatedPassword_textbox = (By.XPATH, "//input[@name='repeatedPassword']")
    repeatedPassword_textbox = (By.XPATH, "//input[@name='repeatedPassword']")
    firstName_textbox = (By.XPATH, "//input[@name='account.firstName']")
    lastName_textbox = (By.XPATH, "//input[@name='account.lastName']")
    email_textbox = (By.XPATH, "//input[@name='account.email']")
    phone_textbox = (By.XPATH, "//input[@name='account.phone']")
    address1_textbox = (By.XPATH, "//input[@name='account.address1']")
    address2_textbox = (By.XPATH, "//input[@name='account.address2']")
    city_textbox = (By.XPATH, "//input[@name='account.city']")
    state_textbox = (By.XPATH, "//input[@name='account.state']")
    zip_textbox = (By.XPATH, "//input[@name='account.zip']")
    country_textbox = (By.XPATH, "//input[@name='account.country']")
    country_textbox = (By.XPATH, "//input[@name='account.country']")
    language_dropdown = (By.XPATH, "//select[@name='account.languagePreference']")
    favourite_dropdown = (By.XPATH, "//select[@name='account.favouriteCategoryId']")
    listOption_checkbox = (By.XPATH, "//input[@name='account.listOption']")
    bannerOption_checkbox  = (By.XPATH, "//input[@name='account.bannerOption']")
    submit_button = (By.XPATH, "//input[@name='newAccount']")
    signin_url = (By.XPATH, "//a[text()='Sign In' and contains(@href,'/actions/Account.')]")





    def __init__(self,driver):
        self.driver = driver
    def registerUserWith(self, user_data):
        self.driver.find_element(*RegistrationPage.userid_textbox).send_keys(user_data["user_id"])
        self.driver.find_element(*RegistrationPage.password_textbox).send_keys(user_data["new_password"])
        self.driver.find_element(*RegistrationPage.repeatedPassword_textbox).send_keys(user_data["new_password"])
        self.driver.find_element(*RegistrationPage.firstName_textbox).send_keys(user_data["first_name"])
        self.driver.find_element(*RegistrationPage.lastName_textbox).send_keys(user_data["last_name"])
        self.driver.find_element(*RegistrationPage.email_textbox).send_keys(user_data["email"])
        self.driver.find_element(*RegistrationPage.phone_textbox).send_keys(user_data["phone"])
        self.driver.find_element(*RegistrationPage.address1_textbox).send_keys(user_data["address1"])
        self.driver.find_element(*RegistrationPage.address2_textbox).send_keys(user_data["address2"])
        self.driver.find_element(*RegistrationPage.city_textbox).send_keys(user_data["city"])
        self.driver.find_element(*RegistrationPage.state_textbox).send_keys(user_data["state"])
        self.driver.find_element(*RegistrationPage.zip_textbox).send_keys(user_data["zip"])
        self.driver.find_element(*RegistrationPage.country_textbox).send_keys(user_data["country"])
        Select(self.driver.find_element(*RegistrationPage.language_dropdown)).select_by_visible_text("english")
        Select(self.driver.find_element(*RegistrationPage.favourite_dropdown)).select_by_visible_text("FISH")
        self.driver.find_element(*RegistrationPage.listOption_checkbox).click()
        self.driver.find_element(*RegistrationPage.bannerOption_checkbox).click()

        self.driver.find_element(*RegistrationPage.submit_button).click()
        self.driver.find_element(*RegistrationPage.signin_url).click()
        return SignInPage(self.driver)




