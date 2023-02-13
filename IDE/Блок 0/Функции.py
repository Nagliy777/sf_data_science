Функция — это фрагмент программного кода, к которому можно обратиться из любого места программы.
Итак, функции позволяют:
1.Выполнять один и тот же набор инструкций (фрагмент исходного кода) несколько раз;
2.Выполнять одни и те же действия с различными входными данными;
3.Структурировать исходный код.

Функция, принимающая на вход один аргумент: 

def print_hours(minutes):
    # // — это оператор целочисленного деления
    hours = minutes // 60
    # % — это оператор получения остатка от деления
    left_minutes = minutes % 60
    print("Hours:", hours)
    print("Minutes left:", left_minutes)
    
print_hours(90) ---> Hours: 1  Minutes left: 30

Оператор, который позволяет функции передать какой-либо объект (число, строку, список, даже другую функцию) 
в то место кода, откуда вызывалась функция, называется return (от англ. "return" — «возвращать»). 
При этом говорят, что функция возвращает какой-либо результат.

# Назовём функцию get_time (get — получать,
# time — время). Она принимает аргументы
# distance — расстояние и speed — скорость.
def get_time(distance, speed):
    # В переменную result сохраним результат
    # деления расстояния на скорость.
    result = distance / speed

    # Чтобы вернуть результат вычислений,
    # пишем оператор return и название переменной,
    # значение которой будет передано.
    return result 

return и несколько переменных:

def get_time_tuple(distance, speed):
    # Получаем целое число часов в пути
    hours = distance // speed
    # Получаем остаток км в пути
    distance_left = distance % speed
    # Переводим скорость из км/ч в км/мин:
    # за одну минуту можно проехать расстояние
    # в 60 раз меньше, чем за 1 час
    kms_per_minute = speed / 60
    # Делим оставшееся расстояние на скорость в км/мин.
    # и округляем до целого
    minutes = round(distance_left / kms_per_minute)
    
    # Перечисляем аргументы через запятую.
    # Они будут возвращены функцией в виде кортежа.
    return hours, minutes

Теперь вызовем функцию get_time_tuple, сохраним результат в переменную result и напечатаем её:

result = get_time_tuple(120, 100)

print("Hours to travel:", result[0]) ---> Hours to travel:1
print("Minutes to travel:", result[1]) ---> Minutes to travel:12

Также мы можем получить результат выполнения функции сразу в две переменные без необходимости обращаться к элементам tuple.
# Через запятую перечисляем переменные, в которые сохранится результат
hours, minutes = get_time_tuple(120, 100)
# Красиво напечатаем результат
print("Hours to travel:", hours) ---> Hours to travel: 1
print("Minutes to travel:", minutes) --->Minutes to travel: 12


Пример с исключением:
grades = {'Ivanov': 5, 'Smirnov': 3, 'Kuznetsova': 4, 'Tihonova': 5}
# Только попробуем (try — пробовать) напечатать оценку студента,
# которого нет в словаре
try:
    print(grades['Pavlov'])
# А если возникнет ошибка в ключе (KeyError), скажем,
# что студента нет в словаре
except KeyError:
    print("Student’s mark was not found!")
# Будет напечатано:
# Student’s mark was not found!

Пример с raise:
После встречи с raise интерпретатор прекращает исполнение кода функции.Вызываем ошибку.

def get_time(distance, speed):
    # Если расстояние или скорость отрицательные, то возвращаем ошибку
    if distance < 0 or speed < 0:
        # Оператор raise возвращает (raise — досл. англ. "поднимать")
        # объект-исключение. В данном случае ValueError (некорректное значение).
        # Дополнительно в скобках после слова ValueError пишем текст сообщения
        # об ошибке, чтобы сразу было понятно, чем вызвана ошибка.
        raise ValueError("Distance or speed cannot be below 0!")
    result = distance / speed
    return result

Пример с raise:
def add_mark(name, mark, journal=None):
    # Добавьте здесь проверку аргумента mark
    if journal is None:
        journal = {}

    if mark not in [2,3,4,5]:
        raise ValueError('Invalid Mark!')
            
    journal[name] = mark
    return journal

print(add_mark('Ivanov', 4))

