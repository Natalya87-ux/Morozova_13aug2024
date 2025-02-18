from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Корзина")
@allure.story("Добавление товара в корзину через UI")
def test_add_to_cart_ui():
    driver = webdriver.Chrome()
    
    with allure.step("Открытие страницы товара"):
        driver.get("https://altaivita.ru/product/altai-mummy-in-capsules-altaivita/") 
    
    with allure.step("Добавление товара в корзину"):
        add_button = driver.find_element(By.CSS_SELECTOR, ".productsets-button")  
        add_button.click()
    
    with allure.step("Выполнен переход в корзину"):
        cart_selector = '.header__basket-link.ga_link_to_cart.grid_container_mobile_menu.pdd_cart'
        cart_button = driver.find_element(By.CSS_SELECTOR, cart_selector)
        cart_button.click()

    with allure.step("Переход в корзину"):
        to_cart = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Перейти в корзину']"))
        )
        to_cart.click()

    with allure.step("Проверка, что товар добавлен в корзину"):
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".basket__name"))
        )
        assert cart_count.text == "Мумиё алтайское в капсулах, 60 капсул по 500 мг", "Ошибка: товар не добавлен в корзину"
    
    driver.quit()