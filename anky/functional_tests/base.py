import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from unittest import skip
import time 


MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    '''функциональный тест'''
    def setUp(self):
        '''установка'''
        options = ChromeOptions()
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=options)
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

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



if __name__ == '__main__':
    unittest.main(warnings='ignore')     
