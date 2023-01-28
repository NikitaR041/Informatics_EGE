##from itertools import product #создаем так сказать перебор значений
##print('x y z w F')
##for x, y, z, w in product([0,1], repeat = 4):
##    # перебор различных чисел из 0 и 1 длиной 4
##    f = y and not x or not z or w
##    if not F:
##        print(x y z w F)

#((x and y) or ((not x) and (not z))) ИСТИННО
##print("x y z ")
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            if ((x and y) or ((not x) and (not z))):
##                print(x, y, z)
## или
##from itertools import product
##print("x y z f")
##for x,y,z,w in product([0,1], repeat = 3):
##    f = ((x and y) or ((not x) and (not z)))
##    if F == True:
##        print(x,y,z)

##from itertools import product
##print('x y z F')
####for x in range(2):
####    for y in range(2):
####        for z in range(2):
####            if (not x and y and z) or (not x and not z):
####                print(x,y,z)
##for x,y,z in product([0,1], repeat = 3 ):
##    f = (not x and y and z) or (not x and not z)
##    if f == True:
##        print(x,y,z,f)

##from itertools import product
##print('a b c d f')
##for a,b,c,d in product([0,1], repeat = 4):
##    f = ((a and b) == (not c)) and (not b or d)
##    if f == True :
##        print(a,b,c,d,f)

print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((not x) and y == z) and w):
                    print(x,y,z,w)
from itertools import product
print('x y z w f')
for x,y,z,w in product([0,1], repeat = 4):
    f = (((not x) and y == z) and w)
    if f == True:
        print(x,y,z,w,f)
