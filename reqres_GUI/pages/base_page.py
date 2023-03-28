from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Общие методы"""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_clickable(self, locator, timeout=10):
        """Является ли элемент кликабельным"""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_are_visible(self, locator, timeout=10):
        """Является ли элемент видимым"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
