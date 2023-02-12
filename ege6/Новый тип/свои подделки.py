'''
Определите, сколько точек с целочисленными координатами будут находиться внутри области,
ограниченной линией, заданной данным алгоритмом.
Точки на линии учитывать не следует.
'''
#1)
'''
from turtle import *
left(90)
m = 10
speed(1)
color('black','red') # Имеют id

begin_fill()
for i in range(3):
    forward(6*m)
    right(120)
end_fill()


c = 0
canvas = getcanvas() #Холст - теклитлер
#print(canvas.find_all()) (1, 5, 4, 2, 3) 
for x in range(-100*m,100*m,m):
    for y in range(-100*m,100*m,m):
        item = canvas.find_overlapping(x,y,x,y) #Создается холст прямоугольник
        
        if len(item) == 1 and item[0] == 5: # len(item) == 1 если я попадаю точкой в треугольник
            c+=1
print(c)
mainloop()
'''
#------------------------------------------------
'''
Определите, сколько точек с целочисленными положительными координатами будут находиться
внутри области, ограниченной линией, заданной данным алгоритмом.
Точки на линии учитывать не следует.

#3)
### СКАЗАНО ЧТО ПОЛОЖИТЕЛЬНЫЕ, поэтому считаем, только x > 0 and y > 0 !!!!!!
''''''
from turtle import *
left(90)
speed(5)
m = 50
color('green','red')

begin_fill()
for i in range(6):
    forward(4*m)
    right(60)

end_fill()
c = 0
canvas = getcanvas()
penup() # перо
for x in range(-5*m,8*m,m):
    for y in range(-5*m,8*m,m):
        item  = canvas.find_overlapping(x,y,x,y)
        goto(x,y)
        dot(3,'black')
        if len(item) == 1 and item[0] == 5:
            c+=1
print(c)
'''
#------------------------------------------------
#6)
'''
Определите, сколько углов у фигуры, ограниченной линией, заданной данным алгоритмом.
'''#24 угла
'''
from turtle import *
left(90)
m = 10
speed(5)
color('green','red')
begin_fill()
for i in range(12):
    right(60)
    forward(5*m)
    right(60)
    forward(5*m)
    right(270)

c = 0
canvas = getcanvas()
for x in range(-100*m,100*m,m):
    for y in range(-100*m,100*m,m):
        item = canvas.find_overlapping(x,y,x,y)

        if len(item) == 1 and item[0] == 5:
            c+=1
print(c)
'''
#-----------------------------------------------------------------------------------
#5)
'''
Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. 
Точки на линии учитывать не следует
'''
##from turtle import *
##left(90)
##m = 5
##speed(1)
##color('black','red') # Имеют id
##
##begin_fill()
##for i in range(4):
##    forward(12*m)
##    right(90)
##end_fill()
##
##c = 0
##canvas = getcanvas() #Холст - теклитлер
##for x in range(-100*m,100*m,m):
##    for y in range(-100*m,100*m,m):
##        item=canvas.find_overlapping(x,y,x,y)
##
##        if len(item) == 1and item[0] == 5:
##            c+=1
##print(c)
##mainloop()
#----------------------------------------------------------------------------------

#6)
'''
Повтори 10 [Вперёд 15 Направо 60]
Сколько существует точек с целочисленными координатами, лежащими на получившемся контуре?
'''
##from turtle import *
##
##left(90)
##color('red','blue')
##speed(50)
##m = 10
##
##begin_fill()
##for i in range(8):
##    forward(15*m)
##    right(60)
##end_fill()
##
##canvas = getcanvas()
##penup()
##for x in range(-10*m,80*m,m):
##    for y in range(-10*m,30*m,m):
##        goto(x,y)
##        dot(3,'black')
##
##mainloop() #Ответ убил, нужно пользоваться кумиром

#7)
'''
Повтори 4 [ Повтори 3 [ Вперед 2 Направо 270] Вперед 5]
Найдите сумму площадей замкнутых фрагментов фигуры
'''
from turtle import *

left(90)
color('red','blue')
m = 50
speed(1)

begin_fill()
for i in range(4):
    for j in range(3):
        forward(2 * m)
        right(270)
    forward(5*m)
end_fill()

mainloop()

