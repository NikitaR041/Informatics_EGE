#интересная задачка из файла 26,09,2022
# ege 12
'''
Исполнитель Редактор строк работает со строками и числами. Редактор строк может выполнять следующие
функции:
Длина(a) – возвращает количество символов в строке a.
Извлечь(a, i) – возвращает i-тый (слева) символ в строке a (нумерация с 1).
Склеить(a, b) – возвращает строку, в которой записаны сначала все символы строки a, а затем все символы строки b.
Дан фрагмент алгоритма на школьном алгоритмическом языке:
--
Какое значение будет у переменной b после выполнения вышеприведенного фрагмента? В от-вете укажите значение
переменной без кавычек.

'''
##a = '101101'
##i = 1
##b = ''
##while i <= len(a):
##    #print(len(a))
##    c = a[i-1]#нужно сравнивать строку со строкой !!!!
##    print(a[i-1])
##    if c == '1':
##        b = b + '0'
##    if c == '0':
##        b = b + '1'
##    i = i + 1
##print(b)

'''
Известно, что исходная строка содержала более 100 единиц и не содержала других цифр. Укажите
минимально возможную длину исходной строки, при которой в результате работы этой программы
получится строка, содержащая минимально возможное количество единиц.
'''
##смотреть, там где нет вообще 1
##for i in range(101,500):
##    a = '1' * i
##    while '1111' in a :
##        a = a.replace('1111','2',1)
##        a = a.replace('22','11',1)
##    print(i, a) ## ответ 106


'''
Дана строка, состоящая из 500 цифр 5. Сколько троек было удалено за время обработки строки по
этой программе?
'''
##def f(a):
##    c = 0
##    while '555' in a or '333' in a:
##        if '333' in a:
##            a = a.replace('333','5',1)
##            c+=1
##        else:
##            a = a.replace('555','3',1)
##    return c
##a = '5' * 500
##print(f(a))
###или
##c = 0
##a = '5' * 500
##while '555' in a or '333' in a:
##    if '333' in a:
##        a = a.replace('333','5',1)
##        c+=1 #(5)
##    else:
##        a = a.replace('555','3',1)
##print(c)

'''
другая задча
'''
##def f(a):
##    while '111' in a:
##        a = a.replace('111','2',1)
##        a = a.replace('222','1',1)
##    return a
##for i in range(40,100):
##    a = '1' * i
##    if f(a) == '11':
##        print(i)

'''
Другая задача
'''
##def f(a):
##    while '555' in a:
##        a = a.replace('5555','33',1)
##        a = a.replace('333','5',1)
##    return a
##a = '5' * 150
##print(f(a))

'''
НАЧАЛО
 ПОКА нашлось (13) ИЛИ нашлось (32) ИЛИ нашлось (12)
 ЕСЛИ нашлось (13)
 ТО заменить (13, 31)
 КОНЕЦ ЕСЛИ
 ЕСЛИ нашлось (32)
 ТО заменить (32, 23)
 КОНЕЦ ЕСЛИ
 ЕСЛИ нашлось (12)
 ТО заменить (12, 21)
 КОНЕЦ ЕСЛИ
 КОНЕЦ ПОКА
КОНЕЦ

На вход приведённой ниже программе поступает строка, содержащая 50 цифр 1, 50 цифр 2 и 50 цифр
3, расположенных в произвольном порядке. Запишите без разделителей символы, которые имеют
порядковые номера 10, 70 и 140 в получившейся строке.

Идея: порядковые нумера идут с 0 значения, поэтому -1 надо делать (10 - 1 = 9, 70 - 1 = 69, 140 - 1 = 139; -> позиции, которые нужно посмотреть)
'''
##n = '1'*50 + '2'*50 + '3'*50
##while '13' in n or '32' in n or '12' in n:
##    if '13' in n:
##        n = n.replace('13','31',1)
##    elif '32' in n:
##        n = n.replace('32','23',1)
##    elif '12' in n:
##        n = n.replace('12','21',1)
###print(n[10],n[70],n[140])
##print(n[9],n[69],n[139]) #Так как нумерация идет с нуля
