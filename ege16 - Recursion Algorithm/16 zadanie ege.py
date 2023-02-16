##def f(n):
##    if n == 1:
##        return 1
##    if n > 1:
##        return 3*f(n-1)+g(n-1) - n + 5
##
##def g(n):
##    if n == 1:
##        return 1
##    if n > 1:
##        return f(n-1) + 3*g(n-1) - 3*n
##
##print(f(14)+g(14))
##17
##def f(s):
##    if int(s, 2) > 500000000:
##        return 0
##    if s.count('1') == 2:
##        return f(s+'0')+1
##    else:
##        return f(s+'0')+f(s+'1')
##
##print(f('1'))

##def f(n):
##    if n < 5:
##        return 1+2*n
##    if n >= 5 and n % 3 == 0:
##        return 2*(n+1) * f(n-2)
##    if n >= 5 and n % 3 !=0:
##        return 2*n + 1 + f(n-1) + 2*f(n-2)
##print(f(15))

##def f(n):
##    if n > 12:
##        return 2*n - 5
##    if  n <= 12:
##        return 2 * f(n+2) + n - 4
##print(f(1))
'''
Назовите максимальное значение n, для которого возможно вычислить F(n)
'''
##c = 0
##def f(n):
##    global c
##    c+=1
##    if c == 900:
##        return 0
##    if n <= 5:
##        return n
##    if n > 5 and n % 4 == 0:
##        return n+ f( n // 2 - 1)
##    if n > 5 and n % 4 != 0:
##        return n + f(n + 2)
##for i in range(1,100000):
##    c = 0
##    x = f(i)
##    if c < 900:
##        print(i)

#Var 10
'''
Назовите минимальное значение n, для которого f(n) равно 31
'''
##def f(n):
##    if n < 2 :
##        return 1
##    if n >= 2 and n % 2 == 0:
##        return f(n/2) + 1
##    if n >= 2 and n % 2 != 0:
##        return f(n - 3) + 3
##for i in range(1, 1000):
##    if f(i) == 31:
##        print(i)
'''
Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими
соотношениями:
F(n) = 1, при n < 2,
F(n) = F(n/2) + 1, когда n ≥ 2 и чётное,
F(n) = F(n - 3) + 3, когда n ≥ 2 и нечётное.
Назовите количество значений n на отрезке [1;100000], для которых F(n) равно 12
'''
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 2:
        return 1
    if not(n % 2):
        return f(n/2) + 1
    return f(n-3) + 3


c = 0
for i in range(1,100000):
    if f(i) == 12:
        c += 1
print(c)
#otvet 26

'''
. Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими
соотношениями:
F(n) = n, при n ≤ 3
при n > 3:
 F(n) = n + 3 + F(n–1), при чётном n;
 F(n) = n*n + F(n-2), при нечётном n;
Определите количество натуральных значений n на отрезке [1; 1000], при которых F(n) кратно 7.
'''
def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return n + 3 + f(n - 1)
    if n > 3 and n % 2 != 0:
        return n*n + f(n-2)
c = 0
for n in range(1,1001):
    if f(n) % 7 == 0:
        c+=1
print(c)

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
print(f(40)) # otvet 84
