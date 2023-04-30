from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Mary")
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input1.send_keys("Abby")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("Mary_Abby@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "One.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
