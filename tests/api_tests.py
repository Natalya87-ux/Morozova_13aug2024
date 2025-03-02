import requests
import pytest
import allure

BASE_URL = "https://altaivita.ru/engine/cart/add_products_to_cart_from_preview.php"
HEADERS = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
DATA = {
    'product_id': '3900',
    'this_listId': 'product_cart',
    'parent_product': '3900',
    'LANG_key': 'ru',
    'S_wh': '1',
    'S_CID': 'e3c4f3e75c750eddcc6596e95a38108f',
    'S_cur_code': 'usd',
    'S_koef': '0.0135',
    'quantity': '1',
    'S_hint_code': 'eur',
    'S_customerID': ''
}

@allure.feature("Корзина")
@allure.story("Добавление товара в корзину")
def test_add_product_to_cart():
    response = requests.post(BASE_URL, headers=HEADERS, data=DATA)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    assert response_json.get("status") == "ok", "Product was not added to cart"


@allure.feature("Корзина")
@allure.story("Удаление товара из корзины")
def test_remove_product_from_cart():
    response = requests.post(BASE_URL, headers=HEADERS, data=DATA)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_json = response.json()
    assert response_json.get("status") == "ok", "Product was not removed from cart"