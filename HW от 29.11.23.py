# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:52:23 2023

@author: user
"""

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print("Да")
else:
    print("Нет")