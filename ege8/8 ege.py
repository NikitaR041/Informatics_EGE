'''
    Раздел - здесь будут полезные советы

Первым делом нужно смотреть, есть ли потворы букв: 1)если есть используй set 2)Иначе не надо
Вторым делом пойми нужно использовать product или permutations из библиотеки itertools
Третьим делом посмотри у тебя СЛОВО или ЧИСЛО:
    если число, то возможно нужно использовать continue
1) contiue - такая команда, которая применяется для условий!(смотря как) К примеру посмотри на 11 пример из этого файла

2) set - такая коллекция(последовательность), которая исключает повторы элементов!
'''

'''
    Раздел - здесь будут примеры
'''

#1
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

#2
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

#3
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

#4
'''
Миша составляет 5-буквенные коды из букв С, А, К, У, Р, А. Каждая допустимая гласная буква
может входить в код не более одного раза. Сколько кодов может составить Миша?

Идея: По идеи нужно использовать set, но можно было ограничится тем, что в цикле просто не напишем вторую букву A
'''
##from itertools import product
##c = 0
##for w in product('САКУР', repeat = 5):
##    w = ''.join(w)
##    if  w.count('А') <= 1 and  w.count('У') <= 1 :
##        c+=1
####    print(w)
##print(c)

#5
'''582
Вася составляет 6-буквенные коды из букв Н, И, Г, Р, О, Л. Каждую букву нужно использовать
ровно 1 раз, при этом код не может начинаться с буквы О и не может содержать сочетания ОИГ.
Сколько различных кодов может составить Вася?

Идея:
Предложение "Каждую букву нужно использовать ровно 1 раз" означает, что нужно использовать permutations
'''
##from itertools import permutations as per
##c = 0
##for w in per('НИГРОЛ', r = 6):
##    w = ''.join(w)
##    if w[0] != 'О' and 'ОИГ' not in w:
##        c+=1
##print(c)

#6
'''840
Вася составляет слова из букв слова АТТЕСТАТ. Код должен состоять из 8 букв, и каждая буква в
нём должна встречаться столько же раз, сколько в заданном слове. Кроме того, в коде должны стоять
рядом две гласные или две согласные буквы. Сколько различных слов может составить Вася?

Идея:
1)Используй set в видим повторы букв - почему нужно?
    Потому что используется перестановка - есть шанс, что поменяются буквы, но так, что они для нас будут незаметны
2)"каждая буква в нём должна встречаться столько же раз, сколько в заданном слове" - используй permutations
'''
##from itertools import permutations as per
##s = set()
##for w in per('АТТЕСТАТ', r = 8):
##    w = ''.join(w)
##    if 'АА' in w or 'АЕ' in w or 'ЕА' in w or 'ТТ' in w or 'ТС' in w or 'СТ' in w:
##        s.add(w)#Добавляем в сет, чтобы отсеить такие же значения!
##print(len(s))

#7
'''96
Вася составляет слова из букв слова АББАТИСА. Код должен состоять из 8 букв, и каждая буква в
нём должна встречаться столько же раз, сколько в заданном слове. Кроме того, в коде не должны
стоять рядом две гласные и две согласные буквы. Сколько различных слов может составить Вася?
'''
##from itertools import permutations as per
##s = set()
##for w in per('АББАТИСА', r = 8):
##    w = ''.join(w)
##    if 'АА' not in w and 'АИ' not in w and 'ИА' not in w and 'ББ' not in w and 'БТ' not in w and 'ТБ' not in w and 'ТС' not in w and 'СТ' not in w and 'БС' not in w and 'СБ' not in w:
##        s.add(w)
##print(len(s))

#8
'''96
Вася составляет 7-буквенные коды из букв К, У, П, Ч, И, Х, А. Каждую букву нужно использовать
ровно 1 раз, при этом код не может начинаться с буквы Ч и не может содержать сочетания ИАУ.
Сколько различных кодов может составить Вася?
'''
##from itertools import permutations as per
##c = 0
##for w in per('КУПЧИХА', r = 7):
##    w =''.join(w)
##    if w[0] != 'Ч' and 'ИАУ' not in w :
##        c+=1
##print(c)

