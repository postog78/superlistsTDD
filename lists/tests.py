from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):
    '''тест домашней страницы'''
    
    def test_home_page_returns_correct_html(self):
        '''тест: домашня страница возвращает правильный html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

# Create your tests here.
