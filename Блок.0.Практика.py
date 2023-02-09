#Напишите функцию get_unique_words(), которая избавляется от знаков препинания в тексте и возвращает упорядоченный список 
#(слова расположены по алфавиту) из уникальных (неповторяющихся) слов. Учтите, что слова, написанные в разных регистрах считаются одним и тем же словом.
#Можно использовать готовый список со знаками препинания:
#punctuation_list = [', '', '', '', '', '']

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_unique_words(text):
	punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')',"'"]
	for i in punctuation_list:
		text=text.replace(i,'')
		text=text.lower()
		a=text.split()
		a=list(set(a))		
		a.sort()


	return a


print(get_unique_words(text_example))



#Необходимо написать функцию get_most_frequent_word(text), которая возвращает самое часто встречающееся слово в тексте text. 
#Не забудьте очистить тест от знаков пунктуации и привести текст к единому регистру (слова в верхнем и нижнем регистре считаются одним и тем же словом).
#Для решения можно использовать функцию из предыдущего задания.
#Примечание: в случае, если в тексте встречаются два слова с одинаковой повторяемостью, 
#функция должна возвращать то, которое начинается с буквы, идущей в алфавите раньше. Например, если слова я и меня встречаются одинаковое количество раз, 
#то функция должна вернуть слово меня.

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

k={}
l=[]

def get_most_frequent_word(text):
	punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')',"'"]
	x = 1
	for i in punctuation_list:
		text=text.replace(i,'')
		text=text.lower()
		a=text.split()			
		a.sort()
		for i in a:
			p=a.count(i)
			if p >= x:
					x=p
					k[i]=x
					m=list(k.values())
					j=list(k)
		print(k)
		for q in a:
			c=a.count(q)
			if m[-1] <= c:
				l.append(q)
				l.append(j[-1])
				l.sort()
				
				return l[0]

		else:				
			return j[-1]
				
					
print(get_most_frequent_word(text_example))


#Разработайте функцию holes_count(number), которая подсчитывает количество отверстий в заданном числе number. 
#Например, в цифре 8 два отверстия, в цифре 9 - одно. В числе 146 - два отверстия.
#Подсказка: используйте словарь для записи количества отверстий в цифрах.


holes_dict = {"0": 1, "4": 1, "6": 1, "8": 2, "9": 1}

def holes_count(number):
	count=0	
	for i in str(number) :		
		if i in holes_dict:

			count += holes_dict.get(i, 0)

	return count



print(holes_count(688))

#Напишите программу, которая запрашивает у пользователя следующие данные : username, age, email о нескольких пользователях и собирает эти данные в структуру:
#[(1, {'username': user1, 'age': age1, 'email': email1}), 
#(2, {'username': user2, 'age': age2, 'email': email2}), ... ]
#Первый элемент каждого кортежа — порядковый номер пользователя, второй элемент — словарь с данными.
#В итоге должен получиться список с кортежами.
#Далее необходимо провести аналитику (собрать данные о пользователях в словарь)
#{'username': [user1, user2, ...],
#'age': [age1, age2, ...],
#'email': [email1, email2, ...]}
#и вывести эту аналитику на экран.


num_users = int(input('Enter number of users: '))
user_analytics = {'username': [], 'age': [], 'email': []}
user_list = []

for i in range(num_users):
    user = {}
    user['username'] = input("Enter username: ")
    user['age'] = int(input("Enter user age: "))
    user['email'] = input("Enter user email: ")
    user_analytics['username'].append(user['username'])
    user_analytics['age'].append(user['age'])
    user_analytics['email'].append(user['email'])
    user_list.append((i + 1, user))

print(user_list)
print(user_analytics)

#Напишите функцию find_min_number(), которая принимает три числа на вход и возвращает наименьшее из них.
#Используйте для решения задачи условия.

def find_min_number(a, b, c):
	if a < b and a<c:
		return a
	elif b < a and b<c:
		return b
	elif c < a and c<b:
		return c

print(find_min_number(5, 11, 4))

#Напишите функцию sum_min_numbers(), которая также принимает на вход три числа и возвращает сумму двух наименьших.
#Используйте для решения задачи условия.

def sum_min_numbers(a, b, c):
	if a < b < c or b < a < c:
		return a+b
	elif c < b < a or b < c < a:
		return c+b
	elif c < a < b or a < c < b:
		return c+a
		
print(sum_min_numbers(10, 25, 16))

#Напишите функцию is_divided_by_six(number), которая проверяет, делится ли число на 6.


def is_divided_by_six(number):
	if number %6 ==0:
		return True
	else:
		return False


print(is_divided_by_six(7))

#Напишите функцию division(a, b), которая осуществляет деление двух чисел.
#Необходимо реализовать внутри функции отлов исключения ZeroDivisionError на случай, если пользователь при вызове функции попытается поделить на ноль.
#Функция принимает на вход два числа — делимое и делитель, и возвращает частное.
#Если в процессе выполнения функции было поймано исключение ZeroDivisionError, 
#то на экран нужно вывести сообщение Zero division error! с помощью функции print(), а затем вернуть значение None из функции.

