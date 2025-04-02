import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from conftest import driver
from locators import Locators

def test_output_by_exit_button_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    email, password = Credentials.login(self=None)
    driver.find_element(*Locators.LOGIN_TO_YUOR_ACCOUNT).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_ACCOUNT_SECTION)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url

    driver.quit()