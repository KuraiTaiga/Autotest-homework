from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Валидные данные
VALID_LOGIN = "admin"
VALID_PASSWORD = "password"

# URL сайта
URL = "https://berpress.github.io/selenium-login-demo/"

# Создаём глобальный объект WebDriverWait для повторного использования
wait = WebDriverWait

def test_successful_login():
    driver = webdriver.Chrome()
    wait_obj = wait(driver, 10)
    driver.get(URL)
        # Ввод логина
    driver.find_element(By.ID, "username").send_keys(VALID_LOGIN)
        # Ввод пароля
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        # Нажатие кнопки входа
    driver.find_element(By.ID, "login-btn").click()
    # Ожидаем появления сообщения о результате
    message_element = wait_obj.until(EC.presence_of_element_located((By.ID, "result")))
    message = message_element.text
    assert message == "Успешно! Вход выполнен.", f"Получено сообщение: {message}"
    print("Позитивный тест прошёл успешно.")
    driver.quit()

def test_wrong_login():
    driver = webdriver.Chrome()
    wait_obj = wait(driver, 10)
    driver.get(URL)
        # Ввод неправильного логина
    driver.find_element(By.ID, "username").send_keys("wrong_user")
        # Ввод правильного пароля
    driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        # Нажатие кнопки входа
    driver.find_element(By.ID, "login-btn").click()
    # Ожидаем появления сообщения о результате
    message_element = wait_obj.until(EC.presence_of_element_located((By.ID, "result")))
    message = message_element.text
    assert "Ошибка" in message or "неверный" in message or message != "Успешно! Вход выполнен.", \
        f"Получено сообщение: {message}"
    print("Негативный тест (неправильный логин) прошёл успешно.")
    driver.quit()

def test_wrong_password():
    driver = webdriver.Chrome()
    wait_obj = wait(driver, 10)
    driver.get(URL)
        # Ввод правильного логина
    driver.find_element(By.ID, "username").send_keys(VALID_LOGIN)
        # Ввод неправильного пароля
    driver.find_element(By.ID, "password").send_keys("wrong_password")
        # Нажатие кнопки входа
    driver.find_element(By.ID, "login-btn").click()
    # Ожидаем появления сообщения о результате
    message_element = wait_obj.until(EC.presence_of_element_located((By.ID, "result")))
    message = message_element.text
    assert "Ошибка" in message or "неверный" in message or message != "Успешно! Вход выполнен.", \
        f"Получено сообщение: {message}"
    print("Негативный тест (неправильный пароль) прошёл успешно.")
    driver.quit()

if __name__ == "__main__":
    test_successful_login()
    test_wrong_login()
    test_wrong_password()
