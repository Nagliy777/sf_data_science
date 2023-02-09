Условный оператор позволяет выполнять определённые вами команды при некотором условии. 
Условие задаётся логическим выражением, которое может принимать два значения («истина» или «ложь») 
и в зависимости от этого выполнять какие-то действия или, наоборот, пропускать их.


ОПЕРАТОР  СИНТАКСИС ВЫРАЖЕНИЯ     ЗНАЧЕНИЕ         ОПЕРАЦИЯ
+=          a += b                a = a + b        Сложение, совмещённое с присваиванием
-=          a -= b                a = a - b        Вычитание, совмещённое с присваиванием
*=          a *= b                a = a * b        Умножение, совмещённое с присваиванием 
/=          a /= b                a = a / b        Деление, совмещённое с присваиванием 
//=         a //= b               a = a // b       Целочисленное деление, совмещённое с присваиванием 
%=          a %= b                a = a % b        Вычисление остатка от деления, совмещённое с присваиванием


if Условие:
   Блок инструкций1
else:
   Блок инструкций 2

is_rainy = True  # дождь будет

if is_rainy:
    print("Take an umbrella") # брать зонт
else:
    print("Don't take an umbrella") # не брать зонт

Пример:
#s = 5
#a = 10
#if a > 0:
#    s = s + a
#else:
#    s = s - a

#print (s)  ---> 15

Пример:
#is_rainy = True  # дождь будет
#heavy_rain = True  # несильный дождь

#if is_rainy:
     в данный блок дописали ещё один условный оператор
#    if heavy_rain:
#        print("Put on a raincoat") #надеть дождевик 
#    else:
#        print("Take an umbrella") #брать зонт
#else:
#    print("Don't take an umbrella") #не брать зонт


#mx = 0
#s = 0
#x = -5
    
#if x < 0:
#    s = x

#if x > mx:
#    mx = x

#print(s)
#print(mx)    

Пустое значение или ноль - False
print(bool(0))   ---> False
print(bool(1))   ---> True

print(bool(""))  ---> False
print(bool("1"))  ---> True

print(bool([]))  ---> False
print(bool([1])) ---> True  


Если ваша задача — проверить, можно ли делить и является ли делитель нулём, 
то проверку в явном виде zero != 0 делать излишне

# Плохо
if zero != 0:
    print(10 / zero)
else:
    print("You can't divide by zero") # делить на ноль нельзя

# Хорошо
if zero:
    print(10 / zero)
else:
    print("You can't divide by zero") # делить на ноль нельзя

Если вам нужно проверить, пустая строка или нет, то делать это таким способом password == "",
а уж тем более таким len(password) == 0 ни к чему. 

# Плохо
if password == "":
    print("You forgot to enter a password") # вы забыли ввести пароль
else:
    ...

# Очень плохо
if len(password) == 0:
    print("You forgot to enter a password") # вы забыли ввести пароль
else:
    ...

# Хорошо
if not password:
    print("You forgot to enter a password") # вы забыли ввести пароль
else:
    ...   



#Пример:
x = -1
y = 2


if x > 0 and y > 0:
    print("Первая четверть") 

if x > 0 and y < 0:
    print("Четвёртая четверть") 


if x < 0 and y > 0:
    print("Вторая четверть")    


if x < 0 and y < 0:
    print("Третья четверть")

#Пример:
a = 18
if a % 2 == 0 and a % 3 == 0:
    print('Number A is divisible by 2 or by 3')

#Пример с функцией. В функции return вместо print :
Запишите вместо вопросительных знаков выражение, которое вернет True, когда каждое из чисел А и В нечетное.

A = 21
B = 4

def are_both_odd(A, B):
    return A%2 >0 and B%2 > 0


#Пример:
def get_wind_class(speed):
    if  1 <= speed <= 4:
        return 'weak [1]'
    elif 5 <= speed <= 10:
        return 'moderate [2]'
    elif 11 <= speed <= 18:
        return 'strong [3]'
    elif 19 <= speed: 
        return 'hurricane [4]'

#Пример:
Чтобы данное время суток считалось утром, оно должно быть больше либо равно 6 
и одновременно строго меньше 12, поэтому условие будет выглядеть следующим образом:

if hour >= 6 and hour < 12:
    print("Morning!") # Утро!

Лаконично:
if 6 <= hour < 12:
    print("Morning!") # Утро!


#Пример:
elif - а если

Если условие if или какого-либо elif по порядку выполняется, то программа сразу переходит в основную ветку программы 
(нижний голубой прямоугольник), а все нижестоящие elif пропускаются.

month = int(input())

if month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
elif month in [12, 1, 2]:
    print("Winter")

#Пример:
a = 42
b = 41
result = a if a > b else b
print(result) ---> 42

x = 10
result = 'greater' if x > 6 else 'less'
print(result) ---> greater


#Пример:
a = 876585679
b = str(a)

if b == b[::-1]:
    print(True)
else:
    print(False)




Пример:
Вам дан словарь user_database с именами пользователей и их паролями. Допишите функцию check_user так, 
чтобы она по логину пользователя проверяла, существует он или нет, после чего с помощью вложенного условия 
проверяла правильность пароля этого пользователя.
Функция должна возвращать только True или False.
Примечание: чтобы вернуть True, напишите "return True"; чтобы вернуть False, напишите "return False".


user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}



def check_user(username, password):
    if username in user_database:
       if password ==  user_database[username]:
            return True
                    
    else: 
        return False


x = 5
'greater' if x > 6 else 'less'


Пример с исключением:
#Создайте скрипт, который будет принимать строки в input(). Строки необходимо конвертировать в числа (добавьте для этого try-except).
#В случае удачного выполнения скрипта пусть выведется: «You entered a right number» (Вы ввели правильное число).
#В конце скрипта обязательно должна быть надпись «Exit» (Выход из программы).

try: # Добавляем конструкцию try-except для отлова нашей ошибки
    print("Before exception") # перед исключением
    # теперь пользователь сам вводит числа для деления
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b # здесь может возникнуть исключение деления на ноль
    print(c) # печатаем c = a / b, если всё хорошо
except ZeroDivisionError as e: # Добавляем тип именно той ошибки, которую хотим отловить.
    print("ZeroDivisionError")
else:
    print("You entered a right number")  #код, который выполнится только в случае, если в try ничего не сломалось*
finally:
    print('Exit') #код, который выполнится в любом случае*




