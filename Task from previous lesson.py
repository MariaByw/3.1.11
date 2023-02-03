from selenium import webdriver      #загрузка необходимых модулей
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))        #математическая функция для решения задачи

try:
    link = "http://suninjuly.github.io/redirect_accept.html"         #открыть ссылку
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")         #нажать кнопку
    button.click()

    new_window = browser.window_handles[1]         #сменить окно
    browser.switch_to.window(new_window)


    x_element = browser.find_element(By.ID, 'input_value')         #найти значение для математической задачи
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")         #вставить ответ в окно
    input1.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")         #нажать кнопку
    button.click()
#
#
#
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()