Пример:
# В функцию должны передаваться 2 значения:
# число и степень корня
def root(value, n):
    # Как мы уже выяснили, чтобы посчитать
    # корень степени n из числа, можно возвести это число
    # в степень 1/n
    result = value ** (1/n)
    return result

# Посчитаем корень 3-ей степени (кубический корень) из 27
print(root(27, 3))  ---> 3.0


Пример с аргументом по умолчанию:
# В функцию должны передаваться 2 значения:
# число и степень корня
def root(value, n=2):
    # Как мы уже выяснили, чтобы посчитать
    # корень степени n из числа, можно возвести это число
    # в степень 1/n
    result = value ** (1/n)
    return result

# Посчитаем корень 3-ей степени (кубический корень) из 27
print(root(81))  ---> 9.0

Указывать аргументам значения по умолчанию можно только после того, как в функции перечислены все обязательные аргументы.

Ввиду особенностей работы со «сложными» типами данных, они являются изменяемыми, 
поэтому использование их в качестве аргументов по умолчанию нежелательно (Списки,словари, множества).

В качестве аргументов по умолчанию точно можно использовать «простые» типы данных, 
которые не содержат в себе дополнительные значения, такие как int, float, str, bool, None.


Чтобы избежать ошибок, связанных с изменяемыми типами данных, используйте None в качестве значения аргумента по умолчанию 
и создавайте новый объект уже в теле функции, как это было сделано в примере ниже:

def add_mark(name, mark, journal=None):
    # Если журнал является None
    # (напоминание: сравнивать объект с None
    # корректнее через оператор is),
    # запишем в journal пустой словарь
    if journal is None:
        journal = {}
    journal[name] = mark
    return journal



Пример с разговорчивой функцией:

def root(value, n=2, verbose=False):
    result = value ** (1/n)
    if verbose:
        # Аргументы в функции print,
        # перечисленные через запятую,
        # печатаются через пробел
        print('Root of power', n, 'from',
            value, 'equals', result)
    return result

Важно сначала передавать порядковые и только затем именованные аргументы.

print(root(81, verbose=True, n=4))

Есть небольшое исключение: можно записать порядковый аргумент после именованных, 
но для этого необходимо подать его в виде именованного — с помощью знака «равно». Вот так:

print(root(verbose=True, n=4, value=81))


*args. Здесь * — это не символ умножения, а оператор распаковки.
После аргументов, записанных через *args, не могут идти другие порядковые аргументы.
Необходимо запомнить, что все аргументы, следующие за конструкцией с оператором *, считаются именованными.

Оператор распаковки * можно использовать и для передачи значений из списка в функцию.
Оператор * удобно использовать для печати списков в более читабельном виде.

langs = ['Python', 'SQL', 'Machine Learning', 'Statistics']

print(*langs) ---> Python SQL Machine Learning Statistics


Сейчас мы напишем функцию, которая принимает неизвестное заранее число аргументов для обработки,
чтобы вы тоже научились создавать подобные функции.

# В массив args будут записаны все переданные
# порядковые аргументы
def mean(*args):
    # Среднее значение — это сумма всех значений,
    # делённая на число этих значений
    # Функция sum — встроенная, она возвращает
    # сумму чисел
    result = sum(args) / len(args)
    return result
 
# Передадим аргументы в функцию через запятую,
# чтобы посчитать их среднее
print(mean(5,4,4,3)) ---> 4.0

Это кортеж (tuple):

def mean(*numbers):
    # С помощью встроенной функции isinstance
    # проверим, что numbers — это tuple
    print(isinstance(numbers, tuple))  ---> True
    # Напечатаем содержимое объекта numbers
    print(numbers)                            ---> (5, 4, 4, 3)
    result = sum(numbers) / len(numbers) 
    return result
 
print(mean(5,4,4,3))  ---> 4.0

Ещё пример:
# В качестве первого аргумента принимаем фамилию
# студента, а затем уже его оценки через запятую
def mean_mark(name, *marks):
    result = sum(marks) / len(marks)
    # Не возвращаем результат, а печатаем его
    print(name+':', result)
 
mean_mark("Ivanov", 5, 5, 5, 4) ---> Ivanov: 4.75

