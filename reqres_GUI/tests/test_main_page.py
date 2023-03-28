from reqres_GUI.data.data import Data
from reqres_GUI.pages.main_page import MainPage


class TestMainPage:
    """Проверка API методов"""

    def test_list_users(self, driver):
        """Проверка списка пользователей"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.list_users()
        assert status_code == "200", 'Другой код ответа'

    def test_single_user(self, driver):
        """Проверка одного пользователя"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.single_user()
        assert status_code == "200", 'Другой код ответа'

    def test_single_user_not_found(self, driver):
        """Проверка что пользователь не найден"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.single_user_not_found()
        assert status_code == "404", 'Другой код ответа'

    def test_list_resource(self, driver):
        """Проверка списка ресурса"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.list_resource()
        assert status_code == "200", 'Другой код ответа'

    def test_single_resource(self, driver):
        """Проверка одного ресурса"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.single_resource()
        assert status_code == "200", 'Другой код ответа'

    def test_single_resource_not_found(self, driver):
        """Проверка что ресурс не найден"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.single_resource_not_found()
        assert status_code == "404", 'Другой код ответа'

    def test_post(self, driver):
        """Проверка оздания пользователя"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.post()
        assert status_code == "201", 'Другой код ответа'

    def test_put(self, driver):
        """Проверка обновления пользователя методом put"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.put()
        assert status_code == "200", 'Другой код ответа'

    def test_patch(self, driver):
        """Проверка обновления пользователя методом patch"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.patch()
        assert status_code == "200", 'Другой код ответа'

    def test_delete(self, driver):
        """Проверка удаления пользователя"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.delete()
        assert status_code == "204", 'Другой код ответа'

    def test_register_successful(self, driver):
        """Проверка успешной регистрации"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.register_successful()
        assert status_code == "200", 'Другой код ответа'

    def test_register_unsuccessful(self, driver):
        """Проверка неуспешной регистрации"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.register_unsuccessful()
        assert status_code == "400", 'Другой код ответа'

    def test_login_successful(self, driver):
        """Проверка успешного логина"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.login_successful()
        assert status_code == "200", 'Другой код ответа'

    def test_login_unsuccessful(self, driver):
        """Проверка неуспешного логина"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.login_unsuccessful()
        assert status_code == "400", 'Другой код ответа'

    def test_delay(self, driver):
        """Проверка ответа сервера с задержкой в 3 секунды"""
        main_page = MainPage(driver, Data.url)
        main_page.open()
        status_code = main_page.delay()
        assert status_code == "200", 'Другой код ответа'
