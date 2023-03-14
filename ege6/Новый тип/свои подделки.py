from turtle import *
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
##
##left(90)
##color('red','blue')
##m = 50
##speed(1)
##
##begin_fill()
##for i in range(4):
##    for j in range(3):
##        forward(2 * m)
##        right(270)
##    forward(5*m)
##end_fill()
##
##mainloop()

#8)---------------------------------------------------------------------------------
'''
Повтори 2 [Вперёд 6 Направо 90 Вперёд 8 Направо 90]
Поднять хвост
Вперёд 2 Направо 90 Вперёд 1 Налево 90 
Опустить хвост
Повтори 2 [Вперёд 3 Направо 90 Вперёд 4 Направо 90]

Выполняя этот алгоритм, Черепаха рисует одну за другой две фигуры. Определите, сколько точек с
целочисленными координатами будут находиться внутри первой нарисованной фигуры, но не внутри
второй. Точки на границах указанной области следует учитывать.

'''
##left(90)
##m = 10
##speed(0)
##color('blue','red')
##
##begin_fill()
##for i in range(2):
##    forward(6 * m)
##    right(90)
##    forward(8 * m)
##    right(90)
##penup()
##forward(2 * m)
##right(90)
##forward(1 * m)
##left(90)
##pendown()
##for j in range(2):
##    forward(3 * m)
##    right(90)
##    forward(4 * m)
##    right(90)
##end_fill()
##
###canvas = getcanvas()
##penup()
##for x in range(-1*m,80*m,m):
##    for y in range(-1*m,30*m,m):
##        goto(x,y)
##        dot(3,'green')
##
##mainloop() 

#9)---------------------------------------------------------------------------------------
'''
(Е. Джобс) Исполнитель Чертёжник перемещается на координатной плоскости, оставляя
след в виде линии. Чертёжник может выполнять команду Сместиться на (a,b) (где a,
b — целые числа), перемещающую Чертёжника из точки с координатами (x, y) в точку с
координатами (x+a, y+b). Если числа a, b положительные, то значение соответствующей
координаты увеличивается, если отрицательные — уменьшается. Например, если
Чертёжник находится в точке с координатами (4, 2), то команда Сместиться на (2,-3)
переместит Чертёжника в точку (6,-1). Запись
Повтори k раз
 Команда1 Команда2 Команда3
конец
означает, что последовательность Команда1 Команда2 Команда3 повторится k раз.
Чертёжнику был дан для исполнения следующий алгоритм:
Повтори 10 раз
 Сместиться на (4, 3)
 Сместиться на (-4, 10)
 Сместиться на (18, -12)
 Сместиться на (-24, -12)
конец
Перед началом алгоритма Чертёжник находился в точке с координатами (0, 0). Определите
количество точек с целочисленными координатами, которые принадлежат получившейся
линии.

Идея:
Берем только те, которые попали на линии на первом цикле получилось 21 штука
ВНИМАНИЕ!!!!!! НЕ БЕРИ НА ПЕРВОМ ЦИКЛЕ ПОСЛЕДНЮЮ ТОЧКУ, КОТОРАЯ ЗАДАЕТ НОВЫЙ ВИТОК ЦИКЛА, Т.К. ЭТО ПРОДОЛЖЕНИЕ НОВОГО ВИТКА
ВНИМАНИЕ!!!! ТАК КАК МЫ УКАЗАЛИ ОДИН ЦИКЛ ОДНОГО ВИТКА, ТО ИХ ВСЕГО 10 ЦИКЛОВ - 10 ВИТКОВ, ПОЛУЧАЕТСЯ 21 * 10 = 210
ОДНАКО, вНиМаНиЕ !!! ПОСЛЕДНЮ ТОЧКУ НАДО БРАТЬ!!!! ТАК КАК ОН НЕ ЗАДАЕТ НОВЫЙ ВИТОК - НА ЭТОМ ВИТКЕ ЦИКЛ ЗАКАНЧИВАЕТСЯ!!!
'''
left(90)
m = 25 #Лучше увеличить масчштаб
speed(0)
tracer(2)
color('blue','red')

x = 0
y = 0
begin_fill()
for _ in range(1): #Так как один цикличный рисунок
    x += 4
    y += 3
    goto(x * m, y *m)
    x += -4
    y += 10
    goto(x * m, y * m)
    x += 18
    y += -12
    goto(x * m, y * m)
    x += -24
    y += -12
    goto(x * m, y * m)
end_fill()
penup() #Поднять хвост

for x in range(-10,20):
    for y in range(-20,15):
        goto(x *m,y * m)
        dot(4)
        
mainloop()
