# Модуль 8. Инструменты для Data Scince.
# 8. Итоги. Финальное задание
# Угадай число за минимальное количество попыток.

## Оглавление  
[1. Описание проекта](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Этапы-работы-над-проектом)  
[5. Результаты](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Результаты)    
[6. Выводы](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число меньше чем за 20 попыток.

:arrow_up:[к оглавлению](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число меньше чем за 20 попыток.

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на Python.
Учимся работать с IDE.
Учимся работать с GitHub.


### Краткая информация о данных
1.def game_core_v3(number: int = 1) -> int: функция угадывания. 
2.def score_game(game_core_v3) -> int: функция определения среднего количества угадываний за 1000 подходов.
3.Переменная "random_array" принимает загаданный список чисел.
4.Переменная "number" загаданное число из списка. чисел.
  
:arrow_up:[к оглавлению](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Оглавление)


### Этапы работы над проектом  
1.Написать код для функции угадывания таким образом, чтобы количество попыток угадывания было меньше 20.
2.Написать код для функции определения среднего количества угадываний за 1000 подходов.
3.Результат вывести в Jupyter Notebook.

:arrow_up:[к оглавлению](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Оглавление)


### Результаты:  
Код размещён [по ссылке](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/game_v3.py)

:arrow_up:[к оглавлению](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Оглавление)


### Выводы:  
Алгоритм угадывает число в среднем за 16 попыток, что соответствует требованию задания.
В Jupyter Notebook [можно ознакомиться с результатом алгоритма](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/game_v3.ipynb)

:arrow_up:[к оглавлению](https://github.com/Nagliy777/sf_data_science/blob/main/IDE/project_final/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами