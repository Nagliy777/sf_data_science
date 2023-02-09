С помощью циклов можно повторять сколько угодно раз код, написанный в теле цикла, — особенном блоке кода, который находится внутри цикла
Тело цикла — это набор команд, находящихся на одном (4 пробела) и более отступе от отступа самого цикла.
Другими словами, тело цикла — это те команды, которые находятся внутри него и будут повторяться.
Итерация — это один шаг цикла, повторное применение операции, прописанной в теле цикла.

Для работы с циклом for используется следующая конструкция:
for — ключевое слово, с которого начинается цикл, отправная точка.
value — переменная цикла (может иметь другое название), в которой на каждом шаге цикла (итерации) 
содержится текущее значение из итерируемого объекта iterator.
in — оператор принадлежности, который указывает, откуда берутся значения для переменной value.
iterator — итерируемый объект (итератор) из которого на каждой итерации достаются элементы 
(например, список, словарь, кортеж, строка и т. д.).

for value in iterator:
    # Начало блока кода с телом цикла
    ...
    ...
    ...
    # Конец блока кода с телом цикла
# Код, который будет выполняться после цикла


Создаём цикл по всем пользователям из списка users
for user_id in users:
    #Начало блока кода с телом цикла
    send_message(user_id) #Отправляем уведомление о скидках
    #Конец блока кода с телом цикла
#Код, который будет выполняться после цикла
#Выводим на экран сообщение об успешной отправке
#print('All messages have been sent')

#my_list= [5, 9, 19]
#for element in my_list:
#	print('Element', element) ---> Element 5 Element 9


ДЛИННАЯ ЗАПИСЬ	     СОКРАЩЁННАЯ ЗАПИСЬ
value = value + a	     value += a
value = value - a	     value -= a
value = value / a	     value /= a
value = value * a	     value *= a
value = value ** a	     value **= a

Пример
#incomes = [120, 38.5, 40.5, 80]
#s = 0

#for income in incomes: #income — текущее значение элемента списка
#    print('Current income', income) #выводим текущее значение переменной income
#    print('Current s', s) #выводим текущее значение переменной S
#    s += income #увеличиваем сумму доходов на значение income, равносильно S = S + income
#    print('New s', s) #выводим обновлённое значение переменной S
#   print() #выводим пустую строку для красивого отображения
#print('Answer: s=', s) #выводим результат 

#Без примерения цикла
#s = sum(incomes)
#print(s) ---> 279.0

#Пример:
S = 0  #создаём накопительную переменную, в которой будем считать сумму
N = 5 #задаём N — последний элемент последовательности

 создаём цикл for, которым мы будем проходить по всем числам от 1 до N (включительно)
for i in range(1, N + 1):  #равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Current S: ", S) #выводим значение суммы на текущем шаге
    print("Current number: ", i) #выводим текущее число
    S += i  #суммируем текущее число i и перезаписываем значение суммы, равносильно S = S + i
    print("Sum after addition: ", S) #выводим значение суммы после сложения
    print("---") #выводим строчку для визуального разделения результатов
print("Answer: sum = ", S) #выводим ответ в формате ответ: сумма равна =


#Пример:
weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15] #список масс товаров

max_weight = 100 #задаём максимальное значение веса груза
num = 1 #задаём начальный номер груза
создаём цикл по элементам списка с массами товаров
for weight in weight_of_products: #weight — текущее значение веса
    if weight < max_weight: #если текущий вес меньше максимального,
        #выводим номер груза, его вес и отправляем его в легковую машину
        print('Product {}, weight: {} -passenger car'.format(num, weight)) 
    else:
        #выводим номер груза, его вес и отправляем его в грузовую машину
        print('Product {}, weight: {} -truck'.format(num, weight))
    num += 1 #увеличиваем значение номера груза на 1


