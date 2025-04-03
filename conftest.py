import pytest
from selenium import webdriver
from data import Credentials
from helper import generate_registration_data
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

@pytest.fixture(scope="function")
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_data():
    # Используем класс Credentials для получения данных для входа
    credentials = Credentials()
    email, password = credentials.login()
    return email, password

@pytest.fixture
def registration_data():
    # Генерация данных для регистрации
    name, email, password = generate_registration_data()
    return name, email, password

@pytest.fixture
def registration_not_successful():
    # Используем класс Credentials для получения данных для регистрации
    credentials = Credentials()
    name, email, password = credentials.registration_was_not_successful()
    return name, email, password

