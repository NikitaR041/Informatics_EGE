#5)

from turtle import *
from math import sqrt, fabs, tan,sin, pi ##для 4.5
'''
Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом.
Точки на линии учитывать не следует. ВАЖНО
'''
'''
left(90)
speed(1)
m = 10
color('black','red')
begin_fill() #Начало заливки

for i in range(4): ## По условию 8 раз, а нужно так чтобы один раз рисовалась
    forward(12*m) #Вперед на 12 * на масштаб
    right(90)
end_fill()#заканчивает рисовку


canvas = getcanvas()#холст - текитлер
##print(canvas.find_all())#Что выводит Id деталей,располоденных на холсте 

c  = 0
for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = canvas.find_overlapping(x,y,x,y)#создали обьект, за счет которого есть ли у него пересечения с какими-то перечесением
                                                #Выводит id
        if len(item)==1 and item[0] == 5:
            c+=1
print(c)
##Вообщем мы проверяем касается ли он этого прямоугольника(накладываются), находит пересечение            


mainloop()#сохраняет окно открытым
'''
##Id 1 2 3  это относится к черепахе, а 4 это граница квадрата, 5 это заливка квадрата

        
#13)
'''
left(90);speed(1);m = 10; color('black','red')
begin_fill()

forward(200)
for i in range(3):
    right(90)
    forward(100)
end_fill()

canvas=getcanvas()

c=0
for x in range(-500,500):
    for y in range(-500,500):
        item = canvas.find_overlapping(x,y,x,y)
        if len(item) == 1 and item[0] > 3:
            c+=1                          
print(c)

#500+90*90 = 10301
'''
#14)
'''
left(90);m = 40; color('black','red')
begin_fill()

for i in range(6):
    forward(4*m)
    right(60)
end_fill()

canvas = getcanvas()

penup() # Поднять точку

c = 0
##for x in range(10):
##    for y in range(10):
##        if x > 0 and y < (1/3**0.5)*x + 4 and y < (- 1/3**0.5)*x + 4 and x < 4 and y > 0 :

for x in range(-1*m,8*m,m):
    for y in range(-1*m,8*m,m):
        item = canvas.find_overlapping(x,y,x,y)
        goto(x,y) #перехожит на координату 
        dot(10,'green') #рисует точки 1) ширина точки и цвет
        if len(item) == 1 and item[0] == 5:
            c+=1
print(c)
'''
# не считали ниже оси х и на линии х
'''
#идеи швацнегера
def line(a : float,b : float):
    x1,y1 = a
    x2,y2 = b
    return sort((x1-x2)**2+(y1-y2)**2)

def geron(a : float,b : float,c : float):
    p = (a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))
'''
##
#4) задача на проверку количество точек в многоульнике
'''
from math import sqrt, fabs

def line(a : float,b : float):
    x1,y1 = a
    x2,y2 = b
    return sqrt((x1-x2)**2+(y1-y2)**2)

def geron(a : float,b : float,c : float):
    p = (a+b+c)/2
    #return sqrt(p*(p-a)*(p-b)*(p-c))
    x = p*(p-a)*(p-b)*(p-c)
    if x < 0:
        return 0
    else:
        return sqrt(x)

left(90)

for i in range(3):
    right(60)
    forward(10)
    print(pos())
    right(60)

dots = [(0.00,0.00),(8.66,5.00), (8.66,-5.00), (-0.00,-0.00)]
s = sqrt(3) / 4 * 10 ** 2
#print(s)

#проевряет на маленькие части треугольника(пока что одного треугольника)
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s1 = 0
        zero = False
        for i in range(len(dots) - 1):
            l1 = line((x,y), dots[i])
            l2 = line((x,y), dots[i+1])
            l3 = line(dots[i], dots[i+1])

            tmp = geron(l1,l2,l3)
            s1 += tmp
            if tmp < 0.01:
                zero = True
        if fabs(s1 - s) < 0.01 and not zero:
            c+=1
print(c)
mainloop()
'''
#5 кол-во точек в фигуре
'''
def line(a : float,b : float):
    x1,y1 = a
    x2,y2 = b
    return sqrt((x1-x2)**2+(y1-y2)**2)

def geron(a : float,b : float,c : float):
    p = (a+b+c)/2
    #return sqrt(p*(p-a)*(p-b)*(p-c))
    x = p*(p-a)*(p-b)*(p-c)
    if x < 0:
        return 0
    else:
        return sqrt(x)

left(90)

for i in range(4):
    forward(12)
    print(pos())
    right(90)

dots = [(0.00,0.00),(0.00,12.00), (12.00,12.00), (12.00,0.00), (0.00,-0.00)]
#s = 144
#print(s)

#проевряет на маленькие части треугольника(пока что одного треугольника)
s = 12*12*4/(4*tan(pi / 4)) # это формула площади любого многоугольника, через сторону s = a**a * n/ 4 * tan(pi / n), где n - количество сторон, a - длина сторон
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s1 = 0
        zero = False
        for i in range(len(dots) - 1):
            l1 = line((x,y), dots[i])
            l2 = line((x,y), dots[i+1])
            l3 = line(dots[i], dots[i+1])

            tmp = geron(l1,l2,l3)
            s1 += tmp
            if tmp < 0.01:
                zero = True
        if fabs(s1 - s) < 0.01 and not zero:
            c+=1
print(c)
mainloop()
'''
#21 определить кол-во точек
'''
def line(a : float,b : float):
    x1,y1 = a
    x2,y2 = b
    return sqrt((x1-x2)**2+(y1-y2)**2)

def geron(a : float,b : float,c : float):
    p = (a+b+c)/2
    #return sqrt(p*(p-a)*(p-b)*(p-c))
    x = p*(p-a)*(p-b)*(p-c)
    if x < 0:
        return 0
    else:
        return sqrt(x)

left(90)

for i in range(2):
    left(60)
    forward(5)
    print(pos())
    left(120)
    forward(5)
    print(pos())
        

dots = [(0.00,0.00),(-4.33,2.50),(-4.33,-2.50),(-0.00,-5.00), (0.00,-0.00)]
#s = 144
#print(s)

#проевряет на маленькие части треугольника(пока что одного треугольника)
s = 2 * 1/2*sin(pi / 3) * 25 # это формула площади любого многоугольника, через сторону s = a**a * n/ 4 * tan(pi / n), где n - количество сторон, a - длина сторон
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s1 = 0
        zero = False
        for i in range(len(dots) - 1):
            l1 = line((x,y), dots[i])
            l2 = line((x,y), dots[i+1])
            l3 = line(dots[i], dots[i+1])

            tmp = geron(l1,l2,l3)
            s1 += tmp
            if tmp < 0.01:
                zero = True
        if fabs(s1 - s) < 0.01 and not zero:
            c+=1
print(c)
mainloop()
'''
#28
'''
def line(a : float,b : float):
    x1,y1 = a
    x2,y2 = b
    return sqrt((x1-x2)**2+(y1-y2)**2)

def geron(a : float,b : float,c : float):
    p = (a+b+c)/2
    #return sqrt(p*(p-a)*(p-b)*(p-c))
    x = p*(p-a)*(p-b)*(p-c)
    if x < 0:
        return 0
    else:
        return sqrt(x)

left(90)
m = 1

for i in range(1):
    forward(8 * m)
    print(pos())
    right(120)
    for j in range(2):
        forward(4*m)
        print(pos())
        right(60)
    forward(4*m)
    print(pos())
    right(120)
        

dots = [(0.00,0.00),(0.00,8.00),(3.46,6.00),(3.46,2.00),(0.00,-0.00)]
#s = 144
#print(s)

#проевряет на маленькие части треугольника(пока что одного треугольника)
s = (8 * m + 4 * m) / 2 * sqrt(12) # это формула площади любого многоугольника, через сторону s = a**a * n/ 4 * tan(pi / n), где n - количество сторон, a - длина сторон
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s1 = 0
        zero = False
        for i in range(len(dots) - 1):
            l1 = line((x,y), dots[i])
            l2 = line((x,y), dots[i+1])
            l3 = line(dots[i], dots[i+1])

            tmp = geron(l1,l2,l3)
            s1 += tmp
            if tmp < 0.01:
                zero = True
        if fabs(s1 - s) < 0.1 and not zero:
            c+=1
print(c)

mainloop()
'''
#30
def line(a : float,b : float):
    x1,y1 = a
    x2,y2 = b
    return sqrt((x1-x2)**2+(y1-y2)**2)

def geron(a : float,b : float,c : float):
    p = (a+b+c)/2
    #return sqrt(p*(p-a)*(p-b)*(p-c))
    x = p*(p-a)*(p-b)*(p-c)
    if x < 0:
        return 0
    else:
        return sqrt(x)

left(90)
m = 1

x, y = 0,0
for i in range(1):
    x,y = x + 3, y + 6
    goto(x,y)
    print(pos())
    x,y = x + 7, y - 2
    goto(x,y)
    print(pos())
    x,y = x - 10, y - 4
    goto(x,y)
    print(pos())

        

dots = [(0.00,0.00),(3.00,6.00),(10.00,4.00),(0.00,0.00)]
#s = 144
#print(s)

#проевряет на маленькие части треугольника(пока что одного треугольника)
s = geron(line(dots[0],dots[1]),line(dots[1],dots[2]),line(dots[2],dots[0])) #нашли площадь треугольника через координаты треугольника из dots
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s1 = 0
        zero = False
        for i in range(len(dots) - 1):
            l1 = line((x,y), dots[i])
            l2 = line((x,y), dots[i+1])
            l3 = line(dots[i], dots[i+1])

            tmp = geron(l1,l2,l3)
            s1 += tmp
            if tmp < 0.01:
                zero = True
        if fabs(s1 - s) < 0.1 and not zero:
            c+=1
print(c)

mainloop()
