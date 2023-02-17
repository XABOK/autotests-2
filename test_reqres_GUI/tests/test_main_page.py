from test_reqres_GUI.pages.main_page import MainPage
from ..pages.main_page import MainPage


class TestMainPage:
    """Проверка API запросов"""

    def test_list_users(self, browser):
        """Проверка списка пользователей"""
        main_page = MainPage(browser)
        status_code = main_page.list_users()
        assert status_code == "200", 'Другой код ответа'

    def test_single_user(self, browser):
        """Проверка одного пользователя"""
        main_page = MainPage(browser)
        status_code = main_page.single_user()
        assert status_code == "200", 'Другой код ответа'

    def test_single_user_not_found(self, browser):
        """Проверка что пользователь не найден"""
        main_page = MainPage(browser)
        status_code = main_page.single_user_not_found()
        assert status_code == "404", 'Другой код ответа'

    def test_list_resource(self, browser):
        """Проверка списка ресурса"""
        main_page = MainPage(browser)
        status_code = main_page.list_resource()
        assert status_code == "200", 'Другой код ответа'

    def test_single_resource(self, browser):
        """Проверка одного ресурса"""
        main_page = MainPage(browser)
        status_code = main_page.single_resource()
        assert status_code == "200", 'Другой код ответа'

    def test_single_resource_not_found(self, browser):
        """Проверка что ресурс не найден"""
        main_page = MainPage(browser)
        status_code = main_page.single_resource_not_found()
        assert status_code == "404", 'Другой код ответа'

    def test_post(self, browser):
        """Проверка оздания пользователя"""
        main_page = MainPage(browser)
        status_code = main_page.post()
        assert status_code == "201", 'Другой код ответа'

    def test_put(self, browser):
        """Проверка обновления пользователя методом put"""
        main_page = MainPage(browser)
        status_code = main_page.put()
        assert status_code == "200", 'Другой код ответа'

    def test_patch(self, browser):
        """Проверка обновления пользователя методом patch"""
        main_page = MainPage(browser)
        status_code = main_page.patch()
        assert status_code == "200", 'Другой код ответа'

    def test_delete(self, browser):
        """Проверка удаления пользователя"""
        main_page = MainPage(browser)
        status_code = main_page.delete()
        assert status_code == "204", 'Другой код ответа'

    def test_register_successful(self, browser):
        """Проверка успешной регистрации"""
        main_page = MainPage(browser)
        status_code = main_page.register_successful()
        assert status_code == "200", 'Другой код ответа'

    def test_register_unsuccessful(self, browser):
        """Проверка неуспешной регистрации"""
        main_page = MainPage(browser)
        status_code = main_page.register_unsuccessful()
        assert status_code == "400", 'Другой код ответа'

    def test_login_successful(self, browser):
        """Проверка успешного логина"""
        main_page = MainPage(browser)
        status_code = main_page.login_successful()
        assert status_code == "200", 'Другой код ответа'

    def test_login_unsuccessful(self, browser):
        """Проверка неуспешного логина"""
        main_page = MainPage(browser)
        status_code = main_page.login_unsuccessful()
        assert status_code == "400", 'Другой код ответа'

    def test_delay(self, browser):
        """Проверка ответа сервера с задержкой в 3 секунды"""
        main_page = MainPage(browser)
        status_code = main_page.delay()
        assert status_code == "200", 'Другой код ответа'