#Пример:
weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15] #список масс товаров
max_weight = 100 #задаём максимальное значение веса груза
N = len(weight_of_products) #вычисляем длину списка
#создаём цикл по последовательности чисел от 0 до N (не включая N)
for i in range(N): #i — текущее значение последовательности
    #обращаемся к элементу по индексу и сравниваем его с максимумом
    if weight_of_products[i] < max_weight: #если текущий вес меньше максимального,
        #выводим номер груза, массу и отправляем его в легковую машину
        print('Product {}, weight: {} -passenger car'.format(i+1, weight_of_products[i])) 
    else:
        #выводим номер груза, массу и отправляем его в грузовую машину
        print('Product {}, weight: {} -truck'.format(i+1, weight_of_products[i]))

#Пример:
places = [
    'Red Square',
    'Swallow Nest',
    'Niagara Falls',
    'Grand Canyon',
    'Louvre',
    'Hermitage'
] 
#словарь соответствия мест и стран
location = {
    'Red Square': 'Russia',
    'Swallow Nest': 'Russia',
    'Niagara Falls': 'USA',
    'Grand Canyon': 'USA',
    'Louvre': 'France',
    'Hermitage': 'Russia'
}
N = len(places) #вычисляем длину списка
#создаём цикл по списку мест, которые хотим посетить
for i in range(N): #i — текущее значение последовательности
    #places[i] — i-й элемент в списке places
    country = location[places[i]] #получаем страну из словаря location по ключу
    if country != 'Russia': #сравниваем название стран
        places[i] = 'Unavailable' #помечаем место как недоступное
print(places) #выводим результирующий список


#Пример
word_list = ['My', 'name', 'is', 'Egor']
n = ''
for i in word_list:
	n += i + ' '
	print(n)

#Пример
my_list = list(range(0, 100, 3))
k = "a"
p= []

for i in my_list:
	if  i % 2 == 0:
		p += list('a')
		print(p)
		print()
	
print(p.count('a'))

#Пример
my_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']

p = 0

for a in my_list:
	if type(a) == str:
		p += 1
		print(p) ---> 3


Такие структуры напоминают таблицу, и их ещё называют двумерными списками, 
а на математическом языке они называются двумерными матрицами.
temperature=[[13, 15, 10], [14, 13, 9], [8, 9, 6]].

print(temperature[1]) ---> [14, 13, 9]
print(temperature[1][2]) ---> 9
 Сначала мы обратились к списку по индексу, а потом к элементу списка.


Примечание. Стоит отметить, что в строгом математическом смысле матрица имеет ограничение на размерности её строк. 
Не может быть, чтобы в одной из строк матрицы было четыре элемента, а в другой — шесть.
В то же время во вложенном списке такая ситуация вполне возможна и не вызовет ошибки.


Способ 1. Циклы по строкам и их содержимому.
Пример:
 matrix = [
    [1, 2], 
    [3, 4], 
    [5, 6]
]
#создаём цикл по элементам списка matrix
for row in matrix: #row — текущее значение из списка matrix
    print('Current row', row) #выводим содержимое на экран
    #создаём цикл по элементам списка row
    for elem in row: #elem — текущее значение из списка row
        print('Current elem', elem)
    print() #отделяем вывод на экран пустой строкой


Способ 2. Циклы по индексам строк и столбцов.
Пример:

matrix = [
    [1, 2], 
    [3, 4], 
    [5, 6]
]

N = len(matrix) #вычисляем длину внешнего списка
M = len(matrix[0]) #вычисляем длину вложенного списка
#создаём цикл по последовательности чисел от 0 до N (не включая N)
for i in range(N): #i — текущий элемент последовательности (индекс строки)
    print('Current i', i) #выводим текущее значение i
    print('Current row', matrix[i]) #выводим i-е значение внешнего списка
    #создаём цикл по последовательности чисел от 0 до M (не включая M)
    for j in range(M):#j — текущий элемент последовательности (индекс столбца)
        print('Current j', j) #выводим текущее значение j
        print('Current elem', matrix[i][j]) #выводим элемент под индексами i и j
    print() #отделяем вывод на экран пустой строкой




Пример:
hours = list(range(10, 24, 5)) #создаём список часов
minutes = list(range(0, 60, 30)) #создаём список минут
#создаём цикл по элементам списка часов
for hour in hours: #hour — текущее значение часа (10, 15, 20)
    #создаём цикл по элементам списка минут
    for minute in minutes: #minute — текущее значение минуты
        print('Alarm is set {}:{}'.format(hour, minute)) #выводим время

