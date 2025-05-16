from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Валидные данные
VALID_LOGIN = "admin"
VALID_PASSWORD = "password"

# URL сайта
URL = "https://berpress.github.io/selenium-login-demo/"

def test_successful_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        driver.get(URL)
        # Ввод логина
        driver.find_element(By.ID, "username").send_keys(VALID_LOGIN)
        # Ввод пароля
        driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        # Нажатие кнопки входа
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(1)  # Ждём немного для отображения сообщения

        message = driver.find_element(By.ID, "result").text
        assert message == "Успешно! Вход выполнен.", f"Получено сообщение: {message}"
        print("Позитивный тест прошёл успешно.")
    finally:
        driver.quit()

def test_wrong_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        driver.get(URL)
        # Ввод неправильного логина
        driver.find_element(By.ID, "username").send_keys("wrong_user")
        # Ввод правильного пароля
        driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        # Нажатие кнопки входа
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(1)

        message = driver.find_element(By.ID, "result").text
        assert "Ошибка" in message or "неверный" in message or message != "Успешно! Вход выполнен.", \
            f"Получено сообщение: {message}"
        print("Негативный тест (неправильный логин) прошёл успешно.")
    finally:
        driver.quit()

def test_wrong_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        driver.get(URL)
        # Ввод правильного логина
        driver.find_element(By.ID, "username").send_keys(VALID_LOGIN)
        # Ввод неправильного пароля
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        # Нажатие кнопки входа
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(1)

        message = driver.find_element(By.ID, "result").text
        assert "Ошибка" in message or "неверный" in message or message != "Успешно! Вход выполнен.", \
            f"Получено сообщение: {message}"
        print("Негативный тест (неправильный пароль) прошёл успешно.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_successful_login()
    test_wrong_login()
    test_wrong_password()