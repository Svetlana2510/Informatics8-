

def average(*args):
summa = 0      #summa, count равны нулю для посчета суммы и количества исел 
count = 0
for arg in args:
if isinstance(arg, (int, float)): #проверяет, является ли объект подходящим под свойства
summa += arg
count += 1
if count == 0:
return "свойство: параметры должены быть числами"
else:
return summa / count
