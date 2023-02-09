"'A game Guess the number'"
"'Компьютер сам загадывает и сам угадывает'"
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): загаданное число Defaults to 1.

    Returns:
        int: Число попыток
    """
    

    #* Количество попыток
    count=0

    while True:
    
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break              #Выход из цикла, если угадал
    return count

def score_game(random_predict) -> int:
    """за какое количество попыток в среднем за 1000 раз число от 1 до 100 угадываем 
    
    Args:
        random_predict (_type_): фуекция угадывания

    Returns:
        int: среднее количество
    """
    count_ls=[]
    np.random.seed(1)
    random_array=np.random.randint(1,101, size=(1000))# загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score= int(np.mean(count_ls))
    print(f'Ваш алгоритм угадыват число в среднем за {score} попыток')
    return score

#
#Launch
if __name__ == '__main__':
    score_game(random_predict)
    