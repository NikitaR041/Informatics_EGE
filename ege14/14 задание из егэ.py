#задачи из егэ 14 с 7 по 10
for i in range(1,1000):
    s = ''
    k = 0
    x = 64 ** 12 - 8** 14 + i
    while x > 0:
        s = str(x%8) + s
        x //= 8
    if s.count('7') == 12 and s.count('1') == 1:
        print(i)
#8
a = 17**5 + 85**8 - 10
c = 0
while a > 0:
    if a % 17 == 16:
        c+=1
    a//=17
print(c)
#9
a = 7**103+20*7**204-3*7**57+97
c = 0
while a > 0:
    if a % 7 == 6:
        c+=1
    a//=7
print(c)
#10
