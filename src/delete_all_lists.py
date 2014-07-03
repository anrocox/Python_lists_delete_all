#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

How to delete all elements that have a list in python?

¿como eliminar todos los elementos que tiene una lista en python?
'''

#create a list
lista = ['hello', 'bye', 'hi']
print (lista)

#the clear() method allows delete all items of the list.
#this method is add in python 3
lista.clear()
print (lista)

#create a list
lista = [1, 2, 3, 4, 5]
print(lista)

#another way to clear list is using del
del lista[:]
print(lista)
