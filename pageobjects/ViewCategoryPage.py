from selenium.webdriver.common.by import By

from pageobjects.ViewProductPage import ViewProductPage


class ViewCategoryPage:

    product_name = None

    category_text = (By.CSS_SELECTOR, "div[id='Catalog'] h2")

    product_links = (By.XPATH, "//tr/td/a")
    product_names_text= (By.XPATH, "//tr/td[2]")
    maninmenu_link = (By.XPATH, "//div[@id='BackLink']/a")

    def __init__(self, driver):
        self.driver = driver
    def selectProduct(self, product_name):
        ViewCategoryPage.product_name = product_name
        all_product_names = self.driver.find_elements(*ViewCategoryPage.product_names_text)
        all_product_links = self.driver.find_elements(*ViewCategoryPage.product_links)
        for  a_product_name  in all_product_names :
            if product_name == a_product_name.text:
                product_index = all_product_names.index(a_product_name)
                product_link =  all_product_links[product_index]
                product_link.click()
                break;
        return ViewProductPage(self.driver)




