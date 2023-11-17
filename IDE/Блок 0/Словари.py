Пустой словарь можно создать несколькими способами:
# my_dict = dict() 
# print(my_dict)  --->{}
# my_dict = {}   --->{}
# print(my_dict)

Выводит значение ключа:
# phones = {'+79033923029': 'Ivan Ivanov', '+78125849204': 'Kirill Smirnov'}
# print(phones['+79033923029']) ----> Ivan Ivanov

Замена значения:
# phones = {'+79033923029': 'Ivan Ivanov', '+78125849204': 'Kirill Smirnov'}

Меняет значение
# phones['+79033923029'] = 'Vano'  
# print(phones['+79033923029'])  ----> Vano  

Добавляет новый ключ и значение в словарь
# phones["+79686581788"]  = 'Artem Pliev' 
# print(phones)  ---->{'+79033923029': 'Ivan Ivanov', '+78125849204': 'Kirill Smirnov', '+79686581788': 'Artem Pliev'}

Выводит значения
# print(phones.values()) ----> dict_values(['Vano', 'Kirill Smirnov', 'Artem Pliev']) 
Выводит ключи
# print(phones.keys()) dict_keys(['+79033923029', '+78125849204', '+79686581788']) 

Важно! Поиск всегда идёт по ключу. Нельзя использовать значение в качестве ключа.
Важно! Ключи в словаре должны быть уникальными. Если вы вставляете в словарь два одинаковых ключа 
с разными значениями, то тогда в качестве значения примется последнее значение, которое вы записали для ключа.

 d = {"a": 1, "b":3, "a": 5}
 print(d["a"]) ----> 5

Методы:

Метод .keys() Чтобы вывести ключи  словаря
Метод .values() Чтобы вывести значения словаря 
Метод .sort() Сортирует

#friends = {"Kolya": 180, "Marina": 176, "Misha": 158, "Dima": 201, "Yana": 183, "Nina": 156}
#friends_keys = list(friends.keys()) Преобразование в список
#friends_keys.sort() Сортировка
#print(friends_keys) -----> ['Dima', 'Kolya', 'Marina', 'Misha', 'Nina', 'Yana']

Метод .clear(), friends = {} Очистка
#friends = {"Kolya": 180, "Marina": 176, "Misha": 158, "Dima": 201, "Yana": 183, "Nina": 156}
#friends.clear()
#print(friends) ----->{}

Метод .get()
«Умная» замена обычному обращению по ключу через квадратные скобки. Если использовать только квадратные скобки при обращении 
к словарю, то при отсутствии нужного ключа программа выдаст ошибку и закончит работу.
В случае с .get() программа продолжит работать, но вернёт константу None — единственного представителя типа NoneType, 
который показывает, что значения нет, оно пусто.

#friends = {"Kolya": 180, "Marina": 176, "Misha": 158, "Dima": 201, "Yana": 183, "Nina": 156}
#print(friends["Matvey"]) -----> KeyError: 'Matvey'
#print(friends.get("Matvey")) #--------> None

Также .get() позволяет вывести значение по умолчанию для отсутствующего ключа. Это второй аргумент в методе .get():
#print(friends.get("Matvey", 'Netu')) -----> Netu

Метод .update() добавляет сразу несколько ключей и значений в словарь, а таже меняет существующее зачение.

#friends = {"Kolya": 180, "Marina": 176, "Misha": 158, "Dima": 201, "Yana": 183, "Nina": 156}
#friends.update({'Tamara': 177, 'Bilbo':777, "Misha": 159})
#print(friends) -----> {'Kolya': 180, 'Marina': 176, 'Misha': 159, 'Dima': 201, 'Yana': 183, 'Nina': 156, 'Tamara': 177, 'Bilbo': 777}

Метод .pop() удаляет из структуры данных элементы, но дополнительно метод возвращает результат в новую переменную.
#friends = {"Kolya": 180, "Marina": 176, "Misha": 158, "Dima": 201, "Yana": 183, "Nina": 156}
#best_friends = friends.pop("Misha")
#print(friends)  -----> {'Kolya': 180, 'Marina': 176, 'Dima': 201, 'Yana': 183, 'Nina': 156}
#print(best_friends) -----> 158

Метод .setdefault() принимает два параметра: ключ и значение по умолчанию, если этого ключа нет в словаре.
Если ключ имеется, его значение останется неизменным

#friends = {"Kolya": 180, "Marina": 176,"Nastya": 163}
#friends.setdefault("Nastya",100)
#print(friends["Nastya"])  -----> 163
#friends.setdefault("Bilbo",777)
#print(friends["Bilbo"]) -----> 777
#print(friends) -----> {'Kolya': 180, 'Marina': 176, 'Nastya': 163, 'Bilbo': 777}

Важно! В качестве ключа словаря должен выступать неизменяемый тип данных 
(числа, строки, кортежи), а в качестве значения может выступать любая структура данных.
d = {(1,2): "hello", "my name is": "Curt", 5: (7,7,7), "info": {"name": "stive", "age": 15, "cities": ["Moscow", "New York"]}}

Добавление в пустой словарь ключей с значениями.
#test_dict={}
#test_dict[5] = [3,4,5]
#test_dict[(3,4,5)] = 'strong man'
#print(test_dict)  -----> {5: [3, 4, 5], (3, 4, 5): 'strong man'}

#test_dict={}
#test_dict.update({5:[3,4,5], (3,4,5):'strong man'})
#print(test_dict) -----> {5: [3, 4, 5], (3, 4, 5): 'strong man'}