import random
def generate_registration_data():
    name = f"IlyaPetrov{random.randint(100, 999)}"
    email = f"Ilya_Petrov_17_{random.randint(100, 999)}@yandex.ru"
    password = f"{random.randint(100000, 999999)}"
    return name, email, password