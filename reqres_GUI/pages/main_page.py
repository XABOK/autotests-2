from test_reqres_GUI.pages.base_page import BasePage
from test_reqres_GUI.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Методы для работы с главной страницей"""
    locators = MainPageLocators()

    def list_users(self):
        self.element_is_clickable(self.locators.LIST_USERS).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def single_user(self):
        self.element_is_clickable(self.locators.SINGLE_USER).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def single_user_not_found(self):
        self.element_is_clickable(self.locators.SINGLE_USER_NOT_FOUND).click()
        return self.element_are_visible(self.locators.STATUS_CODE_BAD).text

    def list_resource(self):
        self.element_is_clickable(self.locators.LIST_RESOURCE).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def single_resource(self):
        self.element_is_clickable(self.locators.SINGLE_RESOURCE).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def single_resource_not_found(self):
        self.element_is_clickable(self.locators.SINGLE_RESOURCE_NOT_FOUND).click()
        return self.element_are_visible(self.locators.STATUS_CODE_BAD).text

    def post(self):
        self.element_is_clickable(self.locators.POST).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def put(self):
        self.element_is_clickable(self.locators.PUT).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def patch(self):
        self.element_is_clickable(self.locators.PATCH).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def delete(self):
        self.element_is_clickable(self.locators.DELETE).click()
        return self.element_are_visible(self.locators.STATUS_CODE_BAD).text

    def register_successful(self):
        self.element_is_clickable(self.locators.REGISTER_SUCCESSFUL).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def register_unsuccessful(self):
        self.element_is_clickable(self.locators.REGISTER_UNSUCCESSFUL).click()
        return self.element_are_visible(self.locators.STATUS_CODE_BAD).text

    def login_successful(self):
        self.element_is_clickable(self.locators.LOGIN_SUCCESSFUL).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def login_unsuccessful(self):
        self.element_is_clickable(self.locators.LOGIN_UNSUCCESSFUL).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text

    def delay(self):
        self.element_is_clickable(self.locators.DELAY).click()
        return self.element_are_visible(self.locators.STATUS_CODE).text
