from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    APP_LOGO = (By.CLASS_NAME, "app_logo")

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get(self.URL)

    def fill_credentials(self, username, password):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def is_logo_displayed(self):
        return self.driver.find_element(*self.APP_LOGO).is_displayed()

    def login(self, username, password):
        self.fill_credentials(username, password)
        self.click_login_button()
