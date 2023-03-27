import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
