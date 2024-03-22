from selenium.webdriver.common.by import By


class ViewCategoryPage:

    product_name = None

    category_text = (By.CSS_SELECTOR, "div[id='Catalog'] h2")

    product_links = (By.XPATH, "//tr/td/a")
    product_name_text= (By.XPATH, "//tr/td[2]")
    maninmenu_link = (By.XPATH, "//div[@id='BackLink']/a")



