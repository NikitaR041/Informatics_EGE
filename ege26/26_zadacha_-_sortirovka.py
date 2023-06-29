#Пример решения
'''
f = open('26.txt')
s,n = map(int, f.readline().split())# n  - не нужно
a = list(map(int, f.readlines()))# Закидвывает в список
a.sort() # a = sorted(a)  от меньшего к большому
i = 0
s1 = 0
c = 0 
#Максимум пользователей, которые можно взять
while s1 + a[i] <= s:
    s1+=a[i]
    i+=1
    c+=1

s1 -= a[i - 1]

while s1 + a[i] <= s :
    i+=1

print(c,a[i - 1])
'''
#21
f = open('26.txt')
s, k = map(int, f.readline().split())
a = list(map(int, f.readlines()))
a.sort()
s1 = 0
for i in range(k):
    s1 = a.pop()
print(a[-1], int(s1*0,2))
