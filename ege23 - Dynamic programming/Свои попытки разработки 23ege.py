#"Свои попытки к разработке в 23 задании"
#5)+1,+4,+5
##a = [0] * 100
##a[30]=1
##for i in range(30,47):
##    a[i+1]+=a[i]
##    a[i+4]+=a[i]
##    a[i+5]+=a[i]
##print(a[46]) ##Ответ 301

#6) +1, *3, *4
##a = [0] * 10000
##a[1]=1
##for i in range(1,26):
##    a[i+1]+=a[i]
##    a[i*3]+=a[i]
##    a[i*4]+=a[i]
##print(a[25]) #Ответ 38

#7) +3 , *2
##Сколько существует программ,для которых при исходном числе 12 результатом является число 96?
##a = [0] * 10000
##a[12] = 1
##for i in range(12, 97):
##    a[i+3]+=a[i]
##    a[i*2]+=a[i]
##print(a[96]) #Ответ 40

#10) +1, +3 2->20
##Сколько существует программ, для которых приисходном числе 2 результатом является число 20,
#и при этом траектория вычислений содержит число 10 и не содержит число 15?
##ДОРАБОТКА!!!!!
##a = [0] * 100
##a[2]=1
##for i in range(2,10):
##    if i + 1 <=10:
##        a[i+1]+=a[i]
##    if i + 3<=10:
##        a[i+3]+=a[i]
##for i in range(10,21):
##    a[15] = 0
##    a[i+1]+=a[i]
##    a[i+3]+=a[i]
##print(a[i])

#13) 2 -> 16
##a = [0] * 1000
##a[2] = 1
##for i in range(2,16):
##    a[i+1]+=a[i]
##    a[i*2]+=a[i]
##    a[(i*2)+1]+=a[i]
##print(a[16])

#16) 2 ->26,но содержит 11 и не содержит 21
# +1, +4, *2
##a = [0] * 1000
##a[2] = 1
##for i in range(2,11):
##    if i + 1<=11:
##        a[i+1]+=a[i]
##    if i + 4<=11:
##        a[i+4]+=a[i]
##    if i % 2 == 0:
##        a[i*2]+=a[i]
##    if i % 2 != 0:
##        a[i+1]+=a[i]
##for i in range(11,27):
##    a[21] = 0
##    a[i+1]+=a[i]
##    a[i+4]+=a[i]
##    if i % 2 == 0:
##        a[i*2]+=a[i]
##    else:
##        a[i+1]+=a[i]
##print(a[26])    

#20 55->6, -1, убрать последнюю цифру справа

##def f(x):
##    
##    s = bin(x)[2:]
##    del my_list[-1]
##    return int(s,2)
##a = [0]*100
##a[55] =1
##for i in range(55,5,-1):
##    a[i-1]+=a[i]
##    if f(i) != i:
##        a[f(i)]+=a[i]
##print(a[6])
#------------------------------------------------------------------------------------------------------------
#ИЗ ДЗ
#+1, +2,*2   1->28
##a = [0] * 100
##a[1]= 1
##for i in range(1,28):
##    a[i+1]+=a[i]
##    a[i+2]+=a[i]
##    a[i*2]+=a[i]
##print(a[28])

'''
Исполнитель Простачок преобразует число, записанное на экране. У исполнителя есть
три команды, которым присвоены номера:
1. Прибавить 2
2. Прибавить 3
3. Умножить на 2
Первая команда увеличивает число на 2, вторая – на 3, третья – увеличивает число вдвое. Сколько
различных чисел может быть получено из числа 10 всеми возможными алгоритмами длиной 5
команд?

s = set()
def f(x,l):
    global s
    if l == 5:
        s.add(x)
        return
    f(x+2,l+1)
    f(x+3,l+1)
    f(x*2,l+1)
f(10,0)
print(len(s))
'''
