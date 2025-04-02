import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from locators import Locators

def test_click_through_personal_account_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*Locators.LOGIN_TO_YUOR_ACCOUNT).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_FORM))
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url

    driver.quit()