def division(a, b):
	try:
		
		c=a/b

	except ZeroDivisionError:
		print("Zero division error!")
		return
	return c 

print(division(5, 1))


#Напишите функцию lucky_ticket(), которая проверяет, является ли билет счастливым.
#Примечание: билет счастливый, если сумма первых трёх цифр равна сумме последних трёх цифр.
#На вход функция получает шестизначное число.


def lucky_ticket(ticket_number):
	ticket_number1=int(ticket_number//1000)
	ticket_number2=(ticket_number%1000)
	a=0
	b=0
	
	for i in str(ticket_number1):
		a+=int(i)

	for i in str(ticket_number2):
		b+=int(i)

	if a == b:
		return True
	else:
		return False

print(lucky_ticket(111112))

#Напишите функцию fib_number(n), которая получает на вход некоторое число n и выводит n-e число Фибоначчи.
#Задачу можно решить как с помощью цикла for, так и с помощью цикла while.
#Примечание 1: числа Фибоначчи определяются так a0 = 0, a1 = 1, a2 = a1 + a0 = 1,..., an = a_n-1 + a_n-2
#Примечание 2: в модуле по функциям уже было задание на вычисление чисел Фибоначчи с помощью рекурсивных функций. 
#Здесь необходимо реализовать те же вычисления, но без использования рекурсии.

def fib_number(n):
	lst=[0,1,1]

	if n == 0:			
		return 0
	elif n==1:
		return 1	
	elif n==2:		
		return 1
		
	for i in range(3,n+1):
		 lst.append(lst[-1]+lst[-2])
		 
		
	if i == n:
		return lst[-1]

			

print(fib_number(10)) ---> 55



#Напишите функцию even_numbers_in_matrix(matrix), которая получает на вход матрицу (список из списков) и возвращает количество четных чисел в ней.

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]


def even_numbers_in_matrix(matrix):
	p=[]
	for i in matrix:
		for a in i:
			if a%2 == 0:
				p.append(a)
			

	return len(p)
	
	
print(even_numbers_in_matrix(matrix_example))


#Напишите функцию matrix_sum(matrix1, matrix2), которая получает на вход две матрицы и возвращает их сумму.
#Примечание: чтобы найти сумму двух матриц, нужно просуммировать их соответствующие элементы. Но перед этим необходимо проверить, 
#что размеры матриц одинаковы (одинаковое количество столбцов и одинаковое количество строк). Если размеры матриц не совпадают, 
#то надо вывести на экран сообщение 'Error! Matrices dimensions are different!' с помощью функции print(), а затем вернуть значение None из функции matrix_sum().

#1 2 3   2 3 4   3 5 7
#2 3 4 + 4 5 6 = 6 8 10
#5 6 7   4 3 2   9 9 9



matrix1 = [[1, 5, 4], [4, 2, -2]]
matrix2 = [[1, 5, 4], [4, 2, -2]]



def matrix_sum(matrix1, matrix2):
	
	q=[]	
	if len(matrix1[0]) == len(matrix2[0]) and len(matrix1) == len(matrix2):
		
		a=len(matrix1)
		b=len(matrix1[0])	
		for i in range(a):
			p=[]			
			for k in range(b):
				p.append(matrix1[i][k]+matrix2[i][k])
			q.append(p)	
				
						
		return q

	
	else:
		print('Error! Matrices dimensions are different!')
		return 
	


print(matrix_sum(matrix1, matrix2))

#Реализуйте программу, которая сжимает последовательность символов. На вход подаётся последовательность вида:
#aaabbccccdaa
#Необходимо вывести строку, состоящую из символов и количества повторений этого символа. Вывод должен выглядеть как:
#a3b2c4d1a2

str_example = 'aaabbccccdaa'
first_symbol = str_example[0]
count = 0
new_str = ''
for symbol in str_example:
    if symbol == first_symbol:
        count += 1
    else:
        new_str += first_symbol + str(count)
        first_symbol = symbol
        count = 1

new_str += first_symbol + str(count)

print(new_str)

#Напишите функцию def distance_between_dots().
#Функция должна получать на вход координаты двух точек (в виде четырёх чисел) и возвращать расстояние между ними.
#Чтобы посчитать расстояние между точками, нужно воспользоваться формуло
#(x1-x2)**2+(y1-y2)**2**(1/2)

def distance_between_dots(x1,x2,y1,y2):
	try:
		coord = [x1,x2,y1,y2]
		for i in coord:
			if type(i) is not int and type(i) is not float:
				raise ValueError
	except ValueError:
		print("Arguments are not numbers!")
		return
		
	distance = ((x1-x2)**2)+((y1-y2)**2)**(1/2)
	return distance
		 



print(distance_between_dots(1, 1, 5, 1))

#Напишите функцию, которая вычисляет среднее арифметическое значений списка.
#Примечание: среднее арифметическое считается как сумма всех чисел, делённая на их количество.
#Не забудьте проверить значение полученного аргумента!


def num(x):
	k=0
	for i in x:
		k+=i
	
	m=k/len(x)
	return m

print(num([6,8]))

Или с ламбдой:
m =lambda x: sum(x)/len(x)
print(m([6,8]))