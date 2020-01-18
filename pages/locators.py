from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # локаторы для формы логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Я забыл пароль")
    # локаторы для формы регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_INPUT_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")



