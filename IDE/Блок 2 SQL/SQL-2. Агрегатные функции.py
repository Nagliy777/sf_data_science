
#? Убираем повторяющиеся значения

#* Для начала получим все основные типы покемонов.

SELECT
    type1
FROM sql.pokemon

#* Видно, что типы повторяются, потому что в результате запроса вы получаете все строки, которые подходят
#* под заданные условия.
#todo Чтобы получить уникальные значения из столбца, воспользуемся ключевым словом DISTINCT.

SELECT DISTINCT
    type1
FROM sql.pokemon

#todo Мы можем применять DISTINCT и для нескольких столбцов.

SELECT DISTINCT
    type1,
    type2
FROM sql.pokemon

#? Агрегатные функции

#* Кроме простых математических операций, которые мы использовали в предыдущем модуле,
#* СУБД позволяет проводить статистические вычисления для нескольких строк.

#todo Давайте посчитаем количество строк в таблице. Для этого применим агрегатную функцию COUNT.

SELECT
    COUNT(*)
FROM sql.pokemon

#* COUNT считает строки, а звёздочка (*) в аргументе функции означает, что считаются
#* все строки, которые возвращает запрос.

#todo Если в аргументе функции указать название столбца, функция обработает только строки с непустым значением.

SELECT
    COUNT(type2)
FROM sql.pokemon

#todo Внутри функции COUNT мы можем также применять DISTINCT, чтобы вычислить количество уникальных значений.

SELECT
    COUNT(DISTINCT type1)
FROM sql.pokemon

#? ОСНОВНЫЕ АГРЕГАТНЫЕ ФУНКЦИИ

COUNT — вычисляет число непустых строк;
SUM — вычисляет сумму;
AVG — вычисляет среднее;
MAX — вычисляет максимум;
MIN — вычисляет минимум.

#todo Найдите максимальное значение атаки среди всех покемонов.

SELECT max(attack)   
FROM sql.pokemon

#todo Какое среднее количество очков здоровья у покемонов-драконов (то есть тех, у кого основной тип — Dragon)?

SELECT AVG(HP)
FROM sql.pokemon
where type1 = 'Dragon'

#todo Кроме того, мы можем применять несколько агрегатных функций в одном запросе.

SELECT
    COUNT(*) AS "всего травяных покемонов",
    COUNT(type2) AS "покемонов с дополнительным типом",
    AVG(attack) AS "средняя атака",
    AVG(defense) AS "средняя защита"
FROM sql.pokemon
WHERE type1 = 'Grass'


#todo Напишите запрос, который выведет:

#* количество покемонов (столбец pokemon_count),
#* среднюю скорость (столбец avg_speed),
#* максимальное и минимальное число очков здоровья (столбцы max_hp и min_hp)
#* для электрических (Electric) покемонов, имеющих дополнительный тип и показатели атаки или защиты больше 50.

SELECT COUNT(id) AS "pokemon_count",
       AVG(speed) AS "avg_speed",
       MAX(HP) AS "max_hp",
       MIN(HP) AS "min_hp"       
FROM sql.pokemon
where type1 = 'Electric' AND type2 IS NOT NULL AND (attack > 50 OR  defense > 50)

#? Группировка

#todo Прежде мы применяли агрегатные функции для всего вывода, а сейчас используем для
#todo  различных групп строк. Поможет нам в этом ключевое слово GROUP BY.
#todo GROUP BY используется для определения групп выходных строк, к которым могут
#todo  применяться агрегатные функции.

#todo Выведем число покемонов каждого типа.
SELECT
    type1 AS pokemon_type,
    COUNT(*) AS pokemon_count
FROM sql.pokemon
GROUP BY type1
ORDER BY type1

#todo Представим ТОП существующих типов покемонов.
SELECT
    type1 AS pokemon_type,
    COUNT(*) AS pokemon_count
FROM sql.pokemon
GROUP BY pokemon_type
ORDER BY COUNT(*) DESC

#todo Использовали в группировке не название столбца, а его алиас.

SELECT
    type2 AS pokemon_type,
    COUNT(*) AS additional_types_count
    AVG(hp) AS avg_hp
    SUM(attack) AS attack_sum
FROM sql.pokemon
GROUP BY type2
ORDER BY type2, type1 DESC, ASK


#todo Напишите запрос, который выведет:

#todo число различных дополнительных типов (столбец additional_types_count),
#todo среднее число очков здоровья (столбец avg_hp),
#todo сумму показателей атаки (столбец attack_sum) в разбивке по основным типам (столбец primary_type).
#todo Отсортируйте результат по числу дополнительных типов в порядке убывания, при равенстве — по основному
#todo типу в алфавитном порядке. Столбцы к выводу (обратите внимание на порядок!): primary_type,
#todo additional_types_count, avg_hp, attack_sum.

SELECT
     type1 AS primary_type,
    COUNT(DISTINCT type2) AS additional_types_count,
    AVG(hp) AS avg_hp,
    SUM(attack) AS attack_sum
FROM sql.pokemon
GROUP BY type1
ORDER BY additional_types_count DESC, type1 ASC

#todo Мы можем осуществлять группировку по нескольким столбцам.

SELECT
    type1 AS primary_type,
    type2 AS additional_type,
    COUNT(*) AS pokemon_count
FROM sql.pokemon
GROUP BY 1, 2
ORDER BY 1, 2 NULLS FIRST

#todo  В группировке можно указывать порядковый номер столбца так же, как мы
#todo делали это в прошлом модуле для сортировки.

#todo GROUP BY можно использовать и без агрегатных функций. Тогда его действие будет
#todo равносильно действию DISTINCT.

SELECT DISTINCT              SELECT
    type1                         type1 
FROM sql.pokemon             FROM sql.pokemon
                             GROUP BY type1
                             
                             
#? Фильтрация агрегированных строк                 

#todo Если ключевое слово WHERE определяет фильтрацию строк до агрегирования, то для фильтрации
#todo уже агрегированных данных применяется ключевое слово HAVING.

#todo HAVING обязательно пишется после GROUP BY.

#* Выведем типы покемонов и их средний показатель атаки, при этом оставим только тех, у кого
#* средняя атака больше 90.   

SELECT
    type1 AS primary_type,
    AVG(attack) AS avg_attack
FROM sql.pokemon
GROUP BY primary_type 
HAVING AVG(attack) > 90

#* В HAVING можно использовать все те же условия, что и в WHERE.    

#todo В квадратных скобках указаны необязательные предложения: они могут отсутствовать в операторе SELECT.
#todo Структура:
SELECT [ALL | DISTINCT] список_столбцов|*
FROM список_имён_таблиц
[WHERE условие_поиска]
[GROUP BY список_имён_столбцов]
[HAVING условие_поиска]
[ORDER BY имя_столбца [ASC | DESC],…]


#todo Напишите запрос, который выведет основной и дополнительный типы покемонов (столбцы
#todo primary_type и additional_type) для тех, у кого средний показатель атаки больше 100
#todo и максимальный показатель очков здоровья меньше 80.

SELECT DISTINCT 
    type1 AS primary_type,
    type2 AS additional_type
FROM sql.pokemon
group by type1, type2
having AVG(attack) > 100 AND MAX(HP) < 80    



                
      

