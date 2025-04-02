import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from data import Credentials
from locators import Locators

def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    email, password = Credentials.login(self=None)
    driver.find_element(*Locators.LOGIN_TO_YUOR_ACCOUNT).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url

    driver.quit()

def test_get_login_by_button_personal_account_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    email, password = Credentials.login(self=None)
    driver.find_element(*Locators.BUTTON_ACCOUNT_SECTION).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url

    driver.quit()

def test_login_via_button_in_registration_form_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    email, password = Credentials.login(self=None)
    driver.find_element(*Locators.LOGIN_LINK_REGISTRATION_FORM).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url

    driver.quit()

def test_login_via_button_in_password_recovery_form_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    email, password = Credentials.login(self=None)
    driver.find_element(*Locators.LOGIN_LINK_REGISTRATION_FORM).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
    assert "/account/profile" in driver.current_url

    driver.quit()

