import requests

URL_API = "https://reqres.in"


def list_users() -> list:
    """Получение списка пользователей"""
    url = f"{URL_API}/api/users?page=2"
    response = requests.get(url=url)
    return [response.status_code, response.json()["page"]]


def single_user() -> list:
    """Получение одного пользователя"""
    url = f"{URL_API}/api/users/2"
    response = requests.get(url=url)
    return [response.status_code, response.json()["data"]["id"]]


def single_user_not_found() -> int:
    """Пользователь не найден"""
    url = f"{URL_API}/api/users/23"
    response = requests.get(url=url)
    return response.status_code


def list_resource() -> list:
    """Получение списка ресурса"""
    url = f"{URL_API}/api/unknown"
    response = requests.get(url=url)
    return [response.status_code, response.json()["support"]["url"], response.json()["support"]["text"]]


def single_resource() -> list:
    """Получение одного ресурса"""
    url = f"{URL_API}/api/unknown/2"
    response = requests.get(url=url)
    return [response.status_code, response.json()["data"]["id"]]


def single_resource_not_found() -> int:
    """Один ресурс не найден"""
    url = f"{URL_API}/api/unknown/23"
    response = requests.get(url=url)
    return response.status_code


def create() -> list:
    """Создание пользователя"""
    url = f"{URL_API}/api/users"
    json = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(url=url, json=json)
    return [response.status_code, response.json()["name"], response.json()["job"]]


def put_update() -> list:
    """Обновление пользователя методом put"""
    url = f"{URL_API}/api/users/2"
    json = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(url=url, json=json)
    return [response.status_code, response.json()["name"], response.json()["job"]]


def patch_update() -> list:
    """Обновление пользователя методом patch"""
    url = f"{URL_API}/api/users/2"
    json = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.patch(url=url, json=json)
    return [response.status_code, response.json()["name"], response.json()["job"]]


def delete() -> int:
    """Удаление пользователя"""
    url = f"{URL_API}/api/users/2"
    response = requests.delete(url=url)
    return response.status_code


def register_successful() -> list:
    """Успешная регистрация"""
    url = f"{URL_API}/api/register"
    json = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url=url, json=json)
    return [response.status_code, response.json()["id"], response.json()["token"]]


def register_unsuccessful() -> list:
    """Неуспешная регистрация"""
    url = f"{URL_API}/api/register"
    json = {
        "email": "sydney@fife"
    }
    response = requests.post(url=url, json=json)
    return [response.status_code, response.json()["error"]]


def login_successful() -> list:
    """Успешный логин"""
    url = f"{URL_API}/api/login"
    json = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url=url, json=json)
    return [response.status_code, response.json()["token"]]


def login_unsuccessful() -> list:
    """Неуспешный логин"""
    url = f"{URL_API}/api/login"
    json = {
        "email": "eve.holt@reqres.in",
    }
    response = requests.post(url=url, json=json)
    return [response.status_code, response.json()["error"]]


def delayed_response() -> list:
    """Ответ сервера с задержкой в 3 секунды"""
    url = f"{URL_API}/api/users?delay=3"
    response = requests.get(url=url)
    return [response.status_code, response.json()["support"]["url"], response.json()["support"]["text"]]
