# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:21:46 2024

@author: user
"""

print("Введите число:")
x = int(input())
y = 2
while y <= x:
  if x % y == 0 and y!=x:
      print("Нет")
      break
  y += 1
  if y == x:
      print("Да")