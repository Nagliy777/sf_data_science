Создание списка
# my_list = list() 
# -->[]

# my_list = [ ] 
# -->[]

# a = range(1, 10)  
# ---->range(1, 10)

# a = range(10) 
# ---->range(0, 10)

Создаёт список, до последней цифры
# a = list(range(-5, 3))
# ---->[-5, -4, -3, -2, -1, 0, 1, 2]

# a = list(range(20, 10, -2))
# ---->[20, 18, 16, 14, 12]

# a = list(range(10, 20, 3))
# ---->[10, 13, 16, 19]

Нумерация индексов в Python начинается с нуля
#a = ["a", "b", "c"]
#print(a[0]) ---->a
#print(a[-1])  ---->c

Операция взятия среза
#a = ["a", "b", "c", "d", "e", "d"]
#print(a[:2])   ----> ['a', 'b']
#print(a[2:4])  ----> ['c', 'd']
#print(a[0:5:2]) ----> ['a', 'c', 'e'] 

Создание списка,потом срез
#a=list(range(-5, 5)[4:9])
#print(a)  ---->[-1, 0, 1, 2, 3]

#a=list(range(-3, 6)[::-1])
#print(a)  ---->[[5, 4, 3, 2, 1, 0, -1, -2, -3]

#a=list(range(-3, 6)[::-2])
#print(a)  ----> [5, 3, 1, -1, -3]

#a='Hello kitty !'
#print(a.split()[0:2]) ---->['Hello', 'kitty']

#Методы списков

Метод  .append() добавляет новый элемент к списку.
#orders_daily = [] 
#orders_daily.append(123) 
#orders_daily.append(45) 
#print(orders_daily)  ----> [123, 45]

Метод .clear() очистка списка
#a=[123, 45]
#a.clear()
#print(a) ----> []

Метод .count() считает количество определённого элемента
#a = ["a", "b", "c", "d", "b", "b", "g", "b", "d"]
#print(a.count("b"))  ----> 4

Метод .copy(), [:] копирует значение в другую переменную
#a = [1,2,3]
#b = a.copy()
#print(b) ----> [1, 2, 3]
#a = [1,2,3]
#b = a[:]
#print(b) ----> [1, 2, 3]

Метод .extend() добавляет к первому списку второй список
#a = ["a", "b", "c"]
#b = ["d", "e"]
#a.extend(b) 
#print(a) ----> ['a', 'b', 'c', 'd', 'e']

Метод .reverse(), [::-1] разворачивает список
# a = [1, 2, 3]
# a.reverse()
# print(a)  ----> [3, 2, 1]
# a = [1, 2, 3]
# b=a[::-1]
# print(b) ----> [3, 2, 1]

Метод .sort() сортирует список
#a=[1,7,5,3,9,8,2,4,6]
#a.sort()
#print(a) ----> [1, 2, 3, 4, 5, 6, 7, 8, 9]

Списки могут хранить списки, кортежи, строки, числа
# list2 = [[3,2,4], (3,4), "5.6", 7]
# строки это списки  “hello” и [“h”, “e”, “l”, “l”, “o”] будут эквивалентными.

Кортеж — неизменяемая структура данных. Его можно создать один раз 
и затем использовать без модификации элементов внутри. 
Это некая защита: не всегда хочется, чтобы пользователь/программист мог менять элементы. Список же такого ограничения не предоставляет.
Кортежи занимают меньший объём памяти. Чтобы увидеть это, можно воспользоваться хитрым методом у структур данных — .__sizeof__().

# a = (1,2,3,4,5,6) 
# b = [1,2,3,4,5,6] 
# print(a.__sizeof__()) ----> 72
# print(b.__sizeof__()) ----> 88

Создание кортежа
# tpl1 = tuple()
# print(tpl1) ----> ()
# tpl2 = ()
# print(tpl2) ----> ()
#tpl4 = ("s", )  запятая после значения обязательна, чтобы получить кортеж.
#print(tpl4)  ----> ('s',)