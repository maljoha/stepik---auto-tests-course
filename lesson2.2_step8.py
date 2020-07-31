'''
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
'''

from selenium import webdriver
import os
import time

try:
    # Открыть страницу http://suninjuly.github.io/file_input.html
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    browser.find_element_by_name("firstname").send_keys("Лена")
    browser.find_element_by_name("lastname").send_keys("Л.")
    browser.find_element_by_name("email").send_keys("lena@mailforspam.com")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_id("file").send_keys(file_path)

    # Нажать на кнопку Submit.
    b_element = browser.find_element_by_tag_name("button")
    b_element.click()

finally:
    # успеваем посмотреть результаты за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()