#номер 21 из полякова
##s = 'ЛЕТО'
##c = 0
##for a in s:
##    for b in s:
##        for x in s:
##            for z in s:
##                #print(a,b,x,z)
##                if a in 'ЛТ':
##                    c+=1
##print(c)

# или воспоьзуемся библиотекой itertools, который перебирает все вариации - комбинаторика

##from itertools import product #ПРОЧИТАТЬ СТАТЬЮ О ITERTOOLS 
##c = 0
##for a,b,x,d in product('лето', repeat = 4): # REPEAT НУЖЕН ЗДЕСЬ, ЧТОБЫ ВАРИАЦИИ БЫЛИ ДЛИНОЙ 4
##    if a in 'лт':
##        c+=1
##print(c)

#или еще упростим вариацию то есть воспользуемся таким понятием как массив,
#где мы будем обращать каждый элемент в массиве

##from itertools import product
##c = 0
##abc = 'лето'
##for w in product('лето', repeat = 4):
##    if w[0] in 'лт': #здесь мы обращаемся к 0 элементу из массива и узнаем
##        c+=1        #по услоивию что есть нечетные буквы
##print(c)

#номер 91

##from itertools import permutations #Для пермутации не нужно(в этом случае)
##c = 0                #repeat = 5, так как он сам все создает вариации, только прикол в том, что он исключает повторений
##for w in permutations('калий'):# поэтому, если в задании написано искучитльно 1 раз, то "пермутация"
##    w = ''.join(w)
##    if w[0] != 'й' and 'иа' not in w:        
##        c+=1
##print(c)

#номер 114
                   
##from itertools import permutations
##c = 0
##for w in permutations('АБАК'):
##    s = set()
##    w = ''.join(w)
##    if 'АА' not in w:
##        s.add(w)
##print(len(s))
#-----------
