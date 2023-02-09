
Пользователю предлагается ввести данные
Функция input() также предоставляет возможность выводить подсказки к тому, что программа хочет увидеть от пользователя.
name = input("Please enter your first name:")
print("Hello,", name)

ДАННЫЕ	                     ТИП	             ПРИМЕРЫ

Целые числа                  int                   73
Числа с плавающей точкой     float                3.14
Строки                       str              "Hello, world!"
Логические переменные        bool             True  False
Списки                       list              [1,2,3,4]
Кортежи                      tuple            (‘a’,’b’,’c’)
Словари                      dict             {‘a’ : 1, ‘b’ : 2}  
Множества                    set              {‘a’, 1, ‘b’, 2}


НЕИЗМЕНЯЕМЫЕ ТИПЫ	                ИЗМЕНЯЕМЫЕ ТИПЫ
Целые числа (int)	                  Списки (list)
Числа с плавающей точкой (float)	   Словари (dict)
Строки (str)	                      Множества (set)
Логические переменные (bool)	
Кортежи (tuple)



type узнать тип данных
a = 'aaa'.
if type(a) is str:
print(True)

ОПЕРАЦИЯ	          ОБОЗНАЧЕНИЕ	       ПРИМЕР
Сложение	             +	              7+5 = 12
Вычитание	             –	              7-5 = 2
Умножение	             *	              7*5 = 35
Возведение в степень	 **	              7**5 = 16807
Деление	                 /	              5/2 = 2.5
Целочисленное деление	//	              7//5 = 1
Остаток от деления   	%	              7%5 = 2

round(): округление чисел.
print(round(3.14/2, 1)) # второй аргумент — желаемое количество знаков

Встроенная функция len() позволяет узнать длину строки (то есть количество символов в ней):

s = "Hello!"
print(len(s)) ---> 6

Метод find(substr), определённый для строк, позволяет находить символы и подстроки:
print(s.find('e')) # возвращает индекс
# 1

Приведённые ниже методы позволяют привести все буквы к верхнему регистру (заглавным буквам) 
или к нижнему регистру (строчным буквам).

print(s.upper())
# HELLO!
print(s.lower())
# hello!
print(s)
# Hello!

Метод replace(): первым аргументом в него передаётся символ, который необходимо заменить, вторым аргументом — то, на что его надо заменить.
text = text.replace(" ", "") #заменяем пробелы на пустые строки

Метод split() разделяет строку на несколько подстрок

colors = 'red blue green'
print(colors.split())  ---> ['red', 'blue', 'green']

colors = 'red blue green'
print(colors.split()[1])  ---> blue 

animal = 'bear,1,0,0,1,0,0,1,1,1,1,0,0,4,0,0,1,1'
print(animal.split(',')) ---> ['bear', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '4', '0', '0', '1', '1']

#\n — символ переноса строки;
#\t — символ горизонтальной табуляции;
#\v — символ вертикальной табуляции.

colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности
colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue



Метод .format() устаревший

print('The {} currency rate on the date {} is {}'.format(currency, cur_date, rate))

Метод f

cur_date = input('Enter date: ')
currency = input('Enter currency: ')
rate = input()

print(f'The {currency} currency rate on the date {cur_date} is {rate}')

Пример sep=" "
print(25, 125, 625) ---> 25 125 625

Параметр sep удобно использовать, чтобы сделать вывод программы более читабельным.
print(25, 125, 625, sep=', ') ---> 25, 125, 625


Пример end=" "

Этот аргумент задаёт символ, которым заканчивается печатаемая строка (по умолчанию это перенос на новую строку — символ \n).

print("Shopping list:")          --->     Shopping list:
print("bread", "butter", "eggs")          bread butter eggs

Теперь мы напечатаем текст в одну строку.
print("Shopping list:", end=' ')   ---> Shopping list: bread butter eggs
print("bread", "butter", "eggs")



