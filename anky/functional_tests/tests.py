from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 


class NewVisitorTest(LiveServerTestCase):
    '''тест нового посетителя'''
    
    def setUp(self):
        '''установка'''
        options = ChromeOptions()
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=options)

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def check_for_row_in_list_talbe(self, row_text):
        '''подтверждение строки в таблице списка'''
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        # Открываем домашнюю страницу
        self.browser.get(self.live_server_url)

        # Видим, что заголовок и шапка страницы говорят о списке вопросов для запоминания и ответов
        self.assertIn('Список вопросов для запоминания', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text 
        self.assertIn('Список вопросов для запоминания', header_text)

        # Нам предлагается сразу ввести первый вопрос и ответ на него
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Введите вопрос')
        # Мы вводим в текстовом поле для вопроса "Автор теории относительности"
        inputbox.send_keys('Автор теории относительности')
        time.sleep(2)

        # inputbox = self.browser.find_element(By.ID, 'id_new_item_answer')
        # self.assertEqual(inputbox.get_attribute('placeholder'), 'Введите ответ')
        # time.sleep(2)

        # # Мы вводим в поле для ответа ответ "Эйнштейн"
        # inputbox.send_keys('Эйнштейн')

        # Когда мы нажимаем Enter, страница обновляется и теперь 
        # страница содержит "Вопрос: Автор теории относительности. Ответ: Эйнштейн" 
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        self.check_for_row_in_list_talbe('Вопрос: Автор теории относительности')
        # self.check_for_row_in_list_talbe('Ответ: Эйнштейн')               
        self.fail('Закончить тест')
        
    
        # 

        # Когда мы нажимаем Enter, страница обновляется и теперь страница содержит "Вопрос: Автор теории относительности. Ответ: Эйнштейн". Ниже
        # находится кнопка подтвердить.
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # table = self.browser.find_element(By.ID, 'id_answer_table')
        # rows = table.find_elements(By.TAG_NAME, 'tr')
        # self.assertTrue(any(row.text == 'Эйнштейн' for row in rows))
        # 

        # Мы нажимаем кнопку, страница обновляется и появляется надпись "Запись внесена. Хотите добавить запись?" Внизу две кнопки Добавить и Далее.

        # Мы нажимаем кнопку Добавить и появляется текстовое поле с предложением ввести новую запись.

        # Мы вводим в текстовом поле "Дата начала 2-й мировой войны"

        # Когда мы нажимаем Enter, страница обновляется и теперь страница содержит "Вопрос: Дата начала 2-й мировой войны. Введите ответ" с полем для ответа

        # Мы вводим в поле для ответа ответ "1939 год"

        # Когда мы нажимаем Enter, страница обновляется и теперь страница содержит "Вопрос: Дата начала 2-й мировой войны. Ответ: 1939 год". Ниже
        # находится кнопка подтвердить.

        # Мы нажимаем кнопку, страница обновляется и появляется надпись "Запись внесена. Хотите добавить запись?" Внизу две кнопки Добавить и Далее.

        # Мы нажимаем кнопку Далее.

        # Мы проверяем, сохранились ли наши записи

        # Мы видим, что сайт сгенерировал уникальный URL-адрес - об этом выводится текст с пояснением.

        # Мы посещаем эти URL-адреса - наши записи там.

if __name__ == '__main__':
    unittest.main(warnings='ignore')     
