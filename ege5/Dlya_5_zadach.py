'''
    ЭТОТ РАЗДЕЛ БУДЕТ ПРЕДНАЗНАЧЕН КАКИМ-ТО ФУНКЦИЯМ, КОТОРЫЕ БУДУТ ЧАСТО ВСТРЕЧАТЬСЯ В 5 ЗАДАНИЯХ
    ВОЗМОЖНО ИЗ НИХ ОНИ БУДУТ ЛЁКИМИ, А ВОЗМОЖНО СЛОЖНЫМИ, НО ВСЁ ЖЕ, БУДУТ ПОЛЕЗНЫМИ
'''
#Чтобы перевести из 10-ой системе нужно  воспользоваться функцией перевода -> при этом не забвыай, что все функции перевода систем счислания переводят в тип STRING!
#value = bin(n)[2:] , где [2:] - это срез, он нужен,так как при переводе в 2-ую систему будет приставка, её нужно убрать
                     #где bin(n) - n -> любая переменная

#Чтобы посчитать сколько находится '1' или '2', то нужно воспользоваться функцией value.count()
#value = value.count(n), где n - это, то что вам нужно проверить количество;
                        #обязательно перед .count нужно указывать переменную, которую нужно проверить

#Допускается такое применение, где нужно перевести в 2-ую запись, затем к нему что-то прибавлять(обязательно str) и переводить сразу в двоичную запись!
#r = int(bin(n)[2:] + '01',2) -> переводит из 10 в 2, а потом переводит из 2 в 10 благодаря int, где первый аргумент принимает, что тебе нужно, а второй аргумент перевод

#Допускается такое применение, где нужно перевести в 2-ую запись, но она должна быть 8-мибитная
#r = '0' * (8 - len(r)) + r -> здесь мы домножаем на столько то '0' , сколько было в изначальном количестве 2-ой записи и прибавляем к нему обычную двоичную запись

#----------------------------------------------------------------------------------
'''
    ЭТОТ РАЗДЕЛ ПРЕДНАЗНАЧЕН ДЛЯ ПРИМЕРОВ И РЕШЕНИЙ
'''

# №1
'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1) Строится двоичная запись числа N.
2) Затем справа дописываются два разряда: символы 01, если число N чётное, и 10, если нечётное.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите минимальное число N, после обработки
которого автомат получает число, большее 138. В ответе это число запишите в десятичной системе.

'''
#Ответ: 35
##for n in range(1,1000):
##    s = bin(n)[2:]#строка
##    if int(s) % 2 == 0 :
##        s = s + '01'
##    else:
##        s = s + '10'
##    if int(s,2) > 138:
##        print(n)
##        break

# №2
'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец
числа (справа). Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы
цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Какое наименьшее число, большее 90, может быть
получено в результате работы автомата?

'''
##for n in range(1,1000):
##    s = bin(n)[2:]
##    s = s + str(s.count('1') % 2)
##    s = s + str(s.count('1') % 2)
##    if int(s,2) > 90:
##        print(n)
##        break

# №3
'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1) Строится двоичная запись числа N.
2) Затем справа дописываются два разряда: символы 01, если число N чётное, и 10, если нечётное.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите минимальное число N, после обработки
которого автомат получает число, большее 138. В ответе это число запишите в десятичной системе
'''
##for n in range(1,1000):
##    if n % 2 == 0 :
##        r = int(bin(n)[2:] + '01',2)
##    else:
##        r = int(bin(n)[2:] + '10',2)
##    if r > 138:
##        print(n)
##        break

# №4
'''
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим
образом:
1) Если исходное число кратно 2, оно делится на 2, иначе из него вычитается 1.
2) Если полученное на предыдущем шаге число кратно 3, оно делится на 3, иначе из него вычитается 1.
3) Если полученное на предыдущем шаге число кратно 7, оно делится на 7, иначе из него вычитается 1.
4) Число, полученное на шаге 3, считается результатом работы алгоритма.
Сколько существует различных натуральных чисел N, при обработке которых получится R = 2?
'''
##c = 0
##for n in range(2,1000):
##    if  n % 2 == 0:
##        g = n // 2
##    else:
##        g = n - 1
##    
##    if g % 3 == 0:
##        h = g // 3
##    else:
##        h = g - 1
##
##    if h % 7 == 0:
##        j = h //7
##    else:
##        j = h - 1
##    
##    if j == 2:
##        c+=1
##print(c)

# №5
'''
(Е. Джобс) Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) К этой записи справа дописывается 0, если число нечетное, и слева 1 в обратном случае.
3) Если единиц в двоичном числе получилось четное количество, справа дописывается 1, иначе 0.
Например, двоичная запись 1010 числа 10 будет преобразована в 110100.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью числа – результата работы данного алгоритма.
Укажите минимальное число N, для которого результат работы алгоритма будет больше 228. В ответе
это число запишите в десятичной системе счисления.
'''
##for n in range(1,10000):
##    x = bin(n)[2:] #Строка
##    if int(x) % 2 == 0 :
##        s = '1' + str(x)
##    else:
##        s = str(x) + '0'
##    r = int(s,2)
##    if r > 228 :
##        print(n)
##        break


# №6
'''
(ЕГЭ-2022) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое
число R следующим образом.
1)Строится двоичная запись числа N.
2)К этой записи дописываются ещё несколько разрядов по следующему правилу:
  а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 0, а затем два левых разряда заменяются на 10;
  б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 1, а затем два левых разряда заменяются на 11.
