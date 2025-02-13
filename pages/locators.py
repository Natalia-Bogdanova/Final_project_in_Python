from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    LOGIN = (By.CSS_SELECTOR, "#login_form")