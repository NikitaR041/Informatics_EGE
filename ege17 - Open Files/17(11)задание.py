# 11 zadanie посмотри фотку влада

file = open('17-4.txt')
a = list(map(int, file.readlines()))
srd = sum(a)/len(a)
c = 0
mn = 10**10

for i in range(len(a)- 1):
    if ((a[i] < srd) or (a[i+1] < srd)):
        if ((a[i] % 7 == 0 and a[i] % 3 != 0 and a[i] % 11 != 0 and a[i] % 13 != 0 ) or ((a[i+1] % 7 == 0 and a[i+1] % 3 != 0 and a[i+1] % 11 != 0 and a[i+1] % 13 != 0 )) :
            c +=1
            mn = min(mn, a[i] + a[i+1])
print(c,mn)
    









