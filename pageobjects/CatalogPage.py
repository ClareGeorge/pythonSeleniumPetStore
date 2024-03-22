from time import sleep

from selenium.webdriver.common.by import By

from pageobjects.ViewCategoryPage import ViewCategoryPage


class CatalogPage:

    signoff_link = (By.PARTIAL_LINK_TEXT, "Sign Out")
    category_id = ""




    def __init__(self, driver):
        self.driver = driver


    def selectCategory(self, category):
        global category_id
        category_id = category.upper()
        category_link = (By.XPATH, "//div[@id='SidebarContent']/a[@href='/actions/Catalog.action?viewCategory=&categoryId=" + category_id + "']")
        self.driver.find_element(*category_link).click()
        sleep(2)
        return ViewCategoryPage(self.driver)


