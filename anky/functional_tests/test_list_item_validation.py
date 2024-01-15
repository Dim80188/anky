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
from .base import FunctionalTest



class ItemValidationTest(FunctionalTest):
    '''тест валидации элемнта списка'''
    def test_cannot_add_empty_list_items(self):
        '''тест: нельзядобавлять пустые элементы списка'''
        # Пользователь открывает домашнюю страницу и случайно пытается отправить
        # пустой элемент списка. Он нажимает Enter на пустом поле ввода
        # Домашняя страница обновляется и появляется сообщение об ошибке,
        # которое говорит, что элемнты списка не должны быть пустыми
        # Он пробует снова, теперь с неким текстом для элемента, и теперь
        # это срабатывает
        # Как ни странно, пользователь решает отправить второй пустой элемент списка
        # Он получает аналогичное предупреждение на странице списка
        # И он может его исправить, заполнив поле неким текстом
        self.fail('напиши меня!')


        


