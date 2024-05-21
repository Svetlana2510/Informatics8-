# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:52:55 2024

@author: user
"""

#Результат выражения 4^3·3^19 записали в троичной системе счисления. 
#Напишите программу которая вычислит количество 0 в данной записи

def count_zeros():  
    result = 4**3 * 3**19
    ternary_result = ""
    while result > 0:
        ternary_result = ternary_result + str(result % 3)
        result //= 3
    zero_count = ternary_result.count("0")
    return zero_count

print("Количество нулей в данном числе:", count_zeros())
    