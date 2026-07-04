import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from locators import Locators

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.REG_NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REG_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        assert "Вход" in driver.find_element(*Locators.LOGIN_HEADER).text

    def test_registration_was_not_successful(self, driver, registration_not_successful):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        name, email, password = registration_not_successful
        driver.find_element(*Locators.REG_NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REG_SUBMIT_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FORM_ERROR_MESSAGE))
        assert "Некорректный пароль" in error_message.text
