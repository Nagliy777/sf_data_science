"'A game Guess the number'"
import numpy as np

number = np.random.randint(1,101) #* Загадываем число

#* Количество попыток
count=0

while True:
    
    count+=1
    predict_number=int(input("Guess the numberfrom 1 to 100:"))
    
    if predict_number > number:
       print('Число должно быть меньше')
    elif predict_number < number:
       print('Число должно быть больше')
    else:
        predict_number == number
        print(f'Вы угадали число за {count} попыток. Это число {number} ')
        break #* Выход из цикла,игра завершена.
        
    
