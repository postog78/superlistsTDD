from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
    '''тест нового посетителя'''
    
    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        #Эдит слышала про крутое новое онлайн приложение со
        #список неотложных дел. Она решает оценить его
        #домашнюю страницу
        self.browser.get(self.live_server_url)
        
        #Она видит, что заголовок и шапка страницы говорят о
        #списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #Ей сразу же предлагается ввести элемент списках
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #Она набирает в текстовом поле "Купить Павлиньи перья" (её хобби - вязание рыболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')
        #Когда она нажимает enter, страница обновляется, и теперь страница содержит "1: Купить павлиньи перья" в качестве элемента списках
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        #Текстовое поле по-прежнему предлагает ее добавить ещё один элемент 
        #Она вводит "Сделать мушку из павлиньих перьев"
        #(Эдит очень методична)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        #Когда она нажимает enter, страница обновляется, и теперь страница содержит "1: Купить павлиньи перья" в качестве элемента списках
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        self.assertIn('1: Сделать мушку из павлиньих перьев', [row.text for row in rows])
        #Страница снова обновляется, и теперь показывает оба элемента на ее списке

        #Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        #сайт сгенерировал для нее уникальный URL-адрес - об этом 
        #выводится небольшой текст с объяснением

        #Она посещает этот URL-адрес - ее список по-прежнему там.

        #Удовлетворенная она снова ложится спать
        self.fail('Закончить тест!')
    

if __name__ == '__main__':
    unittest.main(warnings='ignore')
