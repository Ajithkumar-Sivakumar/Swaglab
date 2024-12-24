from selenium.webdriver.common.by import By

class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"
    LOGOUT_BUTTON = (By.ID, "react-burger-menu-btn")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        self.driver = driver

    def is_on_inventory_page(self):
        return self.driver.current_url == self.URL

    def extract_inventory_data(self, file_path):
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        with open(file_path, "w") as file:
            for item in items:
                file.write(item.text + "\n")

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()