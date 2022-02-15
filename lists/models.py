from django.db import models

class List(models.Model):
    '''список элементов'''
    pass

class Item(models.Model):
    '''элемент списка'''
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

