#Урезанная функция по переводу систем счисления!
'''
def numbersystem(number,system):
    result = ''
    while number != 0:
        result = str(number % system) + result
        number //= system
    return result
print(numbersystem(20,2))
'''

#Функция,которая проверяет на простые числа:
'''
def is_Prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i+=1
    return True
'''

#Пример:
#16
'''
(П. Волгин) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число,
задан следующими соотношениями:
F(n) = 1 при n = 0
F(n) = 7·(n - 1) + F(n - 1) при n > 0
Сколько существует значений n на отрезке [2, 200], для которых значение функции F(n) является
простым числом?
'''
##def is_Prime(x):
##    i = 2
##    while i * i <= x:
##        if x % i == 0:
##            return False
##        i+=1
##    return True
##def f(n):
##    if n == 0:
##        return 1
##    if n > 0:
##        return 7*(n - 1) + f(n - 1)
##for i in range(2,201):
##    
##for x in range(1,10):
##    i = 2
##    while i * i <= x:
##        if x % i == 0:
##            з
##        i+=1
##    print('1')
##    print(x)

