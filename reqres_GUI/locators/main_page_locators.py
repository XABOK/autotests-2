from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы с главной страницы"""
    STATUS_CODE = (By.CSS_SELECTOR, '[class="response-code"]')
    STATUS_CODE_BAD = (By.CSS_SELECTOR, '[class="response-code bad"]')
    LIST_USERS = (By.CSS_SELECTOR, '[data-id="users"]')
    SINGLE_USER = (By.CSS_SELECTOR, '[data-id="users-single"]')
    SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, '[data-id="users-single-not-found"]')
    LIST_RESOURCE = (By.CSS_SELECTOR, '[data-id="unknown"]')
    SINGLE_RESOURCE = (By.CSS_SELECTOR, '[data-id="unknown-single"]')
    SINGLE_RESOURCE_NOT_FOUND = (By.CSS_SELECTOR, '[data-id="unknown-single-not-found"]')
    POST = (By.CSS_SELECTOR, '[data-id="post"]')
    PUT = (By.CSS_SELECTOR, '[data-id="put"]')
    PATCH = (By.CSS_SELECTOR, '[data-id="patch"]')
    DELETE = (By.CSS_SELECTOR, '[data-id="delete"]')
    REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, '[data-id="register-successful"]')
    REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, '[data-id="register-unsuccessful"]')
    LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, '[data-id="login-successful"]')
    LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, '[data-id="login-unsuccessful"]')
    DELAY = (By.CSS_SELECTOR, '[data-id="delay"]')