#9
'''
Из букв слова К А Н К А Н составляются 6-буквенные последовательности. Сколько можно
составить различных последовательностей, если известно, что в каждой из них содержится не менее
3 согласных?

ИДЕЯ: Здесь имеется ввиду про то, что не про каждый из согласных, а имеется ввиду в общем (в сумме) их должно быть
        не менее трёх!
'''
##from itertools import product
##s = set()
##for w in product('КАНКАН', repeat = 6):
##    w = ''.join(w)
##    if w.count('К') + w.count('Н') >= 3: #Не менее трёх
##        s.add(w)
##print(len(s))

#10
'''78
Вася составляет 5-буквенные коды из букв К, А, Л, И, Й. Каждую букву нужно
использовать ровно 1 раз, при этом код не может начинаться с буквы Й и не может
содержать сочетания ИА. Сколько различных кодов может составить Вася?

Идея:
1) Так как 'Каждую букву нужно использовать ровно 1 раз', используем permutations
'''
##from itertools import permutations as per
##c = 0
##for w in per('КАЛИЙ', r = 5):
##    w = ''.join(w)
##    if w[0] != 'Й' and 'ИА' not in w:
##        c+=1
##print(c)

#11
'''(А. Куканова)
Мила составляет 4-значные числа в 8-ичной системе. Сколько различных чисел, делящихся на 4
без остатка, может составить Мила?

Идея:
continue - такая команда, которую можно использовать в любое условие, но в такое, которое True в условии, то он пропускает и продолжает новую ИТЕРАЦИЮ!!!
1)Может быть такой случай, что 0004 или 0010 или 0100 и т.д. - эти все числа нам не подойдут!!!!
Должны подойти только такие числа от 1000 до 9999 !!!
'''
##c = 0
##for w in product('01234567',repeat = 4):
##    if w[0] == '0':
##        continue #НОВАЯ ИТЕРАЦИЯ!!!!
##    w = ''.join(w)
##    if int(w) % 4 == 0:
##        c+=1
##print(c)

#12 - ДОМАШКА возможный Ответ
'''
(А. Богданов) Оля составляет слова перестановкой букв слова СПОРТЛОТО, избегая слов с гласной и в
начале, и в конце слова. Все полученные различные слова Оля отсортировала по алфавиту и пронумеровала,
начиная с 1. Какой номер у последнего слова?
'''
from itertools import permutations
##a = set
##c = 0
##for w in product('СПОРТЛОТО',repeat = 9):
##    w = ''.join(w)
##    if w[0] != 'О' and w[-1] != 'О':
##        c+=1
##        


'''
    Раздел, которые нужно будет решить
'''
'''
*(Д. Статный) Григорий придумывает 16-буквенные слова, состоящие из букв слова АНТИУТОПИЯ.
Сколько слов, содержащих комбинацию АНТИУТОПИЯ, может составить Григорий, если справа от этой
комбинации согласные расположены в алфавитном порядке, а гласные – в обратном, а слева – гласные в
алфавитном порядке, а согласные – в обратном? Буквы в словах могут повторяться любое количество раз
или же не встречаться вовсе.
'''
##from itertools import product
##s = set()
##for w in product('АНТИУТОПИЯ', repeat = 16):
##    w = ''.join(w)
##    print(w)

# Автор: Д. Статный 138677
####
####from itertools import product
######Комбинацию АНТИУТОПИЯ примем за *
####k = 0
####for x in product(set('АНТИУОПИЯ*'), repeat=7):
####    s=''.join(x)
####    vowels = [x for x in s if x in 'АИОУЯ']
####    cons = [x for x in s if x in 'НТП']
####    if vowels==sorted(vowels) and cons==sorted(cons)[::-1] and s.count('*')==1:
####        k += 1
####print(k)

