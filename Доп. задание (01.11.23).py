# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 22:23:17 2023

@author: user
"""
#Дополнительное задание от 25.10.23
x = int (input ('Введите число:'))
 
for d in range (1, x // 2 + 1) :
  if x % d == 0 :
    print (d, ' ', sep = '', end = '')
print (x)