В Python существует четыре типа переменных в зависимости от их видимости. Их разрешение будет идти от пункта 1 до пункта 4. 
Для любого разработчика очень важно понимать различия между ними, чтобы не сделать множество ошибок в попытках использовать переменные, 
которые использовать нельзя.

1.Локальные переменные (local) — это переменные, которые были объявлены в функции и используются непосредственно в ней.
В разряд локальных переменных также входят аргументы функции.
1.1.Аргументы функции register_employee(), name и surname, являются локальными переменными по отношению к этой функции.
1.2.Функция create_full_name() является локальной для функции register_employee(). Попытка вызвать её из основной части программы приведёт к ошибке, 
которую мы уже видели раньше.
1.3.Переменные sep и result являются локальными по отношению к функции create_full_name(). 
Они является невидимыми для функции register_employee() и для основной части программы.
1.4.Переменная full_name, в которую заносится результат работы функции create_full_name(), 
является локальной переменной функции register_employee().

Пример:
#объявляем внешнюю функцию для регистрации сотрудников
def register_employee(name, surname):
    #объявляем функцию для промежуточных вычислений
    def create_full_name():
        #функция использует внешние переменные name и surname
        sep = ' ' #разделитель между именем и фамилией
        result = name + sep + surname #вычисляем полное имя
        return result
    full_name = create_full_name() #вызываем внутреннюю функцию
    #выводим результат на экран, используя внешнюю переменную company_name
    print('Employee {} is registered with the company {}'.format(full_name, company_name))
    
company_name = 'TheBlindMice' #название компании
register_employee('John','Doe') вызов функции  ---> Employee John Doe is registered with the company TheBlindMice

2.Нелокальные переменные (nonlocal) — это переменные, которые были объявлены во внешней функции относительно рассматриваемой функции.

2.1.Переменные name и surname являются нелокальными по отношению к функции create_full_name(). 
Они объявлены во внешней функции и используются во внутренней.


3.Глобальные переменные (global) — это переменные, которые были объявлены непосредственно в основном блоке программы (вне функций).

3.1.Переменная company_name объявлена в основной части программы (вне функции) и является глобальной.
Обратите внимание, что она задана после объявления функции. Ошибки не возникает, потому что код выполняется построчно, 
а значит сначала создаётся переменная company_name, а затем она уже используется в вызове функции  register_employee(). 
Если бы мы поменяли вызов функции и объявление переменной местами, получили бы ошибку.


4.Встроенные переменные (built-in) — это переменные и объекты, которые встроены в функционал Python изначально. 
Например, к ним относятся функции print, len, структуры данных list, dict, tuple и другие. 
В большинстве IDE, таких как PyCharm, VS Code и Jupyter, имена таких переменных подсвечиваются специальным цветом.
4.1.Функция print() является встроенной функцией Python. К ней можно обращаться из любой части программы.


def print_root(value, n=2):
    # Зададим внутреннюю функцию
    # Она будет являться вспомогательной
    def root(value, n=2):
        result = value ** (1/n)
        return result
    # Получим результат из внутренней функции
    res = root(value, n)
    # Печатаем результат и не возвращаем его
    print('Root of power', n, 'from', value, 'equals', res)

print_root(5) ---> Root of power 2 from 5 equals 2.23606797749979


Когда интерпретатор встречает в коде функции ссылку (переменную) на какой-то объект, он начинает искать его среди локальных переменных, 
затем переключается на нелокальные, потом на глобальные и, наконец, ищет переменную среди встроенных объектов. 
Если поиск оказался безрезультатным, возникает ошибка.

Таким образом, действует правило: на свой этаж можно пригласить только жителя со своего или нижних этажей, 
попытка позвать в гости соседа сверху приведёт к ошибке.

Важное замечание: стандарты разработки на Python не рекомендуют изменять в функциях глобальные переменные, 
однако такая возможность предусмотрена. Для этого необходимо добавить оператор global внутри функции перед той переменной, 
которую вы хотите изменить глобально.

В данном случае, чтобы изменить переменную на глобальном уровне, нам необходимо добавить строку global global_counter:

global_counter = 0
 
def add_one():
    # Обозначим, что переменная global_counter
    # является глобальной
    global global_counter
    global_counter += 1
 
add_one()
print(global_counter) --->1

В данном случае, чтобы изменить переменную на нелокальном уровне, нам необходимо добавить строку nonlocal enclosing_counter:

def outer_function():
    enclosing_counter = 0
    def inner_function():
        # С помощью оператора nonlocal покажем,
        # что переменная enclosing_counter находится
        # во внешней функции
        nonlocal enclosing_counter
        enclosing_counter += 1
        print(enclosing_counter)
    inner_function()
 
outer_function() ---> 1

У операции, которую мы только что совершили, есть своё название. 
В данном случае функция inner_function является функцией-замыканием — она использует в своём коде ссылки на переменные, 
которые были объявлены во внешней функции, но не в основном коде программы.

Пример:
# Функция, которая создаёт счётчик
def counter():
    # Начальное значение счётчика — 0
    number = 0
    # Функция add будет каждый раз прибавлять
    # к счётчику 1 при запуске
    def add():
        # Сообщаем, что number берём из
        # внешней функции
        nonlocal number
        # Увеличиваем значение счётчика на 1   
        number += 1
        # Возвращаем текущее число запусков счётчика
        return number
    # Возвращаем не результат вычислений,
    # а непосредственно саму функцию add
    # без круглых скобок!
    return add

# Создадим два различных счётчика
counter1 = counter()
counter2 = counter()

# Будем запускать вразнобой разные счётчики
print("Counter 1:", counter1()) ---> Counter 1: 1
print("Counter 1:", counter1()) ---> Counter 1: 2
print("Counter 2:", counter2()) ---> Counter 2: 1
print("Counter 1:", counter1()) ---> Counter 1: 3
print("Counter 2:", counter2()) ---> Counter 2: 2
print("Counter 2:", counter2()) ---> Counter 2: 3

Каждый счётчик считает только свои запуски.