from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time 


MAX_WAIT = 10

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

    def wait_for_row_in_list_talbe(self, row_text):
        '''подтверждение строки в таблице списка'''
        start_time = time.time()
        while True:
            try: 
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return 
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        # Открываем домашнюю страницу
        self.browser.get(self.live_server_url)

        # Видим, что заголовок и шапка страницы говорят о списке вопросов для запоминания и ответов
        self.assertIn('Список вопросов для запоминания', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text 
        self.assertIn('Начать новый список вопросов для запоминания', header_text)

        # Нам предлагается сразу ввести первый вопрос и ответ на него
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Введите вопрос')
        # Мы вводим в текстовом поле для вопроса "Автор теории относительности"
        inputbox.send_keys('Автор теории относительности')
        

        # inputbox = self.browser.find_element(By.ID, 'id_new_item_answer')
        # self.assertEqual(inputbox.get_attribute('placeholder'), 'Введите ответ')
        # time.sleep(2)

        # # Мы вводим в поле для ответа ответ "Эйнштейн"
        # inputbox.send_keys('Эйнштейн')

        # Когда мы нажимаем Enter, страница обновляется и теперь 
        # страница содержит "Вопрос: Автор теории относительности. Ответ: Эйнштейн" 
        inputbox.send_keys(Keys.ENTER)
       

        # self.wait_for_row_in_list_talbe('Вопрос: Автор теории относительности')
        # self.check_for_row_in_list_talbe('Ответ: Эйнштейн')               
        
    
        # Когда мы нажимаем Enter, страница обновляется и теперь страница содержит "Вопрос: Автор теории относительности. Ответ: Эйнштейн". Ниже
        # находится кнопка подтвердить.
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(3)

        # table = self.browser.find_element(By.ID, 'id_answer_table')
        # rows = table.find_elements(By.TAG_NAME, 'tr')
        # self.assertTrue(any(row.text == 'Эйнштейн' for row in rows))
        # 

        # Мы нажимаем кнопку, страница обновляется и появляется надпись "Запись внесена. Хотите добавить запись?" Внизу две кнопки Добавить и Далее.

        # Мы нажимаем кнопку Добавить и появляется текстовое поле с предложением ввести новую запись.
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Введите вопрос')
        # Мы вводим в текстовом поле "Дата начала 2-й мировой войны"
        inputbox.send_keys('Дата начала 2-й мировой войны')

        # Когда мы нажимаем Enter, страница обновляется и теперь страница содержит "Вопрос: Дата начала 2-й мировой войны. Введите ответ" с полем для ответа
        inputbox.send_keys(Keys.ENTER)
        # Мы вводим в поле для ответа ответ "1939 год"

        # Когда мы нажимаем Enter, страница обновляется и теперь страница содержит "Вопрос: Дата начала 2-й мировой войны. Ответ: 1939 год". Ниже
        # находится кнопка подтвердить.
        self.wait_for_row_in_list_talbe('Вопрос: Автор теории относительности')
        self.wait_for_row_in_list_talbe('Вопрос: Дата начала 2-й мировой войны')
        # Мы нажимаем кнопку, страница обновляется и появляется надпись "Запись внесена. Хотите добавить запись?" Внизу две кнопки Добавить и Далее.
        # self.fail('Закончить тест')
        # Мы нажимаем кнопку Далее.

        # Мы проверяем, сохранились ли наши записи

        # Мы видим, что сайт сгенерировал уникальный URL-адрес - об этом выводится текст с пояснением.

        # Мы посещаем эти URL-адреса - наши записи там.

    def test_layout_and_styling(self):
        '''тест макета и стилевого оформления'''
        # пользователь открывает домашнюю страницу
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Он замечает, что поле ввода аккуратно центрировано
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2,
                               510,
                               delta=20)
        
        # Он начинает новый список и видит, что поле ввода там тоже
        # аккуратно центрировано
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_talbe('Вопрос: testing')
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] /2,
            512,
            delta=10
        )


    def test_multiple_users_can_start_lists_at_different_urls(self):
        '''тест: многочисленные пользователи могут начать списки по разным url'''
        # 1-й пользователь начинает новый список
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Автор теории относительности')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_talbe('Вопрос: Автор теории относительности')

        # он замечает, что его список имеет уникальный URL-АДРЕС
        first_user_list_url = self.browser.current_url
        self.assertRegex(first_user_list_url, '/lists/.+')

        # 2-й пользователь пришел на сайт
        # Мы используем новый сеанс браузера, чтобы никакая информация от 1-го
        # пользователя не прошла через данные cookie 
        self.browser.quit()
        options = ChromeOptions()
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=options)

        # 2-й пользователь посещает домашнюю страницу. На ней нет признаков списка 1-го пользователя
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Автор теории относительности', page_text)
        self.assertNotIn('Дата начала 2-й мировой войны', page_text)

        # 2-й пользователь начинает новый список, вводя новый элемент
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Самый сложный язык')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_talbe('Вопрос: Самый сложный язык')

        # 2-й пользователь получает уникальный URL-адрес
        second_user_list_url = self.browser.current_url
        self.assertRegex(second_user_list_url, '/lists/.+')
        self.assertNotEqual(second_user_list_url, first_user_list_url)

        # Нет ни следа от списка 1-го пользователя
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text 
        self.assertNotIn('Дата начала 2-й мировой войны', page_text)
        self.assertIn('Самый сложный язык', page_text) 
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')     
