'''
Сколько существует натуральных чисел, шестнадцатеричная запись которых содержит
6 знаков, не начинается с единицы и заканчивается на AB?
'''
#Незабудь переписать коды !!!
#5
##from itertools import permutations as per
##g = 0
##for w in per('РУЛЬКА'):
##    w = ''.join(w)
##    if w[0] != 'Ь' and 'УЬ' not in w and 'АЬ' not in w:
##        g+=1
##print(g) #ответ 0
##from itertools import permutations as per
##g = 0
##for w in per('АБРИКОС'):
##    w=''.join(w)
##    if 'АИ' not in w and'ИА' not in w and 'АО' not in w and 'ОА' not in w and 'ОИ' not in w and 'ИО' not in w:
##        if ('БР' not in w) and ('РБ' not in w) and ('БК' not in w) and ('КБ' not in w) and ('БС' not in w) and ('СБ' not in w) and ('СР' not in w) and ('РС' not in w) and ('КР' not in w) and ('РК' not in w) and ('КС' not in w) and ('СК' not in w) :
##            g+=1
##print(g)
##from itertools import product
##c = 0
##for w in product('ABCD', repeat = 3):
##    w =''.join(w)
##    if  'CB' not in w and 'BC' not in w or 'AD' in w:
##        c+=1
##        print(c,w)
'''
Из букв слова Р У С Т А М составляются 6-буквенные последовательности. Сколько можно
составить различных последовательностей, если известно, что в каждой из них содержится не менее
3 согласных?
'''
##from itertools import product
##c = 0
##count = 0
##for i in product('РУСТАМ',repeat = 6):
##    i = ''.join(i)
##    if (not 'УА' in i):
##        c+=1
##print(c)

'''
Сергей составляет 5-буквенные коды из букв Ж, А, Л, Е, Й. Буква Й может использоваться в коде не
более одного раза, при этом она не может стоять на первом месте, на последнем месте и рядом с
буквой Е. Все остальные буквы могут встречаться произвольное количество раз или не встречаться
совсем. Сколько различных кодов может составить Сергей?
'''
##from itertools import product
##c=0
##for w in product('ЖАЛЕЙ', repeat = 5):
##    w = ''.join(w)
##    if  (w.count('Й') == 1 or w.count('Й') == 0) and w[0] != 'Й' and w[-1] != 'Й' and ('ЕЙ' not in w and 'ЙЕ' not in w):
##        c+=1
##        print(w)
##print(c)
'''
Миша составляет 5-буквенные коды из букв С, А, К, У, Р, А. Каждая допустимая гласная буква
может входить в код не более одного раза. Сколько кодов может составить Миша?
'''

from itertools import product
c = 0
for w in product('САКУР', repeat = 5):
    w = ''.join(w)
    if  w.count('А') <= 1 and  w.count('У') <= 1 :
        c+=1
##    print(w)
print(c)

