#Пробник из С-Пб взято из КЕГЭ КИМ № 25021833 БР № 2832503195017

#1 ответ 18

#2 ответ xzyw
# from itertools import product
# print('x y z w f')
# for x,y,z,w in product([0,1], repeat = 4):
#     f = int( not((not(x) or w) and (y or z)) or ((z==x) or (w and not(y))))
#     if f == False:
#         print(x,y,z,w,f)

#5)6588)  Овет: 32
# for n in range(1,1000):
#     r = bin(n)[2:]
#     r = r.replace('0','x')
#     r = r.replace('1','0')
#     r = r.replace('x','1')
#     r = '1' + r
#     if r.count('1') % 2 != 0:
#         r = r + '1'
#     else:
#         r = r + '0'
#     if int(r,2) > 180:
#         print(int(r,2),n)
 
#6
# from turtle import *
# left(90)
# m = 10
# speed(0)
# color('black','red')

# begin_fill()
# for i in range(5):
#     forward(16*m)
#     right(120)

# penup()
# for x in range(-5*m,20*m,m):
#     for y in range(-10*m,20*m,m):
#         goto(x,y)
#         dot(3,'black')

# mainloop()

#8)6591) 
"""
ОПРЕДЕЛИТЕ количество пятизначных чисел, записанных в семеричной системе счисления, в записи которых:
1) только одна цифра 6
2) сумма четных цифр числа меньше суммы нечётных цифр числа
"""
# from itertools import product
# c = 0
# s = set()
# for w in product('0123456',repeat = 5):
#     w = ''.join(w)
#     if w[0] != 0 and w.count('6') == 1 and (w.count('0')+w.count('2')+w.count('4')+w.count('6')) < (w.count('1')+w.count('3')+w.count('5')):
#         c+=1
#         s.add(w)
# print(c,len(s))

#12 6604) 245
"""
"""
# def f(n):
#     while ">1" in n or '>2' in n or '>3' in n:
#         if '>1' in n:
#             n = n.replace('>1','2>',1)
#         if '>2' in n:
#             n = n.replace('>2','3>',1)
#         if '>3' in n:
#             n = n.replace('>3','11>',1)
#     return n

# def dels(x):
#     a = []
#     i = 2
#     while i**2 <= x:
#         if i**2 == x:
#             a.append(i)
#         elif x % i == 0:
#             a += [i, x//i]
#         i+=1
#     return a
# # print(dels(6))
# c = 0 
# for m in range(0,500):
#     a = '>' + '1'*15 + '2'*35 + '3' * m
#     c+=1
#     # print(c,f(a)[:-1])
#     if len(dels(sum(map(int,f(a)[:-1])))) == 3:
#         print(m)

 
#14 6594) 22953
# for x in '0123456789ABC':
#     f = int('753'+x+'2',13) + int('2'+x+'173',13)
#     if f % 12 == 0:
#         print(f//12)

#15 6595) 2
# for a in range(1,1000):
#     f = True
#     for x in range(1,1000):
#         g = ((x % 3 != 0) or (x % 2 != 0)) or (x - a >= 4)
#         if g == False:
#             f = False
#             break
#     if f == True:
#         print(a)

# 16) 6596) 1083202575
# def f(x):
#     if x == 1:
#         return 1
#     if x > 1:
#         return f(x-1)*(2*x-3)
# for i in range(1,520):
#     f(i)
# print(f(516)/f(513))

#17 6605)
# file = open('17_6605.txt')
# a = list(map(int,file.readlines()))
# mx5 = max([i for i in a if abs(i) % 10 == 5]) #9985
# c = 0
# mn = 10**10
# mx = -10**10
# for i in range(len(a) - 1):
#     if (abs(a[i]) % 10 == 5 and abs(a[i+1])%10 != 5 and abs(a[i]^2 - a[i+1]^2)<=mx5^2) or (abs(a[i]) % 10 != 5 and abs(a[i+1])%10 == 5 and abs(a[i]^2 - a[i+1]^2)<=mx5^2):
#         c+=1
#         mx = max(mx, abs(a[i]-a[i+1]))
# print(c,mx)

#19) 6608)
"""
Кучи: s>=13
Ходы: -12 или //3(количество камней, полученное при делении, округляется до меньшего)
Победа: <=12
Известо, что Ваня выиграл своим первым ходом после неудачного хода Пети.
При каком максимальном значении S такое возможно?
"""
# from functools import lru_cache
# @lru_cache(None)
# def game(x):
#     if x <= 12:
#         return 0
#     tmp = [game(x-12), game(x//3)]
#     neg = [i for i in tmp if i <= 0]
#     if len(neg) != 0:
#         return -max(neg) +1
#     else:
#         return -max(tmp)
#1) Нужно было 12 * 3 = 36, потом +2 = 38, затем 38*3=114, затем +2 = 116
# for i in range(13,1000):
#     r = game(i)
#     if r == 2:
#         print(i)
# for i in range(13,1001): #длина 24
#     r = game(i)
#     if r == -2:
#         print(i)


#23 6635) 2224
"""
№ 6635 Пробник ИМЦ СПб (Уровень: Средний)
Исполнитель Троечка преобразует число, записанное на доске. У Троечки есть две команды:
1. Вычесть 3
2. Умножить на -3
Первая команда уменьшает число на 3, вторая команда умножает его на –3.
Сколько различных отрицательных результатов можно получить из исходного числа 333 в ходе исполнения программы,
содержащей ровно 13 команд?
"""
# s = set()
# def f(x,n):
#     if n == 13:
#         if x < 0:
#             s.add(x)
#         return 0
#     f(x-3, n+1)
#     f(x*(-3), n+1)
# f(333,0) #Вызываем f(333,0)
# print(len(s))
    

#25 6637)
"""
Идея
Предел 10? всего 6 цифр, тогда свободных 4 
В цикле пишем 3
"""
# from itertools import product
# a = []
# l = ['']
# c = 0
# for x in range(3):
#     l += [''.join(i) for i in product('0123456789', repeat = x + 1)]
# for x1 in range(10):
#     for x2 in l:
#         f = int('1'+str(x1)+'2139'+x2+'4')
#         if f % 3052 == 0:
#             a.append(f)
# a.sort()
# for i in a:
#     print(i,i//3052)