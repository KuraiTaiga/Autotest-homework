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
    driver.get(URL)
    wait_obj = wait(driver, 10)

    # Ввод логина
    login_field = wait_obj.until(EC.presence_of_element_located((By.ID, "username")))
    login_field.send_keys(VALID_LOGIN)

    # Ввод пароля
    password_field = wait_obj.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys(VALID_PASSWORD)

    # Нажатие кнопки входа
    login_button = wait_obj.until(EC.element_to_be_clickable((By.ID, "login-btn")))
    login_button.click()

    # Ожидаем появления сообщения о результате
    message_element = wait_obj.until(EC.presence_of_element_located((By.ID, "result")))
    message = message_element.text

    assert message == "Успешно! Вход выполнен.", f"Получено сообщение: {message}"
    print("Позитивный тест прошёл успешно.")
    driver.quit()

def test_wrong_login():
    driver = webdriver.Chrome()
    driver.get(URL)
    wait_obj = wait(driver, 10)

    # Ввод неправильного логина
    login_field = wait_obj.until(EC.presence_of_element_located((By.ID, "username")))
    login_field.send_keys("wrong_user")

    # Ввод правильного пароля
    password_field = wait_obj.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys(VALID_PASSWORD)

    # Нажатие кнопки входа
    login_button = wait_obj.until(EC.element_to_be_clickable((By.ID, "login-btn")))
    login_button.click()

    # Ожидаем появления сообщения о результате
    message_element = wait_obj.until(EC.presence_of_element_located((By.ID, "result")))
    message = message_element.text

    assert "Ошибка" in message or "неверный" in message or message != "Успешно! Вход выполнен.", \
        f"Получено сообщение: {message}"
    
    print("Негативный тест (неправильный логин) прошёл успешно.")
    driver.quit()

def test_wrong_password():
    driver = webdriver.Chrome()
    driver.get(URL)
    wait_obj = wait(driver, 10)

    # Ввод правильного логина
    login_field = wait_obj.until(EC.presence_of_element_located((By.ID, "username")))
    login_field.send_keys(VALID_LOGIN)

    # Ввод неправильного пароля
    password_field = wait_obj.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("wrong_password")

    # Нажатие кнопки входа
    login_button = wait_obj.until(EC.element_to_be_clickable((By.ID, "login-btn")))
    login_button.click()

    # Ожидаем появления сообщения о результате
    message_element = wait_obj.until(EC.presence_of_element_located((By.ID, "result")))
    message = message_element.text

    assert "Ошибка" in message or "неверный" in message or message != "Успешно! Вход выполнен.", \
        f"Получено сообщение: {message}"
    
    print("Негативный тест (неправильный пароль) прошёл успешно.")
    
if __name__ == "__main__":
    test_successful_login()
    test_wrong_login()
    test_wrong_password()