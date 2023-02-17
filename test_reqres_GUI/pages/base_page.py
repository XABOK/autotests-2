from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Общие методы"""
    def __init__(self, browser):
        self.browser = browser

    def element_is_clickable(self, locator, timeout=10):
        """Является ли элемент кликабельным"""
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def element_are_visible(self, locator, timeout=10):
        """Является ли элемент видимым"""
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
