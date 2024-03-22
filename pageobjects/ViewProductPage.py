from selenium.webdriver.common.by import By


class ViewProductPage:
    item_name = None

    category_text = (By.CSS_SELECTOR, "div[id='Catalog'] h2")
    item_descriptions_text = (By.XPATH, "//tr/td[3]")
    itemid_links = (By.XPATH, "//tr/td[1]/a")
    addtocart_links = (By.XPATH, "//tr/td[5]/a[text()='Add to Cart']")
    backtocategory_link = (By.XPATH, "//div[@id='BackLink']/a")
