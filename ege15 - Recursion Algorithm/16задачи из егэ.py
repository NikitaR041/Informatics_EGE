#16 задачи из егэ с 11 по 12, 14 по 15:
#def f(n):
#    if n <= 5:
#        return n + 15
#    if n % 2 == 0 and n > 5:
#        return f(n//2)+ n*n*n - 1
#    if n % 2 != 0 and n > 5:
#        return f(n-1) + 2*n*n + 1
#c = 0
#for i in range(1,1001,1):
#    s = str(f(i))
#    if s.count('8') >= 2:
#        c+=1
#print(c)
#12
#def f(n):
#    if n < 3:
#        return n + 3
#    if n>=3 and n % 3 == 0:
#        return (n+2)*f(n-4)
#    if n>=3 and n % 3 != 0:
#        return n + f(n-1) + 2*f(n-2)
#print(f(20))
#14
#def f(n):
#    if n<=3 :
#        return n
#        return n + f(n-1)
#    if n % 2 != 0 and n > 3:
#        return n*n+f(n-2)
#n = 0
#while f(n) < 10**8:
#    n+=1
#print(n)
#15
##############from functools import lru_cache
##############@lru_cache
##############def f(n):
##############    if n < -100000:
##############        return 1
##############    if n > 10:
##############        return f(n-1) + 3 * f(n-3) + 2
##############    else:
##############        return -1 * f(n-1)
##############for i in range(-100000,21):
##############    f(i)
##############print(f(20))

##def f(n):
##    if n < 1:
##        return n
##    if n >= 1 and n % 2 == 0:
##        return n + 3 * f(n-3)
##    if n>= 1 and n % 2 != 0:
##        return 5*n + 2*f(n-5)
##print(f(30))

'''
Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:
F(0) = 1, F(1) = 3
F(n) = F(n–1) – F(n–2) + 3n, при чётном n > 1
F(n) = F(n–2) – F(n–3) + 2n, при нечётном n > 1
Чему равно значение функции F(40)? В ответе запишите только целое число.
'''
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n > 1 and n % 2 == 0:
        return f(n - 1) - f(n - 2)+ 3*n
    if n > 1 and n % 2 != 0:
        return f(n - 2) - f(n - 3)+ 2*n
print(f(40))

'''
Определите, сколько символов * выведет эта процедура при вызове F(35):
'''
#Создаем count = 0 (кол-во) и вместо print('*'), пишем count+=1
count=0
def F( n ):
  global count
  count+=1
  if n >= 1:
    count+=1
    F(n-1)
    F(n-2)
    count+=1
print(F(35))
print(count)

'''(К. Багдасарян)
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан
следующими соотношениями:
F(n) = 2, если n = 1,
F(n) = 2 · F(n – 1), если n > 1.
Чему равно значение выражения F(1900) / 21890?
'''
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 2 * f(n - 1)
for i in range(1901):
    f(i)
print(f(1900)/2**1890)
