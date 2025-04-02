import pytest
from selenium import webdriver
from data import Credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

@pytest.fixture
def driver():
    #Фикстура для инициализации и закрытия браузера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def register_new_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    name, email, password = Credentials()

    driver.find_element(*Locators.REG_NAME_FIELD).send_keys(name)
    driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(password)
    driver.find_element(*Locators.REG_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))

    return {"email": email, "password": password, "name": name}