#Тренировочные задачи для себя
from itertools import product
'''
number 113
not a or ( b and not c)
number 114
'''
##from itertools import product
##print('a b c f')
##for a,b,c in product([0,1], repeat = 3):
##    f = not a or ( b and not c)
##    print(a,b,c,f)
'''
number 133
(not x and y and z) or (not x and not z)
'''
##from itertools import product
##print('x y z f')
##for x,y,z in product([0,1], repeat = 3):
##    f = (not x and y and z) or (not x and not z)
##    if f == True:
##        print(x,y,z,f)
'''или'''
##print('x y z f')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = (not x and y and z) or (not x and not z)
##            if f == True :
##                print(x,y,z,f)
'''
nuber 134
(not x and z) or (not (x) and not (y) and not (z))
'''
##print('x y z f')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = (not x and z) or (not (x) and not (y) and not (z))
##            if f == True:
##                print(x,y,z,f)
'''
number 138
x and ((not y) and z and w or y and (not w))
'''
##from itertools import product
##print('x y z w f')
##for x,y,z,w in product([0,1], repeat = 4):
##    f = x and ((not y) and z and w or y and (not w))
##    if f == True:
##        print(x,y,z,w,f)

'''
number 175
not(z or y) or (x == z)
nuber 178
not(not z or not y) or (x == z)
nuber 177
not(x or y)or(x == z)
'''
##from itertools import product
##print('x y z f')
##for x,y,z in product([0,1], repeat = 3):
##    f = not(x or y)or(x == z)
##    if f == False:
##        print(x,y,z,f)

'''
number 184
((not or y) and (not y or w) or (z ==( x or y))
'''
##from itertools import product
##print('x y z w f') #Проверял
##for y,w,z,x in product([0,1], repeat = 4):
##    f = ((not x or y) and (not y or w)) and (z ==(x or y))
##    if f == False:
##        print(y,w,z,x,f)

'''
nubmer 186
(x and y) or (not x and not z)
number 191
(x and not y) or (y == z) and w
'''
##from itertools import product
##print('y x w z f')
##for y,x,w,z in product([0,1], repeat = 4):
##    f = (x and not y) or (y == z) and w
##    if f == False :
##        print(y,x,w,z,f)


#134
'''
(not(x) and z) or (not(x) and not(y) and not(z))
'''
##from itertools import product
##print('w x y z f')
##for w,x,y,z in product([0,1], repeat = 4):
##    f = int((not(x == (not y))) or ((x and w) == z ))
##    if f == False:
##        print(w,x,y,z,f) 
    
'''
Ответ: w z y x f - maybe
((z → y) ∧ (¬ x → w)) → ((z ≡ w) ∨ (y ∧ ¬ x))
'''
##print('x y z w f')
##for x,y,z,w in product([0,1], repeat = 4):
##    f = int( not((not(z) or y)and(x or w))or ((z == w) or (y and not(x))) )
##    if f == False:
##        print(x,y,z,w,f)
