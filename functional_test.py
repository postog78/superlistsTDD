from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
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
        self.browser.get('http://localhost:8000')
        
        #Она видит, что заголовок и шапка страницы говорят о
        #списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')

            #Ей сразу же предлагается ввести элемент списках

            #Она набирает в текстовом поле "Купить Павлиньи перяь" (её хобби - вязание рыболовных мушек)

            #Когда она нажимает enter, страница обновляется, и тперерь страница содержит "1: Купить павлиньи перья" в качестве элемента списках

            #Текстовое поле по-прежнему предлагает ее добавить ещё один элемент 
            #Она вводит "Сделать мушку из павлиньих перетье"
            #(Эдит очень методична)

            #Страница снова обновляется, и теперь показывает оба элемента на ее списке

            #Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
            #сайт сгенерировал для нее уникальный URL-адрес - об этом 
            #выводится небольшой текст с объяснением

            #Она посещает этот URL-адрес - ее список по-прежнему там.

            #Удовлетворенная она снова ложится спать

if __name__ == '__main__':
    unittest.main(warnings='ignore')