import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Корзина")
@allure.story("Добавление товара в корзину через UI")
def test_add_to_cart_ui(driver):
    with allure.step("Открытие страницы товара"):
        driver.get("https://altaivita.ru/product/altai-mummy-in-capsules-altaivita/") 

    with allure.step("Добавление товара в корзину"):
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".productsets-button"))
        )
        add_button.click()

    with allure.step("Выполнен переход в корзину"):
        cart_selector = ".header__basket-link.ga_link_to_cart"
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, cart_selector))
        )
        cart_button.click()

    with allure.step("Переход в корзину"):
        to_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Перейти в корзину')]"))
        )
        to_cart.click()

    with allure.step("Проверка, что товар добавлен в корзину"):
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".basket__name"))
        )
        assert "Мумиё алтайское" in cart_count.text.strip(), "Ошибка: товар не добавлен в корзину"


@allure.feature("Корзина")
@allure.story("Изменение количества товара в корзине")
def test_update_product_quantity_in_cart(driver):
    """Тест проверяет изменение количества товара в корзине."""

    with allure.step("Открытие страницы товара"):
        driver.get("https://altaivita.ru/product/altai-mummy-in-capsules-altaivita/")

    with allure.step("Добавление товара в корзину"):
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".productsets-button"))
        )
        add_button.click()

    with allure.step("Переход в корзину"):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".header__basket-link"))
        )
        cart_button.click()

    with allure.step("Переход в корзину"):
        to_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Перейти в корзину')]"))
        )
        to_cart.click()


    with allure.step("Проверка текущей цены товара"):
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-item-total"))
        )
        initial_price = float(price_element.text
                              .replace("$", "")
                              .replace("₽", "")
                              .replace(",", ".")
                              .replace(" ", "")
                              .strip())

    with allure.step("Изменение количества товара"):
        quantity_more = driver.find_element(By.CSS_SELECTOR, ".more")
        quantity_more.click()

    with allure.step("Проверка, что цена изменилась"):
        WebDriverWait(driver, 10).until(
            lambda d: float(d.find_element(By.CSS_SELECTOR, ".js-item-total")
                            .text.replace("$", "")
                            .replace("₽", "")
                            .replace(" ", "")
                            .replace(",", ".").strip()
                            ) > initial_price
        )