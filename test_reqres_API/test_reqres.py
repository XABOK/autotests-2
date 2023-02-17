from reqres import list_users, single_user, single_user_not_found, list_resource, single_resource, \
    single_resource_not_found, create, put_update, patch_update, delete, register_successful, register_unsuccessful, \
    login_successful, login_unsuccessful, delayed_response


def test_list_users():
    """Проверка списка пользователей"""
    status_code_list_users = list_users()[0]
    page_list_users = list_users()[1]
    assert status_code_list_users == 200, f"Неверный код ответа, получен {status_code_list_users}"
    assert page_list_users == 2, f"Получена другая страница, равная {page_list_users}"


def test_single_user():
    """Проверка одного пользователя"""
    status_code_single_user = single_user()[0]
    id_single_user = single_user()[1]
    assert status_code_single_user == 200, f"Неверный код ответа, получен {status_code_single_user}"
    assert id_single_user == 2, f"Получен другой id, равный {id_single_user}"


def test_single_user_not_found():
    """Проверка что пользователь не найден"""
    status_code_single_user_not_found = single_user_not_found()
    assert status_code_single_user_not_found == 404, f"Неверный код ответа, получен {status_code_single_user_not_found}"


def test_list_resource():
    """Проверка списка ресурса"""
    status_code_list_resource = list_resource()[0]
    url_list_resource = list_resource()[1]
    text_list_resource = list_resource()[2]
    assert status_code_list_resource == 200, f"Неверный код ответа, получен {status_code_list_resource}"
    assert url_list_resource == "https://reqres.in/#support-heading", f"Получен другой url, равный {url_list_resource}"
    assert text_list_resource == "To keep ReqRes free, contributions towards server costs are appreciated!", f"Получен другой текст, равный {text_list_resource}"


def test_single_resource():
    """Проверка одного ресурса"""
    status_code_single_resource = single_resource()[0]
    id_single_resource = single_resource()[1]
    assert status_code_single_resource == 200, f"Неверный код ответа, получен {status_code_single_resource}"
    assert id_single_resource == 2, f"Получен другой id, равный {id_single_resource}"


def test_single_resource_not_found():
    """Проверка что ресурс не найден"""
    status_code_single_resource_not_found = single_resource_not_found()
    assert status_code_single_resource_not_found == 404, f"Неверный код ответа, получен {status_code_single_resource_not_found}"


def test_create():
    """Проверка оздания пользователя"""
    status_code_create = create()[0]
    name_create = create()[1]
    job_create = create()[2]
    assert status_code_create == 201, f"Неверный код ответа, получен {status_code_create}"
    assert name_create == "morpheus", f"Получено другое имя, равное {name_create}"
    assert job_create == "leader", f"Получена другая работа, равная {job_create}"


def test_put_update():
    """Проверка обновления пользователя методом put"""
    status_code_put_update = put_update()[0]
    name_put_update = put_update()[1]
    job_put_update = put_update()[2]
    assert status_code_put_update == 200, f"Неверный код ответа, получен {status_code_put_update}"
    assert name_put_update == "morpheus", f"Получено другое имя, равное {name_put_update}"
    assert job_put_update == "zion resident", f"Получена другая работа, равная {job_put_update}"


def test_patch_update():
    """Проверка обновления пользователя методом patch"""
    status_code_patch_update = patch_update()[0]
    name_patch_update = patch_update()[1]
    job_patch_update = patch_update()[2]
    assert status_code_patch_update == 200, f"Неверный код ответа, получен {status_code_patch_update}"
    assert name_patch_update == "morpheus", f"Получено другое имя, равное {name_patch_update}"
    assert job_patch_update == "zion resident", f"Получена другая работа, равная {job_patch_update}"


def test_delete():
    """Проверка удаления пользователя"""
    status_code_delete = delete()
    assert status_code_delete == 204, f"Неверный код ответа, получен {status_code_delete}"


def test_register_successful():
    """Проверка успешной регистрации"""
    status_code_register_successful = register_successful()[0]
    id_register_successful = register_successful()[1]
    token_register_successful = register_successful()[2]
    assert status_code_register_successful == 200, f"Неверный код ответа, получен {status_code_register_successful}"
    assert id_register_successful == 4, f"Получен другой id, равный {id_register_successful}"
    assert token_register_successful == "QpwL5tke4Pnpja7X4", f"Получен другой token, равный {token_register_successful}"


def test_register_unsuccessful():
    """Проверка неуспешной регистрации"""
    status_code_register_unsuccessful = register_unsuccessful()[0]
    error_register_unsuccessful = register_unsuccessful()[1]
    assert status_code_register_unsuccessful == 400, f"Неверный код ответа, получен {status_code_register_unsuccessful}"
    assert error_register_unsuccessful == "Missing password", f"Получена другая ошибка, равная {error_register_unsuccessful}"


def test_login_successful():
    """Проверка успешного логина"""
    status_code_login_successful = login_successful()[0]
    token_login_successful = login_successful()[1]
    assert status_code_login_successful == 200, f"Неверный код ответа, получен {status_code_login_successful}"
    assert token_login_successful == "QpwL5tke4Pnpja7X4", f"Получен другой token, равный {token_login_successful}"


def test_login_unsuccessful():
    """Проверка неуспешного логина"""
    status_code_login_unsuccessful = login_unsuccessful()[0]
    error_login_unsuccessful = login_unsuccessful()[1]
    assert status_code_login_unsuccessful == 400, f"Неверный код ответа, получен {status_code_login_unsuccessful}"
    assert error_login_unsuccessful == "Missing password", f"Получена другая ошибка, равная {error_login_unsuccessful}"


def test_delayed_response():
    """Проверка ответа сервера с задержкой в 3 секунды"""
    status_code_delayed_response = delayed_response()[0]
    url_delayed_response = delayed_response()[1]
    text_delayed_response = delayed_response()[2]
    assert status_code_delayed_response == 200, f"Неверный код ответа, получен {status_code_delayed_response}"
    assert url_delayed_response == "https://reqres.in/#support-heading", f"Получен другой url, равный {url_delayed_response}"
    assert text_delayed_response == "To keep ReqRes free, contributions towards server costs are appreciated!", f"Получен другой текст, равный {text_delayed_response}"