3)Результат переводится в десятичную систему и выводится на экран.
Например, для исходного числа 6 = 1102 результатом является число 10002 = 8, а для исходного числа 4 = 1002 результатом является число 11012 = 13.
Укажите максимальное число N, после обработки которого с помощью этого алгоритма получается число R, меньшее, чем 35

Идея:
1) Так как мы использем тип string, то нужно смело использовать СРЕЗЫ, НЕ НУЖНО REPLACE!!
'''
##for n in range(1,1000):
##    b = bin(n)[2::]
##    if b.count('1') % 2 == 0:
##        b = '10' + b[2:] + '0'
##    else:
##        b = '11' + b[2:] + '1'
##    r = int(b,2) 
##    if r <= 35 :
##        print(n)#24

# №7  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
'''
(А.М. Кабанов) Автомат обрабатывает натуральное число N<256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N.
2) Инвертируются все разряды исходного числа (0 заменяется на 1, 1 на 0).
3) К полученному двоичному числу прибавляют единицу.
4) Полученное число переводится в десятичную систему счисления.
Для какого числа N результат работы алгоритма равен 221?

Идея замены:
    В первом реплейсе должны заменить '0' на 'x', так как, если заменим на '1', то получится число с одинаковыми '1' в итоге не правильно заменятся цифры, поэтому,
    чтобы такого не допустить, нужно домнжаать на совершенно другой элемент! Ну, а потом его заменить на то, что спрашивается в условии!
'''
##for i in range(256):
##    r = bin(i)[2:]
##    r = '0' * (8 - len(r)) + r
##    # Тип мы будем домножать '0' * на то сколько получится выражении
##    r = r.replace('0','x')
##    r = r.replace('1','0')
##    r = r.replace('x','1')
##    if int(r,2) + 1 == 221:
##        print(i)

# №8 Примерно такое же
'''
Автомат обрабатывает натуральное число N < 256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N-1.
2) Инвертируются все разряды исходного числа (0 заменяется на 1, 1 на 0).
3) Полученное число переводится в десятичную систему счисления.
Для какого значения N результат работы алгоритма равен 143?
'''
##for n in range(256):
##    r = bin(n)[2:]
##    s = '0' * (8 - len(r)) + r
##    s = s.replace('0','x')
##    s = s.replace('1','0')
##    s = s.replace('x','1')
##    if int(s,2) == 143:
##        print(n)


# №9
'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
 а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа).
    Например, запись 11100 преобразуется в запись 111001;
 б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы цифр на 2.

Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Какое наименьшее число, большее 90, может быть

получено в результате работы автомата?

'''
##for n in range(1,1000):
##    s = bin(n)[2:]
##    s = s + str(s.count('1') % 2)
##    s = s + str(s.count('1') % 2)
##    if int(s,2) > 90:
##        print(n)
##        break

# №10
'''
(Е. Джобс) Автомат обрабатывает десятичное натуральное число N < 256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа.
2) Полученное в п.1 число записывается справа налево (переворачивается),
3) Из первого числа вычитается второе, результат записывается в десятичной системе счисления.
Найдите максимальное возможное число, которое может являться результатом работы алгоритма.

Идея:
1) value[::-1] , где value - ваша переменная, а [::-1] применяется к переменной и читает его с право на лево
'''
##w = []
##for i in range(256):
##    r = bin(i)[2:]
##    r = '0' * (8 - len(r)) + r
##    r1 = r[::-1]
##    #r2 = int(r,2) - int(r1,2)
##    w.append(int(r,2) - int(r1,2))
##print(max(w))

