# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:32:28 2024

@author: user
"""
def func(x, base):
    alphabet = "012346789ABCDEFGHIJKLMNOPQRTUVWXYZ"
    k = len(x)-1
    result = 0 
    for i in x:
        result+=alphabet.index(i)*(base**k)
        k-=1
        return result 
    y = func("108", 8)+func("5F", 37)*func("1011",3)**func("BA",15)
    
    print("Выражение в десятичной системе счисления", y)
    z = 0
    while y>=23:
        c=y%24
        y=y//24
        if с==17:
            z=z+1
            
    print("КОЛИЕСТВО БУКВ H В ЗНАЧЕНИИ ВЫРАЖЕНИЯ, ЗАПИСАННОГО В 24-ОЙ СИСТЕМЕ СЧИСЛЕНИЯ")
        

