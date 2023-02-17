from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_list_users(browser):
    button_list_users = browser.find_element(By.CSS_SELECTOR, '[data-id="users"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_list_users)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_list_users)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_single_user(browser):
    button_single_user = browser.find_element(By.CSS_SELECTOR, '[data-id="users-single"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_single_user)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_single_user)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_single_user_not_found(browser):
    button_single_user_not_found = browser.find_element(By.CSS_SELECTOR, '[data-id="users-single-not-found"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_single_user_not_found)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_single_user_not_found)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '404', 'Другой код ответа'


def test_list_resource(browser):
    button_list_resource = browser.find_element(By.CSS_SELECTOR, '[data-id="unknown"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_list_resource)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_list_resource)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_single_resource(browser):
    button_single_resource = browser.find_element(By.CSS_SELECTOR, '[data-id="unknown-single"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_single_resource)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_single_resource)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_single_resource_not_found(browser):
    button_single_resource_not_found = browser.find_element(By.CSS_SELECTOR, '[data-id="unknown-single-not-found"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_single_resource_not_found)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_single_resource_not_found)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '404', 'Другой код ответа'


def test_post(browser):
    button_post = browser.find_element(By.CSS_SELECTOR, '[data-id="post"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_post)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_post)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '201', 'Другой код ответа'


def test_put(browser):
    button_put = browser.find_element(By.CSS_SELECTOR, '[data-id="put"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_put)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_put)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_patch(browser):
    button_patch = browser.find_element(By.CSS_SELECTOR, '[data-id="patch"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_patch)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_patch)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_delete(browser):
    button_delete = browser.find_element(By.CSS_SELECTOR, '[data-id="delete"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_delete)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_delete)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_register_successful(browser):
    button_register_successful = browser.find_element(By.CSS_SELECTOR, '[data-id="register-successful"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_register_successful)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_register_successful)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_register_unsuccessful(browser):
    button_register_unsuccessful = browser.find_element(By.CSS_SELECTOR, '[data-id="register-unsuccessful"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_register_unsuccessful)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_register_unsuccessful)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '400', 'Другой код ответа'


def test_login_successful(browser):
    button_login_successful = browser.find_element(By.CSS_SELECTOR, '[data-id="login-successful"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_login_successful)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_login_successful)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'


def test_login_unsuccessful(browser):
    button_login_unsuccessful = browser.find_element(By.CSS_SELECTOR, '[data-id="login-unsuccessful"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_login_unsuccessful)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_login_unsuccessful)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '400', 'Другой код ответа'


def test_delay(browser):
    button_delay = browser.find_element(By.CSS_SELECTOR, '[data-id="delay"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_delay)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(mark=button_delay)
    ).click()
    assert browser.find_element(By.CSS_SELECTOR, '[class="response-code"]').text == '200', 'Другой код ответа'
