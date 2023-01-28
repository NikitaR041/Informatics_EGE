#задачи 12 из егэ с 1 по 5
def f(a):
    while '63' in a or '664' in a or '6665' in a:
        if '63' in a :
            a = a.replace('63','4', 1)
        elif '664' in a:
            a=a.replace('664','5',1)
        elif '6665' in a:
            a = a.replace('6665','3',1)
    return a
a = '3' + '6'*120 + '3'
print(f(a))
#2
def f(a):
    while '4444' in a or '7777' in a:
        if '4444' in a:
            a = a.replace('4444','77',1)
        else :
            a = a.replace('7777','44',1)
    return a
a = '7' * 86
print(f(a))
#3
def f(a):
    while '222' in a or '888' in a :
        if '222' in a:
            a = a.replace('222','8',1)
        else :
            a = a.replace('888','2',1)
    return a
a = '8' * 193
print(f(a))
#4
def f(a):
    while '222' in a or '888' in a:
        if '222' in a:
            a = a.replace('222','8',1)
        else :
            a = a.replace('888','2',1)
    return a
a = 156 * '8'
print(f(a))
#5
def f(a):
    c = 0
    while '555' in a or '333' in a:
        if '333' in a:
            a = a.replace('333','5',1)
            c+=3
        else :
            a = a.replace('555','3',1)
    return c
a = "5" * 500
print(f(a))
