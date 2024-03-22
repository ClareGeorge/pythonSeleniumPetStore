from selenium.webdriver.common.by import By


class CatalogPage:
    category_id = None
    signoff_link = (By.PARTIAL_LINK_TEXT, "Sign Out")
    category_link = (By.XPATH, "//div[@id='SidebarContent']/a[@href='/actions/Catalog.action?viewCategory=&categoryId="+ category_id +"']")



    def __init__(self, driver):
        self.driver = driver
        # self.driver.find_element(*SearchProductsPage.signoff_link).click()

    def selectCategory():
        global category_id