# №11
'''
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
1) Строится двоичная запись числа N.
2) Подсчитывается количество нулей и единиц в полученной записи. Если их количество одинаково, в конец записи добавляется её последняя цифра.
   В противном случае в конец записи добавляется цифра, которая встречается реже.
3) Шаг 2 повторяется ещё два раза.
4) Результат переводится в десятичную систему счисления.
При каком наименьшем исходном числе N > 90 в результате работы алгоритма получится чётное число, которое не делится на 4?

Идея:
1)Функцию нужно будет вызывать 3 раза, так как если прочитать условие внимательно, то получится, что первый раз мы вызовем функцию, но в 3 пунке сказано будет, что нужно еще 2 раза вызывать
'''
##def f(n):
##    s = bin(n)[2:]
##    c0 = s.count('0')
##    c1 = s.count('1')
##    if c0 == c1:
##        s += s[-1]
##    elif c0 > c1:
##        s+= '1'
##    else:
##        s+= '0'
##    return int(s,2)
##
##for n in range(91,200): #Уже учитываем условием, что N>90
##    r = f(f(f(n))) # вызывали еще два раза, поэтому в общем 3 раза
##    if r % 2 == 0 and r % 4 != 0:
##        print(n)
##        break


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# №12
'''
На вход алгоритма подаётся натуральное число N. Алогритм строит по нему новое число R следующим образом:
    1)Строится двоичная запись числа N.
    2)Далее эта запись обрабатывается по следующему правилу:
       а)Если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 0, а затем два левых разрадяа заменяются на 1;
       б)Если сумма цифр в доичной записи числа нечётная, то к этой записи справа дописывается 1, а затем два левых разрада заменяются на 11.
Полученна таким образом запись является двоичной записью числа R.
Например, для исходного числа 6 в 10 == 110 в 2 результатом является число 100 в 2 == 4 в 10, а для исходного числа 4 в 10 == 100 в 2 результатом является число
1101 в 2 == 13 в 10.
Укажите число N, после обработки которого с помощью этого алгоритма получается НАИМЕНЬШЕЕ значение R, большее 25. В ответе запишите это число в десятичной с.с.
'''
##def f(s):
##    s = bin(s)[2:]
##    if s.count('1') % 2 == 0:
##        s = '1' + s[2:] + '0'
##    else:
##        s = '11' + s[2:] + '1'
##    return int(s,2)
##
##a = []
##for i in range(50):
##    if f(i) > 25:
##        a += [[f(i),i]] # F(i) - обработанное число, i - его порядковый числитель, вот его и нужно указать в ответах
##a.sort()
##print(a) #Вызывается сам список
##print(a[0])#Там будет 26 и 29,верный 29 - вызывается список, в котоом мы конкретизируем, какой элемент-список нужен
##print(a[0][1]) #А здесь ещё конкретизируем, здесь мы просим уже элемент списка, который находится в другом списке

# №13
'''
Автомат обрабатывает натуральное число N по следующему алгоритму:
1. Строится двоичная запись числа N без ведущих нулей.
2. Если в полученной записи единиц больше, чем нулей, то справа приписывается единица. Если
нулей больше или нулей и единиц поровну, справа приписывается ноль.
3. Полученное число переводится в десятичную запись и выводится на экран.
Какое наименьшее число, превышающее 36, может получиться в результате работы автомата?

Идея:
1)Короче, если видишь, что написано 'без ведущих нулей',то это посути одно и то же, что и без этой надписи,
так как к примеру: 0000111 или 111 из двоич в 10, такой же будет ответ!
'''
##for i in range(1000):
##    s = bin(i)[2:]
##    if s.count('1') > s.count('0'):
##        s = s + '1'
##    elif s.count('1') < s.count('0') or s.count('1') == s.count('0'):
##        s = s + '0'
##    r = int(s,2)
##    if r > 36:
##        print(r,i)#ответ 39

# №14
'''
Автомат обрабатывает натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) Запись «переворачивается», то есть читается справа налево. Если при этом появляются
ведущие нули, они отбрасываются.
3) Полученное число переводится в десятичную систему счисления и выводится на экран.
Какое наименьшее число, превышающее 500, после обработки автоматом даёт результат 15?

Идея: Так как говорится про ведущие нули, то их посути и нет! одинаково будет считаться
'''
##for i in range(500,10000): #По условию превыщающее 500, но наимаеньшее число!
##    s = bin(i)[2:]
##    s = s[::-1]
##    if int(s,2) == 15:
##        print(i)
##        break