Пример:
def mult(*numbers):
    result = 1
    for i in numbers:
        result *= i
    return result

print(mult(3,5,10)) ---> 150

Пример:
marks = [4,5,5,5,5,3,4,4,5,4,5]

def mean_mark(name, *marks):
    result = sum(marks) / len(marks)
    # Не возвращаем результат, а печатаем его
    print(name+':', result)   

mean_mark('Kuznetsov',*marks) ---> Kuznetsov: 4.454545454545454

С помощью оператора ** можно передавать в функцию нескольких аргументов. 
Он используется для передачи именованных аргументов с помощью словаря, который в дальнейшем будет распакован. 
Кроме того, оператор ** является оператором распаковки, только для словарей. Ключами словаря выступают названия аргументов, 
а значениями — те значения аргументов, которые должны быть им присвоены.

# В переменную kwargs будут записаны все
# именованные аргументы
def schedule(**kwargs):
    # kwargs — это словарь, проверим это с помощью isinstance:
    print(isinstance(kwargs, dict)) ---> True
    # Напечатаем объект kwargs
    print(kwargs)
 
schedule(monday='Python', tuesday='SQL', friday='ML') ---> {'monday': 'Python', 'tuesday': 'SQL', 'friday': 'ML'}


Пример:

def schedule(**kwargs):
    print("Week schedule:")
    for key in kwargs:
        print(key, kwargs[key], sep=' - ')

schedule(monday='Python', tuesday='SQL', friday='ML')
# Будет напечатано:
# Week schedule:
# monday — Python
# tuesday — SQL
# friday — ML


Принцип совместного использования *args и **kwargs логично вытекает из принципа перечисления аргументов: 
сначала — порядковые, затем — именованные. 

def print_args(*args, **kwargs):
    print(args)   ---> (1, 4, 5, 7)
    print(kwargs) ---> {'name': 'Ivanov', 'age': 19, 'city': 'Moscow'}
 
print_args(1,4,5,7, name='Ivanov', age=19, city='Moscow')


Пример:
list1 = [1,4,6,8]
list2 = [12, 45, 56, 190, 111]
list3 = ['Python', 'Functions']
 
# Один раз запишем в словарь параметры для печати
# через print: разделитель — запятая,
# окончание строки — точка с запятой
how = {'sep': ', ', 'end': '; '}
 
# Распаковываем и список, и словарь how
print(*list1, **how)
print(*list2, **how)
print(*list3, **how)  ---> 1, 4, 6, 8; 12, 45, 56, 190, 111; Python, Functions;


lambda-функции. Он позволяет быстро создавать короткие однострочные функции, 
для которых нет необходимости прописывать целиком сигнатуру и оператор return.

is_even = lambda num: "even" if num % 2 == 0 \
else "odd"


print(is_even(2)) ---> even

Пример:
# Для получения корня произвольной степени от числа
# (например, корня степени 4) необходимо возвести исходное
# число в степень, равную единице, делённой на желаемую
# степень корня.
nth_root = lambda num, n: num**(1/n)
print(nth_root(16,4)) ---> 2.0

Пример:
full_func = lambda *args, **kwargs: (args, kwargs)

print(full_func(1,5,6,7,name='Ivan', age=25)) ---> ((1, 5, 6, 7), {'name': 'Ivan', 'age': 25})

На самом деле использовать lambda-функцию удобно, если требуется передать простую функцию в качестве аргумента другой функции.

names = ['Ivan', 'Kim', 'German', 'Margarita', 'Simon']
names.sort(key=lambda name: len(name))
print(names) ---> ['Kim', 'Ivan', 'Simon', 'German', 'Margarita']

Пример:
def get_length(line):
    return len(line)

new_list = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']
new_list.sort(key=get_length)
print(new_list) ---> ['cc', 'bbb', 'aaa', 'ababa', 'aaaaa']

Пример сортировки и по длине, и по алфавиту:

new_list = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']

new_list.sort(key=lambda word: (len(word), word))
print(new_list) ---> ['cc', 'aaa', 'bbb', 'aaaaa', 'ababa']


