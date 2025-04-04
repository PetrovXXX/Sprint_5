import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators

class TestClickButonPersonalAccount:

    def test_click_through_personal_account_successful(self, driver): #Проверка переход по клику на «Личный кабинет» в форму регистрации.
        driver.get("https://stellarburgers.nomoreparties.site/") #Сайт
        driver.find_element(*Locators.LOGIN_TO_YUOR_ACCOUNT).click() #Клик по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_FORM)) # Ожидание пока откроется окно формы входа
        WebDriverWait(driver, 10).until(EC.url_contains("/login")) # Ожидание что в URL появилось "/login"
        assert "/login" in driver.current_url # проверка URL на наличие "/login"