Пример:
hours =  list(range(9, 24, 2))
minutes =  list(range(0, 60, 15))

for hour in hours:  
    for minute in minutes:  
        print(f'Alarm is set {hour}:{minute}')
    print()


Пример:

str_list = ['text', 'morning', 'notepad', 'television', 'ornament'] #заданный список строк
count = 0 #задаём начальное количество символов 'e'
#создаём цикл по элементам списка str_list
for text in str_list: 
    #создаём цикл по символам в строке text
    for symbol in text:
        #проверяем условие, что текущий символ == 'e'
        if symbol == 'e': #если условие истинно,
            count += 1 #увеличиваем количество символов 'e'
print("Count symbol 'e':", count) -----> Count symbol 'e': 5

Пример без условия и внутреннего цикла:

str_list = ['text', 'morning', 'notepad', 'television', 'ornament'] #заданный список строк
count = 0 #задаём начальное количество символов 'e'
#создаём цикл по элементам списка str_list
for text in str_list:
    #увеличиваем количество символов 'e' 
    count += text.count('e') #.count() считает, сколько раз символ встречается в строке text
print("Count symbol 'e':", count) -----> Count symbol 'e': 5
 

Пример нахождения наименьшего элемента в каждой строке:

random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
] #заданная матрица
min_value_rows = [] #задаём пустой список с минимальными значениями строк
#создаём цикл по строкам матрицы random_matrix 
for row in random_matrix: #row — текущая строка таблицы
    min_value = row[0] #начальное значение кандидата на минимум
    #создаём цикл по элементам списка row
    for elem in row: #elem — текущий элемент из списка row
        #проверяем условие, что текущий элемент меньше кандидата на минимум
        if elem < min_value: #если условие выполняется,
            min_value = elem #заменяем кандидата на минимум
    min_value_rows.append(min_value) #добавляем полученный минимум строки в список
print("Minimal elements:", min_value_rows) #выводим минимальные элементы


Пример:

student_scores = [
    [56, 90, 80],
    [80, 86, 92],
    [91, 76, 89],
    [91, 42, 60],
    [65, 30, 90]
] #заданная таблица со студентами
N = len(student_scores) #задаём число студентов
M = len(student_scores[0]) #задаём число экзаменов
summa = 0 #задаём начальное значение общего балла
math_sum = 0 #задаём начальное значение общего балла по математике
info_sum = 0 #задаём начальное значение общего балла по информатике
rus_sum = 0 #задаём начальное значение общего балла по русскому языку
#создаём цикл по последовательности от 0 до N (не включая N)
for i in range(N): #i — индекс строки
    math_sum += student_scores[i][0] #добавляем баллы по математике i-го студента
    info_sum += student_scores[i][1] #добавляем баллы по информатике i-го студента
    rus_sum += student_scores[i][2] #добавляем баллы по русскому i-го студента
    #создаём цикл по последовательности от 0 до M (не включая M)
    for j in range(M): #j — индекс столбца
        summa += student_scores[i][j] #добавляем баллы i-го студента по j-му экзамену
print('Average math score', math_sum/N) #выводим средний балл по математике
print('Average info score', info_sum/N) #выводим средний балл по информатике
print('Average rus score', rus_sum/N) #выводим средний балл по русскому языку
print('Average score', summa/(N*M)) #выводим общий средний балл


Пример:
test_matrix1 = [
    [7, -1, 2],
    [123, 2, -1],    
    [123, 5, 1]
]

a = len(test_matrix1)
b = len(test_matrix1[0])


for test in test_matrix1:
    if a == b:
        print(True)
    else:
        print(False)



СПОСОБ 1. ЦИКЛ ПО ЭЛЕМЕНТАМ СПИСКА
user_dynamics = [-5, 2, 4, 8, 12, -7, 5] #заданный список динамики пользователей
number = 1 #задаём номер дня
#создаём цикл по элементам списка user_dynamics
for dynamic in user_dynamics: #dynamic — текущее значение из списка
    print("Day {} : {}".format(number, dynamic)) #выводим номер дня и динамику на этот день
    number += 1 #увеличиваем номер дня
 