Пример:
#Напишите функцию sort_sides, которая сортирует переданный в неё список.
#Входной список состоит из кортежей с парами чисел — длинами катетов прямоугольных треугольников.
#Функция должна возвращать список, отсортированный по возрастанию длин гипотенуз треугольников.



def sort_sides(l_in):
    l_in.sort(key=lambda x: (x[0]**2 + x[1]**2) ** (1/2))
    return l_in
    

print(sort_sides([(3,4), (1,2), (10,10)])) ---> [(1, 2), (3, 4), (10, 10)]


Пример:

#Напишите функцию get_less, которая принимает на вход через запятую список, состоящий из чисел, и ещё одно число. 
#Функция должна вернуть первое найденное число из списка, которое меньше переданного во втором аргументе. 
#Если такого числа нет, необходимо вернуть None.

l = [11, 15, 9,  7]

def get_less(numbers, number):
    for i in numbers:
        if i < number:
            return i
        else:
            None

print(get_less(l, 11)) ---> 9

Пример:
#Напишите функцию is_prime(num), которая проверяет, является ли число простым.
#Функция должна вернуть True, если число простое, иначе — False.


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):     
        if num % i == 0:    
            return False
    return True

print(is_prime(13))


Пример:
#Напишите функцию between_min_max(...), которая принимает на вход числа через запятую.
#Функция возвращает среднее арифметическое между максимальным и минимальным значением этих чисел, то есть (max + min)/2.


def between_min_max(*numbers):
    i=list(numbers)
    i.sort()
    a = i[::-1]
    result = (i[0]+a[0])/2
    return result


Пример:
#Напишите функцию best_student(...), которая принимает на вход в виде именованных аргументов имена студентов и их номера в рейтинге 
#(нагляднее в примере).Необходимо вернуть имя студента с минимальным номером по рейтингу.


def best_student(**name):
    a = name.keys()
    b = list(a)
    c = name.values()
    d = list(c) 
    d.sort()
    for i in b:
        if name[i] == d[0]:
            return i


        
print(best_student(Tom=12, Mike=3, Bilbo=5, Lev=2, Kolya=1, lecha=9 )) ---> Kolya


Пример:
#Напишите lambda-функцию is_palindrom, которая принимает на вход одну строку и проверяет, является ли она палиндромом, 
#то есть читается ли она слева-направо и справа-налево одинаково.
#Функция возвращает 'yes', если строка является палиндромом, иначе — 'no'.


is_palindrom = lambda x: 'yes' if x == x[::-1] \
else 'no'

print(is_palindrom('1212'))


Пример:
#Функция принимает на вход числа через запятую 
#и возвращает одно число — среднее между максимумом и минимумом этих чисел.

between_min_max = lambda *num: (min(num)+max(num))/2

print(between_min_max(1,2,3,4,5)) ---> 3.0

Пример:
#Напишите функцию exchange(usd, rub, rate), которая может принимать на вход сумму в долларах (usd), 
#сумму в рублях (rub) и обменный курс (rate). Обменный курс показывает, сколько стоит один доллар. 
#Например, курс 85.46 означает, что один доллар стоит 85 рублей и 46 копеек.

#В функцию должно одновременно передавать два аргумента. Если передано менее двух аргументов, 
#должна возникнуть ошибка ValueError('Not enough arguments'). Если же передано три аргумента, должна возникнуть ошибка: 
#ValueError('Too many arguments').

#Функция должна находить третий аргумент по двум переданным. Например, если переданы суммы в разных валютах,
#должен возвращаться обменный курс. Если известны сумма в рублях и курс, должна быть получена эквивалентная сумма в долларах, 
#аналогично — если передана сумма в долларах и обменный курс.

def exchange(usd=None, rub=None, rate=None):
    if usd is None and rub is None:
        raise ValueError('Not enough arguments')
    if usd is None and rate is None:
        raise ValueError('Not enough arguments')        
    if rub is None and rate is None:
        raise ValueError('Not enough arguments')
    if rub is not None and usd is not None and rate is not None:
        raise ValueError('Too many arguments')          


    if usd is None:
        usd = rub/rate
        return usd
    if rub is None:
        rub = usd*rate
        return rub
    if rate is None:
        rate = rub/usd
        return rate 

print(exchange(usd=100, rub=555))