import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestAuthorization:
    def test_login_from_main_page(self, driver, login_data):
        driver.get("https://stellarburgers.nomoreparties.site/")
        email, password = login_data
        driver.find_element(*Locators.LOGIN_TO_YUOR_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url


    def test_get_login_by_button_personal_account_successful(self, driver, login_data):
        driver.get("https://stellarburgers.nomoreparties.site/")
        email, password = login_data
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()
        WebDriverWait(driver, 15).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url


    def test_login_via_button_in_registration_form_successful(self, driver, login_data):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        email, password = login_data
        driver.find_element(*Locators.LOGIN_LINK_REGISTRATION_FORM).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()
        WebDriverWait(driver, 15).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url


    def test_login_via_button_in_password_recovery_form_successful(self, driver, login_data):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        email, password = login_data
        driver.find_element(*Locators.LOGIN_LINK_REGISTRATION_FORM).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url