#15
'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим
образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа
(справа). Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является
двоичной записью искомого числа R. Какое наименьшее число, большее 108, может быть получено в
результате работы автомата?

'''
##res = []
##for n in range(1, 100000):
##    r = bin(n)[2:]
##    for _ in range(2): # два раза
##        r = r + str(r.count('1') % 2) #Остаток от деления на 2, которое переводится стринги
##    r = int(r, 2) #Переводим в 10-ую запись
##    if r > 108:
##        res.append(r)
##print(min(res))

#№16 ????
'''
Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее возможные двузначные
числа (числа не могут начинаться с нуля).
2. На экран выводится разность полученных двузначных чисел.
Пример. Дано число N = 351. Наибольшее двузначное число из заданных цифр – 53, наименьшее – 13. На экран
выводится разность 53 – 13 = 40.
Чему равно наименьшее возможное трёхзначное число N, в результате обработки которого на экране автомата
появится число 63?
'''
def f(x,y):
    w = []
    while x!=0:
        if y == 'макс':
            w.append(x%10)
            x//=10
    a = max(w)
    w.remove(a)
    b = max(w)
    w.remove(b)
    return a,b
        
print(f(256,'макс'))
##for n in range(100,1000):
    


'''
неизвестная задача
Но выглядит прикольно!
'''
##def f(N):
##    N = bin(N)[2:]
##    R = int(N)
##    s = 0
##    while R > 0:
##        s += R % 10
##        R //=10
##    N = str(N)
##    if s % 2 == 0:
##        N = N + '0'
##        N1 = '10' + x[2:]
##    else:
##        N = N + '1'
##        N1 = '11' + x[2:]
##    z = int(N1,2)
##    return int(N)
##for a in range(100):
##    if f(a) > 40:
##        print(a, f(a))
##        break



#----------------------------------------------------------------------------------


'''
    ЭТОТ ПРИМЕР ПРЕДНАЗНАЧЕН ДЛЯ ТЕХ ПРИМЕРОВ, КОТОРЫЕ ВЫЗВАЛИ У МЕНЯ ВОПРОС И ИХ НУЖНО РЕШИТЬ!(ЕСЛИ ПОЯВИТСЯ ВРЕМЯ:) )
'''


#----------
'''Нужно создать файл с особенными функциями'''
# Проверка на простые числа:

##def is_Prime(x):
##    i = 2
##    while i * i <= x:
##        if x % i == 0:
##            return False
##        i+=1
##    return True

#Пример:
#16
'''
(П. Волгин) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число,
задан следующими соотношениями:
F(n) = 1 при n = 0
F(n) = 7·(n - 1) + F(n - 1) при n > 0
Сколько существует значений n на отрезке [2, 200], для которых значение функции F(n) является
простым числом?
'''
##def is_Prime(x):
##    i = 2
##    while i * i <= x:
##        if x % i == 0:
##            return False
##        i+=1
##    return True
##def f(n):
##    if n == 0:
##        return 1
##    if n > 0:
##        return 7*(n - 1) + f(n - 1)
##for i in range(2,201):
##    
##for x in range(1,10):
##    i = 2
##    while i * i <= x:
##        if x % i == 0:
##            з
##        i+=1
##    print('1')
##    print(x)

'''
(Е. Джобс) Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) К полученному числу справа дописывается 0, если в числе единиц больше, чем нулей; иначе
дописывается 1.
3) Из середины двоичного числа убирается 2 разряда, если количество разрядов получилось четным, и 3
разряда, если нечетное.
4) Результат переводится в десятичную систему.
Пример. Дано число N = 11. Алгоритм работает следующим образом.
1) Двоичная запись числа N: 11 = 10112
2) Единиц больше, чем нулей, новая запись 101102
.
3) Длина начётная, удаляем три средних разряда, новая запись 102
.
4) Десятичное значение полученного числа 2.
Каково должно быть исходное число, чтобы в результате его обработки автомат получил значение 55?
'''
##def f(x):
##    w = []
##    while x!=0:
##        w.append(x % 10)
##        x//=10
##    return len(w)
##
##for n in range(1,10000):
##    s = bin(n)[2:]
##    if s.count('1') > s.count('0'):
##        s = s + '0'
##    else:
##        s = s + '1'
##    if len(f(s)) % 2 == 0:
##        s = s[:len(s)//2 - 1] + s[:len(s)//2 + 1]
##    else:

