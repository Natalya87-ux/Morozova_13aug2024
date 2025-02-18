import requests
import pytest
import allure

BASE_URL = "https://altaivita.ru/"  
HEADERS = {"Content-Type": "application/json"}
COOKIES = {"PHPSESSID": "ph9kjbpcmjdgic9mea1i5kicb1", "CID": "e3c4f3e75c750eddcc6596e95a38108f"}

@allure.feature("Корзина")
@allure.story("Добавление товара в корзину")
def test_add_to_cart():
    payload = {
        "product_id": 709,
        "this_listId": "product_cart",
        "parent_product": 709,
        "LANG_key": "ru",
        "S_wh": 1,
        "S_CID": "e3c4f3e75c750eddcc6596e95a38108f",
        "S_cur_code": "usd",
        "S_koef": 0.01367,
        "quantity": 1,
        "S_hint_code": "eur",
        "S_customerID": ""
    }

    response = requests.post(f"{BASE_URL}/cart/add", json=payload, headers=HEADERS, cookies=COOKIES)
    
    with allure.step("Проверка успешности запроса"):
        assert response.status_code == 200, f"Ошибка запроса: {response.text}"
        data = response.json()
        assert data["status"] == "success", f"Ошибка добавления в корзину: {data}"

@allure.feature("Корзина")
@allure.story("Удаление товара из корзины")
def test_remove_from_cart():
    payload = {"product_id": 709}
    
    response = requests.post(f"{BASE_URL}/cart/remove", json=payload, headers=HEADERS, cookies=COOKIES)
    
    with allure.step("Проверка успешности удаления товара"):
        assert response.status_code == 200, f"Ошибка запроса: {response.text}"
        data = response.json()
        assert data["status"] == "success", f"Ошибка удаления товара из корзины: {data}"