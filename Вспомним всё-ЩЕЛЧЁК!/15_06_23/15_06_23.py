"""Задание взято с КЕГЭ (второй фипи 23 года)"""
#КИМ № 25019914 БР № 2832503195017

#2 Ответ: wxzy
# from itertools import product
# print('x y z w f')
# for x,y,z,w in product([0,1], repeat = 4):
#     f = int( not( (w or not(y)) and x) or (y == z))
#     if f == False:
#         print(x,y,z,w,f)

#5 Ответ:
"""новое задание с подвохом!!!!"""
# w = []
# for n in range(1,1000):
#     r = bin(n)[2:]
#     if r.count('1') % 2 == 0:
#         r = '1' + r[2:] + '0'
#     else:
#         r = '11' + r[2:] + '1'
#     if int(r,2) > 25:
#         w += [int(r,2),n]
# w.sort()
# print(w)

#6 Ответ: 72
# from turtle import *
# screensize(1000,1000)
# left(90)
# m = 10
# speed(0)
# color('black','red')

# begin_fill()
# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(20*m)
#     right(90)
# penup()
# forward(3*m)
# right(90)
# forward(7*m)
# left(90)
# pendown()
# for i in range(2):
#     forward(70*m)
#     right(90)
#     forward(90*m)
#     right(90)

# penup()
# for x in range(0*m,50*m,m):
#     for y in range(-10*m,12*m,m):
#         goto(x,y)
#         dot(3,'black')
# mainloop()

#8 
"""
Определите количество шестизначных чисел, записанных в семеричной системе счисления,в записи 
которых ровно одна цифра 6, при этом чётные и нечётные цифры чередются
Решение ручками!!!
"""
# from itertools import product

# for w in product('0123456',repeat= 6):
#     w = ''.join(w)
#     if w[0] != '0' and w.count('6') == 1 and 

#12 6044 Ответ 1
# def f(n):
#     while '888' in n or '2222' in n:
#         if '2222' in n :
#             n = n.replace('2222','88',1)
#         else:
#             n = n.replace('888','22',1)
#     return n
# a = 120 * '8'
# print(f(a).count('8')) 
# print(f(a))

#14 Ответ; 29
# a = 3 * 1024**75 + 2*256**76 - 16**77 - 2023
# w = []
# while a != 0:
#     w.append(a%32)
#     a//=32
# print(w.count(0))

#15 6047 Ответ:6
# for a in range(1,1000):
#     f = True
#     for x in range(1,1000):
#         for y in range(1,1000):
#             g = (x > a) or (y > a) or (y - 2*x + 12 != 0)
#             if g == False:
#                 f =False
#                 break
#         if f == False:
#             break
#     if f == True:
#         print(a)

#16 Овтет: 42
# def f(a):
#     if a < 3:
#         return 1 
#     if a > 2 and a % 2 == 0:
#         return f(a-1)+2*a - 1
#     if a > 2 and a % 2 != 0:
#         return f(a-2)+2*a
    
# for i in range(1,22):
#     f(i)
# print(f(21)-f(19))

#17  1600 -130873
# file = open("17_6049.txt")
# a = list(map(int,file.readlines()))
# mx9 = max([i for i in a if abs(i) % 10 == 9])
# c = 0
# mn = 10**10
# for i in range(len(a)-1):
#     if (abs(a[i]) % 10 == 9 and abs(a[i+1]) % 10 != 9 and (a[i]^2 + a[i+1]^2) < mx9^2) or (abs(a[i]) % 10 != 9 and abs(a[i+1]) % 10 == 9 and (a[i]^2 + a[i+1]^2) < mx9^2):
#         c+=1
#         mn = min(mn,a[i]^2+a[i+1]^2)
# print(c,mn)

#19 Решение ручками : 
"""
Ходы:+2 *3
Камни: 1)5 2) 1<=s<=46
Победа: >=52
"""
# from functools import lru_cache
# @lru_cache(None)
# def game(x,y):
#     if x + y >= 52:
#         return 0
#     tmp = [game(x+1,y),game(x*3,y), game(x,y+1), game(x,y*3)]
#     neg = [i for i in tmp if i <= 0]
#     if len(neg) != 0:
#         return -max(neg) + 1
#     else:
#         return -max(tmp)
# for i in range(1,47):
#     r = game(5,i)
#     if r == -2:
#         print(i)