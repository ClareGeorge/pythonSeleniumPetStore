from selenium.webdriver.common.by import By


class ViewProductPage:
    item_name = None

    category_text = (By.CSS_SELECTOR, "div[id='Catalog'] h2")
    item_descriptions_text = (By.XPATH, "//tr/td[3]")
    itemid_links = (By.XPATH, "//tr/td[1]/a")
    addtocart_links = (By.XPATH, "//tr/td[5]/a[text()='Add to Cart']")
    backtocategory_link = (By.XPATH, "//div[@id='BackLink']/a")

    signoff_link = (By.PARTIAL_LINK_TEXT, "Sign Out")

    def __init__(self, driver):
        self.driver = driver
    def selectProduct(self, item_name):

        all_item_descriptions = self.driver.find_elements(*ViewProductPage.item_descriptions_text)
        all_itemid_links = self.driver.find_elements(*ViewProductPage.itemid_links)

        for an_item_description in all_item_descriptions:
            updated_item_description = " ".join(an_item_description.text.split())
            if updated_item_description == item_name:
                item_index = all_item_descriptions.index(an_item_description)
                item_link = all_itemid_links[item_index]
                item_link.click()
                break



        self.driver.find_element(*ViewProductPage.signoff_link).click()

