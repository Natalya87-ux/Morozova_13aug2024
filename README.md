# Morozova_13aug2024

## Установить зависимости
pip install selenium requests pytest allure-pytest

## Запуск API-тестов
pytest -v --alluredir=allure-results tests/api_tests.py

## Запуск UI-тестов
pytest -v --alluredir=allure-results tests/ui_tests.py

## Генерация отчета Allure
allure serve allure-results