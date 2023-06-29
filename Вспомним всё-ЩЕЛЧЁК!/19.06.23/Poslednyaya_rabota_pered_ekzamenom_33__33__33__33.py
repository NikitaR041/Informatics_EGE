#Последняя работа перед экзаменом!!!! Никита повнимателней пожалуйста !!!!
# 1 25
# 2 yxwz 
# from itertools import product
# print('x y z w f')
# for x,y,z,w in product([0,1], repeat = 4):
#     f = int( (x and not(y)) or (x == z) or w)
#     if f == False:
#         print(x,y,z,w,f)

# 3 нужен файл!

# 4 ОТВЕТ 8
# 5 166
# a = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if n % 3 == 0:
#         r = r + r[-3:]
#     else:
#         r = r + bin((n%3)*3)[2:]
#     if int(r,2) < 170:
#         a.append(int(r,2))
# print(max(a))

#6  249
# from turtle import * 
# left(90)
# m = 10
# speed(0)
# color('black','red')

# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(18*m)
#     right(90)
# penup()
# forward(5*m)
# right(90)
# forward(7*m)
# left(90)
# pendown()
# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(7*m)
#     right(90)

# penup()

# for x in range(-5*m,20*m,m):
#     for y in range(-3*m,17*m,m):
#         goto(x,y)
#         dot(3,'red')

# mainloop()

# 7 288

#8 можно ручками или кодом! 6655 или 100810
# from itertools import product
# c = 0
# a = []
# for w in product('АГМНСТУ', repeat = 6):
#     w = ''.join(w)
#     c += 1
#     if w[0] != 'У' and w.count('М') == 2 and w.count('Г') == 0:
#         print(c,w)
#         a +=[[c,w]]
# print(a)

#9 файл
#10 файл
#11 2320 КБ
#12 186
# def f(x):
#     while '72' in x or '522' in x or '2222' in x:
#         if '72' in x:
#             x = x.replace('72','2',1)
#         if '522' in x:
#             x = x.replace('522','27',1)
#         if '2222' in x:
#             x = x.replace('2222','5',1)
#     return x
# for n in range(4,10000):
#     a = '5' + '2' * n
#     if sum(map(int,f(a))) == 63:
#         print(n)

#13 23

#14 470402599
# a = 'qwertyuiopasdfghjklzxcvbnm'
# a = sorted(a) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(a)
# for x in '0123456789ABCDEFGHI':
#     f = int('98'+x+'79641',19)+int('36'+x+'14',19)+int('73'+x+'4',19)
#     if f % 18 == 0:
#         print(f//18)  

#15 Ответ при 0 ->17; инача ответ 17  
# for a in range(0,1000):
#     f =True
#     for x in range(0,1000):
#         for y in range(0,1000):
#             g = (x < a) or (y < a) or (x + 2*y > 50)
#             if g == False:
#                 f = False
#                 break
#         if f ==False:
#             break
#     if f == True:
#         print(a)

#16 6069
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n < 11:
#         return n
#     if n >= 11:
#         return n + f(n-1)
    
# for i in range(1,2025):
#     f(i)
# print(f(2024)-f(2021))

#19
"""
Ходы: +1 +4 *3
Победа: >= 88
одна куча: 1<=s <= 87
1) 29
2)25 28
3)24
"""
# from functools import lru_cache
# @lru_cache(None)
# def game(x):
#     if x >= 88:
#         return 0
#     tmp = [game(x+1),game(x+4),game(x*3)]
#     neg = [i for i in tmp if i <= 0]
#     if len(neg) != 0:
#         return -max(neg) + 1
#     else:
#         return -max(tmp)
# for i in range(1,88): 
#     r = game(i)
#     if r == -2:
#         print(i) 

#23 90
# def f(x,y):
#     if x > y or x == 17:
#         return 0
#     if x == y:
#         return 1
#     return f(x+2,y)+f(x+3,y)+f(x*2,y)
# print(f(3,10)*f(10,25))

#24
"""
Текстовый файл состоит из символов T,U,V,W,X,Y,Z.
Определите в прилагаемом файле максимальное количество идущих подряд символов (длину непрерывной
подпоследовательности), среди которых символ Y встречается не более 150 раз.
Для выполнения этого задания следует написать программу.
"""

#25
"""
321657 159
34105757 16859
35117257 17359
36128757 17859
37140257 18359
38151757 18859
39163257 19359
"""
# from itertools import product
# a = []
# l = ['']
# for x in range(3):
#     l += [''.join(i) for i in product('0123456789', repeat = x + 1)]
# for x1 in range(10):
#     for x2 in l:
#         f = int('3'+ str(x1) + '1' + x2 + '57')
#         if f  % 2023 == 0:
#             a.append(f)
# a.sort()
# for i in a:
#     print(i,i//2023)