Day 1 : -5
Day 2 : 2
Day 3 : 4
Day 4 : 8
Day 5 : 12
Day 6 : -7
Day 7 : 5


СПОСОБ 2. ЦИКЛ ПО ИНДЕКСАМ СПИСКА

user_dynamics = [-5, 2, 4, 8, 12, -7, 5] #заданный список динамики пользователей
N = len(user_dynamics) #вычисляем длину списка
#создаём цикл по элементам последовательности от 0 до N (не включая N)
for i in range(N): #i — текущий индекс
    print("Day {} : {}".format(i+1, user_dynamics[i])) #выводим номер дня и динамику на этот день
 
Day 1 : -5
Day 2 : 2
Day 3 : 4
Day 4 : 8
Day 5 : 12
Day 6 : -7
Day 7 : 5

СПОСОБ 3. ЦИКЛ ПО ИНДЕКСАМ И ЭЛЕМЕНТАМ ОДНОВРЕМЕННО

Функция enumerate() создаёт цикл for по индексам и значениям списка user_dynamics. Переменные цикла назовём i и dynamic. 

user_dynamics = [-5, 2, 4, 8, 12, -7, 5] #заданный список динамики пользователей
#создаём цикл по индексам и элементам списка 
for i, dynamic in enumerate(user_dynamics): # i — индекс текущего элемента, dynamic — текущее значение из списка
    print("Day {} : {}".format(i+1, dynamic)) #выводим номер дня и динамику на этот день

Day 1 : -5
Day 2 : 2
Day 3 : 4
Day 4 : 8
Day 5 : 12
Day 6 : -7
Day 7 : 5

Пример:
user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
for i, user in enumerate(user_dynamics): 
    if user < 0: 
        print(f'Number day:{i+1}, Churn value: {user_dynamics[i]}') # выводим день и количество ушедших в этот день пользователей.


Благодаря оператору break любой цикл преждевременно заканчивает своё выполнение и переходит к основному коду программы.

Пример:

to_inventory = ['Blood Moon Sword', 'Sunset-colored sword', 'Bow of Stars', 'Gain Stone']
inventory = [] #задаём пустой инвентарь
#создаём цикл по элементам списка to_inventory
for item in to_inventory: #item — текущий элемент списка
    #проверяем условие, что инвентарь уже заполнен
    if len(inventory) == 3: #если условие выполняется,
        print('inventory is full!') #выводим предупреждение об ошибке
        break #завершаем работу цикла
    else:#в противном случае
        inventory.append(item) #добавляем предмет в инвентарь
print(inventory)#выводим результирующий инвентарь


Благодаря оператору continue цикл пропускает весь код до конца тела цикла и переходит на следующий шаг.

Пример:
client_status = {
    103303: 'yes', 
    103044: 'no',
    100423: 'yes',
    103032: 'no',
    103902: 'no'
}
#создаём цикл по ключам словаря client_status
for user_id in client_status: #user_id — текущий ключ словаря
    #если текущий статус == 'no',
    if client_status[user_id] == 'no':
        continue #переходим на следующую итерацию
    else:
        print('Send present user', user_id) #выводим сообщение об отправке





Цикл while : 
Цикл выполняется до тех пор, пока истинно его условие. Как только оно становится ложным, цикл прерывается.

Пример:
n = 27 #задаём число
#создаём бесконечный цикл
while True:
    #проверяем условие, что остаток от деления на 3 равен 0
    if n % 3 == 0: #если условие выполняется,
        n = n // 3 #новое число — результат целочисленного деления на 3
        if n == 1: #если в результате деления получили 1,
            print('n - is the power of the number 3!')#выводим утвердительное сообщение
            break #выходим из цикла
    else: #в противном случае
        print('n - is not the power of the number 3!') #выводим сообщение-опровержение
        break #выходим из цикла
#Будет выведено
#n - is the power of the number 3!

Пример:

x = 21 
y = 55
count = 0 #задаём начальное значение количества итераций
while x < y: #записываем условное выражение в цикл
    x += 2 #увеличиваем значение переменной x на 2, равносильно x = x + 2
    count += 1 #увеличиваем количество итераций на 1, равносильно count = count + 1
#выводим результирующее количество итераций
print('Number of iterations', count)

Пример:
weight = 67 #заданный вес входящего в лифт человека
max_weight = 400 #задаём грузоподъёмность
S = 0 #задаём суммарный вес людей в лифте
#создаём цикл, который будет работать, пока S не превысит max_weight 
while S < max_weight: #делай, пока...
    S += weight #увеличиваем суммарный вес, равносильно S = S + weight 
    print('Current sum weight', S) #выводим значение суммарного веса после обновления
print() #отделяем промежуточный вывод от результата пустой строкой
print(f'Overweight {S-max_weight} kg') #выводим итоговое значение перевеса

Пример:

S = 0  # создаём накопительную переменную, в которой будем считать сумму
n = 1  # задаём текущее натуральное число
 
# создаём цикл, который будет работать, пока сумма не превысит 500
while S < 500:  # делай, пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # увеличиваем значение натурального числа
    print("Still counting ...") #выводим строку ожидания
print() #отделяем промежуточный вывод от результата пустой строкой
print("Sum is: ", S) #выводим результирующую сумму
print("Numbers total: ", n-1) #выводим результирующее количество чисел

Пример:
secret_passwords = {
    'Enot': 'ulybaka',
    'Agent12': '1password1',
    'MouseLulu': 'myshkanaruhka'
} #база позывных и паролей
#создаём бесконечный цикл
while True:
    name = input('Enter your name: ') #запрашиваем у пользователя позывной
    #проверяем, что позывной есть среди ключей словаря
    if name in secret_passwords: #если позывной верный
        password = input('Enter your password: ') #запрашиваем у пользователя пароль
        #проверяем, что введённый пароль совпадает со значением по ключу позывного
        if password == secret_passwords[name]: #если пароль верный,
            print('Welcome') #выводим приветственное сообщение
            break #завершаем цикл
        else: #если пароль неверный,
            print('Wrong password') #выводим сообщение об ошибке
    else: #если позывной неверный,
        print('Wrong name') #выводим сообщение об ошибке



Пример:
c=1000
a = 0

while True:
    if a*a > c:
        print(f'last natural number whose square does not exceed 1000: {a-1}')
        break
    a += 1   


Пример:

text = """
The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well.
 
Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled `ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.
 
`Well!' thought Alice to herself, `after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)
"""
text = text.lower() #приводим текст к нижнему регистру
text = text.replace(" ", "") #заменяем пробелы на пустые строки
text = text.replace("\n", "") #заменяем символы переноса строки на пустые строки
count_dict = {} #создаём пустой словарь для подсчёта количества символов
#создаём цикл по символам в строке text
for symbol in text: #symbol — текущий символ в тексте
    #проверяем условие, что символа ещё нет среди ключей словаря
    if symbol not in count_dict: #если условие выполняется,
        count_dict[symbol] = 1 #заносим символ в словарь со значением 1
    else: #в противном случае
        count_dict[symbol] += 1 #увеличиваем частоту символа
print(count_dict) #выводим результирующий словарь

Пример:
text = """
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
"""
text = text.lower() #приводим текст к нижнему регистру
text = text.replace("\n", " ") #заменяем символы переноса строки на пробелы
text = text.replace(",", "") #заменяем запятые на пустые строки
text = text.replace(".", "") #заменяем точки на пустые строки
text = text.replace(";", "") #заменяем точки с запятыми на пустые строки
word_list = text.split()
count_dict = {} #создаём пустой словарь для подсчёта количества слов
#создаём цикл по словам в списке word_list
for word in word_list: #word — текущее слово из списка word_list
    #проверяем условие, что слова ещё нет среди ключей словаря
    if word not in count_dict: #если условие выполняется,
        count_dict[word] = 1 #заносим слово в словарь со значением 1
    else: #в противном случае
        count_dict[word] += 1 #увеличиваем частоту слова
print(count_dict) #выводим результирующий словарь