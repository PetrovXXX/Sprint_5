import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from locators import Locators

def test_transition_to_section_buns_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCES_TAB)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUNS_TAB)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUNS_SECTION))
    assert driver.find_element(*Locators.BUNS_SECTION).is_displayed(), "Раздел 'Булки' не отображается"

    driver.quit()

def test_transition_to_section_sauces_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCES_TAB)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SAUCES_SECTION))
    assert driver.find_element(*Locators.SAUCES_SECTION).is_displayed(), "Раздел 'Соусы' не отображается"

    driver.quit()

def test_transition_to_section_filling_successful(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FILLINGS_TAB)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FILLINGS_SECTION))
    assert driver.find_element(*Locators.FILLINGS_SECTION).is_displayed(), "Раздел 'Начинки' не отображается"

    driver.quit()
