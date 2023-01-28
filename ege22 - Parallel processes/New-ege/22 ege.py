from csv import reader
#1)
'''
def calc(d, id):
    if '0' in d[id]['rel']:
        return d[id]['time']
    
    mx = 0 #ГОВОРЯТ,ЧТО ВСЕ РАБОТАЮТ ПРОЦЕДУРЫ => MAХ В ПРОЦЕДУРЕ, НО ИЗВНЕ ОСТАВЛЯЕМ MAX
    for searchID in d[id]['rel']:
        t = calc(d, searchID)
        mx = max(mx,t)
    d[id]['rel'] = ['0']
    d[id]['time'] += mx
    return d[id]['time']

f = open('22-1.csv')
rdr = reader(f, delimiter = ';', quotechar = '"')
d = {} # словарь
for id, time, rel, empty in rdr: ## empty зависит от файла, надо смотреть
    d[id] = {'time': int(time), 'rel':[x.strip() for x in rel.split(';')]}
#strip убирает пробелы справа и слева, split разделяет пробелом вместо ;
#print(d)

mx = 0
for id in d:
    t = calc(d,id)
    mx = max(t, mx)
print(mx)
'''
#27)
#27) (PRO100 ЕГЭ) В файле 22-27.xls содержится информация о совокупности N вычислительных процессов, которые могут выполняться параллельно илипоследовательно…
#(Условие совпадает с условием задачи из демо-варианта 2023 года).
'''
def calc(d, id):
    if '0' in d[id]['rel']:
        return d[id]['time']

    mx = 0
    for sID in d[id]['rel']:
        t = calc(d, sID)
        mx = max(mx, t)
    d[id]['rel'] = ['0']
    d[id]['time'] += mx
    return d[id]['time']

f = open('22-27.csv')
rdr = reader(f, delimiter = ';', quotechar = '"')
d = {}
##ПЕРЕД ТЕМ КАК ПИСАТЬ EMPTY, НАДО ПРОВЕРИТЬ ЦИКЛОМ, СКОЛЬКО ЗНАЧЕНИЙ СУЩЕСТВУЕТ.
#ТАК КАК ТАМ ТРИ ЗНАЧЕНИЯ, ТО УБИРАЕМ ЧЕТВЕРТОЕ ЗНАЧЕНИЕ EMPTY
##for i in rdr:
##    print(i)
##    break

for id, time, rel in rdr:
    d[id] = {'time' : int(time), 'rel': [x.strip() for x in rel.split(';')]}

mx = 0
for id in d:
    t = calc(d,id)
    mx = max(t,mx)
print(mx)
'''
'''
for i in rdr:
    print(i)
'''

#29)
'''
def calc(d, id):
    if '0' in d[id]['rel']:
        return d[id]['time']

    mn = 10**10 #спрашивают ХОТЯ БЫ ОДНА ПРОЦЕДУРА => MIN В ПРОЦЕДУРЕ, НО ИЗВНЕ ПРОЦЕДУРЫ СОХРАНЯЕМ MAX
    for sID in d[id]['rel']:
        t = calc(d, sID)
        mn = min(mn, t)
    d[id]['rel'] = ['0']
    d[id]['time'] += mn
    return d[id]['time']

f = open('22-29.csv')
rdr = reader(f, delimiter = ';', quotechar = '"')
d = {}
##for i in rdr:
##    print(i)
##    break
for id, time, rel in rdr:
    d[id] = {'time' : int(time), 'rel': [x.strip() for x in rel.split(';')]}

mx = 0
for id in d:
    t = calc(d,id)
    mx = max(t,mx)
print(mx)
'''
#30)
'''
from pprint import pprint

def calc(d, id):
    if '0' in d[id]['rel']:
        return d[id]['time']
    a = []
    for sID in d[id]['rel']:
        t = calc(d,sID)
        a.append(t)
    a.sort()
    if len(a) % 2 == 0:
        mx = max(a[:len(a)//2])
    else:
        mx = max(a[:len(a)//2 + 1])
    d[id]['rel'] = ['0']
    d[id]['time'] += mx
    return d[id]['time']

f = open('22-30.csv')
rdr = reader(f, delimiter = ';', quotechar = '"')
d = {}
for id, time, rel in rdr:
    d[id] = {'time' : int(time), 'rel':[x.strip() for x in rel.split(';')]}
    pprint(d)

mx = 0
for id in d:
    t = calc(d, id)
    mx = max(t, mx)
print(mx)
'''
#31) #ЗА 25 СЕКУНД, НЕ ИЗВЕСТНО ОДИН ПРОЦЕССОР
#from pprint import pprint
'''
def calc(d, id):
    if '0' in d[id]['rel']:
        return d[id]['time']
    
    mx = 0 #ГОВОРЯТ,ЧТО ВСЕ РАБОТАЮТ ПРОЦЕДУРЫ => MAХ В ПРОЦЕДУРЕ, НО ИЗВНЕ ОСТАВЛЯЕМ MAX
    for searchID in d[id]['rel']:
        t = calc(d, searchID)
        mx = max(mx,t)
    d[id]['rel'] = ['0']
    d[id]['time'] += mx
    return d[id]['time']

f = open('22-31.csv')
rdr = reader(f, delimiter = ';', quotechar = '"')

d = {} # словарь
for id, time, rel in rdr:
    d[id] = {'time' : int(time), 'rel': [x.strip() for x in rel.split(';')]}

for i in range(1,12): #с условия 12
    d['12']['rel'] = [str(i)]
    copy = {}
    for key in d:
        copy[key] = d[key].copy()
    mx = 0
    for id in copy:
        t = calc(copy, id)
        mx = max(t, mx)
    
    if mx == 25:
        print(mx, i)
'''
#32)

