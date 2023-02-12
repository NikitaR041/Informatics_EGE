'''
    ЭТОТ РАЗДЕЛ БУДЕТ ПРЕДНАЗНАЧЕН КАКИМ-ТО ФУНКЦИЯМ, КОТОРЫЕ БУДУТ ЧАСТО ВСТРЕЧАТЬСЯ В 5 ЗАДАНИЯХ
    ВОЗМОЖНО ИЗ НИХ ОНИ БУДУТ ЛЁКИМИ, А ВОЗМОЖНО СЛОЖНЫМИ, НО ВСЁ ЖЕ, БУДУТ ПОЛЕЗНЫМИ

#Чтобы перевести из 10-ой системе нужно  воспользоваться функцией перевода -> при этом не забвыай, что все функции перевода систем счислания переводят в тип STRING!
value = bin(n)[2:] , где [2:] - это срез, он нужен,так как при переводе в 2-ую систему будет приставка, её нужно убрать
                     где bin(n) - n -> любая переменная

#Чтобы посчитать сколько находится '1' или '2', то нужно воспользоваться функцией value.count()
value = value.count(n), где n - это, то что вам нужно проверить количество;
                        обязательно перед .count нужно указывать переменную, которую нужно проверить

#Допускается такое применение, где нужно перевести в 2-ую запись, затем к нему что-то прибавлять(обязательно str) и переводить сразу в двоичную запись!
r = int(bin(n)[2:] + '01',2) -> переводит из 10 в 2, а потом переводит из 2 в 10 благодаря int, где первый аргумент принимает, что тебе нужно, а второй аргумент перевод

#Допускается такое применение, где нужно перевести в 2-ую запись, но она должна быть 8-мибитная
r = '0' * (8 - len(r)) + r -> здесь мы домножаем на столько то '0' , сколько было в изначальном количестве 2-ой записи и прибавляем к нему обычную двоичную запись
'''
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
    В первом реплейсе должны заменить '0' на 'x', так как, если заменим на '1', то получится число с одинаковыми '1' в итоге не правильно заменятся числа, поэтому,
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

# №10 не нашел в задачнике
'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1. Строится двоичная запись числа N без ведущих нулей.
2. Если в полученной записи единиц больше, чем нулей, то справа приписывается единица. Если
нулей больше или нулей и единиц поровну, справа приписывается ноль.
Полученная таким образом запись является двоичной записью искомого числа R. Какое наибольшее
число, меньшее 43, может быть получено в результате работы автомата?
'''
##for n in range(1000):
##    s = bin(n)[2:] # без значащих нулей
##    if s.count('1') > s.count('0'):
##        s = s + '1'
##    elif s.count('1') == s.count('0') or s.count('0') > s.count('1'):
##        s = s + '0'
##    if int(s,2) < 43:
##        print(n)
        
# №11
'''
Автомат обрабатывает натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) Запись «переворачивается», то есть читается справа налево. Если при этом появляются ведущие нули, они отбрасываются.
3) Полученное число переводится в десятичную систему счисления и выводится на экран.
Какое наименьшее число, превышающее 500, после обработки автоматом даёт результат 15?
'''
##for n in range(501,1000):
##    s = bin(n)[2:]
##    s = s[::-1]
##    if int(s,2) == 15:
##        print(n)
##        break

# №12
'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1) Строится двоичная запись числа N.
2) Затем справа дописываются два разряда: символы 01, если число N чётное, и 10, если нечётное.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите минимальное число N, после обработки
которого автомат получает число, большее 97.
В ответе это число запишите в десятичной системе
'''
##for i in range(1000):
##    s = bin(i)[2:]
##    if s.count('1') % 2 == 0 :
##        s = s + '01'
##    else:
##        s = s + '10'
##    if int(s,2) > 97:
##        print(i)
##        break


#----------------------------------------------------------------------------------

'''
    ЭТОТ ПРИМЕР ПРЕДНАЗНАЧЕН ДЛЯ ТЕХ ПРИМЕРОВ, КОТОРЫЕ ВЫЗВАЛИ У МЕНЯ ВОПРОС И ИХ НУЖНО РЕШИТЬ!(ЕСЛИ ПОЯВИТСЯ ВРЕМЯ:) )
'''

'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1) Строится двоичная запись числа N.

2) К этой записи дописывается (дублируется) последняя цифра. -> значит последняя

3) Затем справа дописывается 0, если в двоичном коде числа N чётное число единиц, и 1, если нечётное.

4) К полученному результату дописывается ещё один бит чётности так, чтобы количество единиц в двоичной записи полученного числа стало чётным.

Полученная таким образом запись (в ней на три разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите минимальное число R, большее 80, которое
могло получиться в результате работы автомата. В ответе это число запишите в десятичной системе.
'''
##for n in range(1000):
##    s = bin(n)[2:]
##    s = s + s[-1]
##    if s.count('1') % 2 == 0:
##        s = s + '0'
##    else:
##        s = s + '1'
##    if s.count('1') % 2 == 0:
##        pass
##    else:
##        s = s + '1'
##    if int(s,2) > 80:
##        print(n)
##        break