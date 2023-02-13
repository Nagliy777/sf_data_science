Модуль Collections. Counter и defaultdict

#Объект Counter (от англ. «счётчик») предназначен для решения часто возникающей задачи по подсчёту
#различных элементов.

# Импортируем объект Counter из модуля collections
from collections import Counter
# Создаём пустой объект Counter
c = Counter()
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter()
for car in cars:
    c[car] += 1
 
 print(c) ---> Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})
 
 Однако гораздо проще при создании Counter сразу передать в круглых скобках итерируемый объект, 
в котором необходимо посчитать значения:

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter(cars)
print(c) ---> Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})

Узнать, сколько раз встретился конкретный элемент, можно, обратившись к счётчику по ключу 
как к обычному словарю:
print(c['black']) ---> 3

Если обратиться к счётчику по несуществующему ключу, то, в отличие от словаря, ошибка KeyError не возникнет:

print(c['purple']) ---> 0

Узнать сумму всех значений в объекте Counter можно, воспользовавшись следующей конструкцией:
print(sum(c.values())) ---> 9

Счётчики можно складывать и вычитать.
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow)  ---> Counter({'black': 4, 'yellow': 3, 'white': 2})
print(counter_spb) ---> Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})

print(counter_moscow + counter_spb) ---> Counter({'black': 6, 'white': 5, 'yellow': 5, 'red': 2})

Чтобы узнать разницу между объектами Counter, необходимо воспользоваться функцией subtract.
Функция subtract модифицирует исходный счётчик.
    
counter_moscow.subtract(counter_spb)
print(counter_moscow) --->  Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2}) 

Чтобы получить список всех элементов, которые содержатся в Counter, используется функция elements().
Элементы возвращаются в порядке появления уникальных элементов. 

print(*counter_moscow.elements()) ---> black black black black white white yellow yellow yellow

 Чтобы получить список уникальных элементов, достаточно воспользоваться функцией list():
     
print(list(counter_moscow)) ---> ['black', 'white', 'yellow']


С помощью функции dict() можно превратить Counter в обычный словарь:

print(dict(counter_moscow)) ---> {'black': 4, 'white': 2, 'yellow': 3}
    
Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:

print(counter_moscow.most_common()) ---> [('black', 4), ('yellow', 3), ('white', 2)]

В неё можно передать значение, которое задаёт число первых наиболее частых элементов, например, 2:

print(counter_moscow.most_common(2)) ---> [('black', 4), ('yellow', 3)]

Наконец, функция clear() позволяет полностью обнулить счётчик:
    
counter_moscow.clear()
print(counter_moscow) --->  Counter()


