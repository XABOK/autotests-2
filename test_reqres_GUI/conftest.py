import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    browser.get(url="https://reqres.in/")
    yield browser
    browser.quit()
