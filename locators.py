from selenium.webdriver.common.by import By

class Locators:
    # Страница регистрации
    REG_NAME_FIELD = (By.XPATH, "//fieldset[1]//input[@name='name']") #Поле "Имя"
    REG_EMAIL_FIELD = (By.XPATH, "//fieldset[2]//input[@name='name']") #Поле "Email"
    REG_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']") #Поле "Пароль"
    REG_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']") #Заголовок формы входа с текстом "Вход"
    FORM_ERROR_MESSAGE = (By.XPATH, '//form//p[contains(@class, "input__error")]') #Сообщение об ошибке формы регистрации
    # Вход
    LOGIN_TO_YUOR_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт на главной странице
    EMAIL_INPUT = (By.XPATH, '//form//input[@name="name"]') #Поле "Email"
    PASSWORD_INPUT = (By.XPATH, '//form//input[@type="password"]') #Поле "Пароль"
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') #Кнопка "Войти"
    LOGO_TEXT_PERSONAL_ACCOUNT = (By.XPATH, '//nav/a[contains(@href, "account")]') #Кнопка "Личный кабинет"
    BUTTON_ACCOUNT_SECTION = (By.XPATH, '//a[.//p[text()="Личный Кабинет"]]') #Кнопка "Личный кабинет"
    LOGIN_LINK_REGISTRATION_FORM = (By.XPATH, '//a[text()="Войти"]') #Кнопка "Войти" в форме регистрации

    LOGIN_FORM = (By.XPATH, '//div[contains(@class, "Auth_login__3hAey")]') #Форма входа в Личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]') #Кнопка "Конструктор"
    BUN_FLUORESCENT_INGREDIENT = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]') #Кнопка "Флюоресцентная булка"
    BUN_SECTION = (By.XPATH, '//h2[text()="Булки"]') #Кнопка "Булки"

    LOGOUT_BUTTON = (By.XPATH, '//nav/ul/li[3]/button') #Выход Кнопка
    INGREDIENT_SAUCE = (By.XPATH, './/span[text()="Соусы"]') #Кнопка "Соусы"
    ACTIVE_TAB = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]') #Активная кнопка "Булки"

    INGREDIENT_FILLING = (By.XPATH, './/span[text()="Начинки"]') #Кнопка "Начинки"

    BUNS_TAB = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Булки"]/..') #ищет раздел "Булки"
    SAUCES_TAB = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Соусы"]/..') #ищет раздел "Соусы"
    FILLINGS_TAB = (By.XPATH, '//div[contains(@class, "tab_tab")]//span[text()="Начинки"]/..') ##ищет раздел "Начинки"

    BUNS_SECTION = (By.XPATH, '//h2[text()="Булки"]') #Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, '//h2[text()="Соусы"]') #Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, '//h2[text()="Начинки"]') #Раздел "Начинки"


