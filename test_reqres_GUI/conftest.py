import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(url="https://reqres.in/")
    yield browser
    browser.quit()
