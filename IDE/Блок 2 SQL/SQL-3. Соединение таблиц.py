
#! Соединение таблиц по ключу

#? ОБЪЕДИНЯЕМ ТАБЛИЦЫ БЕЗ ОПЕРАТОРОВ

#* Существует несколько способов соединения таблиц. Мы познакомимся со всеми основными операторами,
#* которые используются для этих нужд, но начнём с простого метода объединения таблиц — без операторов.

#* Чтобы соединить две таблицы между собой, достаточно записать названия таблиц через запятую в разделе from.
#* Каждая запись, которая есть в таблице teams, будет соединена с каждой записью в таблице matches.
#* Это действие также называют декартовым произведением таблиц.


SELECT *
FROM
    sql.teams,
    sql.matches
    
    
#* В таблице teams есть столбец api_id, а таблица matches содержит столбцы home_team_api_id и away_team_api_id — это ключи таблиц, по которым они соединяются.
#* Ключ — это поле (столбец) в таблице, которое позволяет однозначно идентифицировать запись (строку).
#* Чтобы соединить таблицы и получить данные о домашней команде по каждому матчу, добавим условие
#* where home_team_api_id = api_id.

SELECT *
FROM
    sql.teams,
    sql.matches
WHERE api_id = home_team_api_id

#* Аналогично можем получить данные о гостевых командах: необходимо изменить условие на
where away_team_api_id = api_id.

#todo Ключи нужны для того, чтобы иметь возможность не перепутать между собой различные записи.

#* Ключи бывают двух основных типов:

#* Primary — первичный ключ — служит для идентификации текущей таблицы и, как правило, идёт первым в списке столбцов. Всегда уникален: повторяющихся значений в основной таблице быть не может.
#* Foreign — внешний ключ — представляет собой ссылку на другую таблицу.

#todo мы можем выбирать, какие столбцы соединённой таблицы выводить.
#todo С помощью известного нам запроса получим названия команд, игравших домашние матчи, и счёт матчей.
SELECT 
    long_name, 
    home_team_goals,
    away_team_goals
FROM
    sql.teams,
    sql.matches
WHERE home_team_api_id = api_id

#! Знакомимся с JOIN

#* Для соединения таблиц мы использовали условие в разделе where, чтобы показать принцип работы оператора JOIN.
#todo JOIN — это оператор SQL, который позволяет соединять таблицы по условию.

SELECT 
    long_name,
    home_team_goals,
    away_team_goals
FROM    
    sql.teams
JOIN sql.matches on home_team_api_id = api_id

#? СИНТАКСИС

#* Оператор JOIN упрощает процесс соединения таблиц. Его синтаксис можно представить следующим образом:

SELECT
        столбец1,
	столбец2,
	...
FROM
	таблица1
JOIN таблица2 ON условие

#* Порядок присоединения таблиц в данном случае не важен — результат будет одинаковым.
#* С помощью JOIN можно соединить и более двух таблиц.

SELECT
        столбец1,
	столбец2,
	...
FROM
	таблица1
JOIN таблица2 ON условие
JOIN таблица3 ON условие

#* В таблицах, которые мы соединяем, могут быть одинаковые названия столбцов.

#todo К примеру, столбец id есть и в таблице matches, и в таблице teams. Такой запрос не будет обработан.
#todo Можно указать, откуда мы хотим запросить данные, записав название таблицы перед столбцом через точку.

SELECT
    teams.id
FROM 
    sql.teams
JOIN sql.matches ON home_team_api_id = api_id

#todo Упростить обращение к различным таблицам можно, присвоив им сокращённые названия — алиасы
#todo Название записывается без пробелов и операторов.
SELECT
        столбец1,
	столбец2,
	...
FROM
	таблица1 AS короткое_название_1
JOIN таблица2 AS короткое_название_2 ON условие

#todo Ключевое слово as, как и в названии столбца, можно опустить в большинстве СУБД.

#todo Напишите запрос, который выведет два столбца: id матча (match_id) и id домашней команды (team_id).
#todo Отсортируйте по id матча в порядке возрастания значений.

SELECT 
    matches.id AS match_id,
    teams.id AS team_id
    
FROM
    sql.teams AS teams
    JOIN  sql.matches AS matches ON api_id = home_team_api_id
ORDER BY match_id

#todo С помощью запроса SQL получим таблицу, содержащую:

#* название домашней команды;
#* количество забитых домашней командой голов;
#* количество забитых гостевой командой голов;
#* название гостевой команды.

SELECT
    h.long_name "домашняя команда",
    m.home_team_goals "голы домашней команды",
    m.away_team_goals "голы гостевой команды",
    a.long_name "гостевая команда" 
FROM
    sql.matches m
    JOIN sql.teams h ON m.home_team_api_id = h.api_id
    JOIN sql.teams a ON m.away_team_api_id = a.api_id
    
#todo Пример   

#*Напишите запрос, который выведет столбцы:
#* id матча,
#* короткое название домашней команды (home_short),
#* короткое название гостевой команды (away_short).
#* Отсортируйте запрос по возрастанию id матча.   
    
SELECT 
   m.id,
   h.short_name as home_short,
   a.short_name as away_short
FROM
    sql.matches AS m
    JOIN  sql.teams AS h ON h.api_id = m.home_team_api_id
    JOIN  sql.teams AS a ON a.api_id = m.away_team_api_id
ORDER BY m.id

#! Фильтрация и агрегатные функции

#? РАБОТА С ОБЪЕДИНЁННЫМИ ТАБЛИЦАМИ

#* К соединённым таблицам применимы функции фильтрации данных.
#* Например, можно вывести id матчей, в которых команда Arsenal была гостевой.

SELECT 
    m.id
FROM
    sql.teams t
    JOIN sql.matches m ON m.away_team_api_id = t.api_id
WHERE long_name = 'Arsenal'

#todo фильтруя записи одной таблицы, мы также будем фильтровать и записи другой таблицы, поскольку
#todo соединённые на уровне запроса таблицы по сути являются единой таблицей.

#todo Пример
#* Напишите запрос, который выведет полное название домашней команды (long_name), количество голов
#* домашней команды (home_goal) и количество голов гостевой команды (away_goal) в матчах, где
#* домашней командой были команды с коротким названием 'GEN'. Отсортируйте запрос по id матча
#* в порядке возрастания.

SELECT 
    h.long_name AS "long_name",
    m.home_team_goals AS "home_goal",
    m.away_team_goals AS "away_goal"
    
FROM
    sql.matches AS m
    JOIN  sql.teams AS h ON h.api_id = m.home_team_api_id
    JOIN  sql.teams AS a ON a.api_id = m.away_team_api_id
    
where h.short_name = 'GEN'
ORDER BY m.id

#todo Например, можно оставить только записи, в которых короткое название домашней команды GEN 
#todo и матчи сезона 2008/2009.

SELECT *
FROM    
    sql.matches m
    JOIN sql.teams t on t.api_id = m.home_team_api_id
WHERE
    t.short_name = 'GEN'
    AND m.season = '2008/2009'


#todo Пример
#* Напишите запрос, чтобы вывести id матчей, короткое название домашней команды (home_short), короткое
#* название гостевой команды (away_short) для матчей сезона 2011/2012, в которых участвовала команда
#* с названием Liverpool. Отсортируйте по id матча в порядке возрастания.

SELECT 
    m.id,
    h.short_name as home_short,
    a.short_name as away_short 
    
FROM
    sql.matches AS m
    JOIN  sql.teams AS h ON h.api_id = m.home_team_api_id
    JOIN  sql.teams AS a ON a.api_id = m.away_team_api_id
    
where m.season = '2011/2012' and (h.long_name = 'Liverpool' or a.long_name = 'Liverpool')
ORDER BY m.id


#? АГРЕГАЦИЯ ДАННЫХ
#todo К соединённым таблицам также применимы любые агрегатные функции — самые важные функции для анализа данных.

#todo Например, мы можем вывести сумму голов матча, забитых командами, агрегированную по гостевым командам
#todo (совокупное количество голов в матче, забитых обеими командами, суммированное в разрезе гостевых команд).

SELECT
    t.long_name,
    SUM(m.home_team_goals) + SUM(m.away_team_goals) match_goals
FROM
    sql.matches m
    JOIN sql.teams t ON m.away_team_api_id = t.api_id 
GROUP BY t.id

#* В данном запросе была использована группировка по столбцу id таблицы teams, хотя этот столбец
#* не выводится в запросе. Это необходимо для того, чтобы команды с одинаковым названием,
#* если такие найдутся, не группировались между собой. 

#todo Пример
#* Мы можем использовать оператор HAVING для фильтрации сгруппированных данных.
#* Поставим задачу — вывести таблицу с суммарным количеством забитых голов в матчах по командам
#* и сезонам для команд, в которых суммарное количество голов в матчах сезона больше 100.

SELECT
    m.season,
    t.long_name,
    SUM(m.home_team_goals) + SUM(m.away_team_goals) AS total_goals
FROM sql.matches m
JOIN sql.teams t ON t.api_id = m.home_team_api_id OR t.api_id = m.away_team_api_id
GROUP BY m.season, t.id
HAVING SUM(m.home_team_goals) + SUM(m.away_team_goals) > 100

#todo Пример
#* Напишите запрос, с помощью которого можно вывести список полных названий команд, сыгравших
#* в гостях 150 и более матчей. Отсортируйте список по названию команды.

SELECT
t.long_name

FROM sql.matches m
JOIN sql.teams t ON t.api_id = m.away_team_api_id
group by t.id
having count(t.long_name) >= 150
order by t.long_name

#! Способы соединения таблиц

#? ОПЕРАТОРЫ
#todo существует несколько различных видов соединений (join’ов)

#* Для INNER JOIN работает следующее правило: присоединяются только те строки таблиц, которые
#* удовлетворяют условию соединения. Если в любой из соединяемых таблиц находятся такие строки,
#* которые не удовлетворяют заявленному условию, — они отбрасываются.

SELECT*
FROM sql.matches m
JOIN sql.teams t ON t.api_id = m.away_team_api_id

#? LEFT OUTER JOIN И RIGHT OUTER JOIN

#* Для LEFT JOIN работает следующее правило: из левой (относительно оператора) таблицы сохраняются
#* все строки, а из правой добавляются только те, которые соответствуют условию соединения. Если в
#* правой таблице не находится соответствия, то значения строк второй таблицы будут иметь значение NULL.

SELECT
    t.long_name,
    m.id
FROM sql.teams t
LEFT JOIN sql.matches m ON t.api_id = m.home_team_api_id OR t.api_id = m.away_team_api_id
ORDER BY m.id DESC

#todo Вывод: в таблице teams сохранились все записи, а в таблице matches есть пустые строки.

#* Теперь, чтобы выбрать такие команды, которые не принимали участия в матчах, достаточно
#* добавить условие where m.id is null (или любое другое поле таблицы matches).

SELECT
    t.long_name
FROM 
    sql.teams t
LEFT JOIN sql.matches m ON t.api_id = m.home_team_api_id OR t.api_id = m.away_team_api_id
WHERE m.id IS NULL

#* Если мы добавим какой-либо фильтр по отличному от NULL значению для таблицы matches,
#* то LEFT JOIN превратится в INNER JOIN, поскольку для второй таблицы станет необходимым
#* присутствие такого (NOT NULL) значения в строке.


#todo Используя LEFT JOIN, выведите список уникальных названий команд, содержащихся в таблице matches.
#todo Отсортируйте список в алфавитном порядке.

SELECT
    distinct t.long_name
    
    FROM sql.matches m 
LEFT JOIN sql.teams t ON t.api_id = m.home_team_api_id OR t.api_id = m.away_team_api_id
order by t.long_name


#todo С LEFT JOIN также работают агрегатные функции, что позволяет не потерять значения из левой таблицы.
#todo Например, мы можем вывести сумму голов команд по гостевым матчам.

SELECT
    t.long_name,
    SUM(m.away_team_goals) total_goals
FROM   
    sql.teams t
LEFT JOIN sql.matches m ON t.api_id = m.away_team_api_id
GROUP BY t.id
ORDER BY 2 DESC

#todo При использовании RIGHT JOIN сохраняется та же логика, что и для LEFT JOIN, только
#todo за основу берётся правая таблица. Чтобы из LEFT JOIN получить RIGHT JOIN, нужно просто
#todo поменять порядок соединения таблиц.
#todo Вообще, применение RIGHT JOIN считается плохим тоном, так как язык SQL читается и пишется слева направо,
#todo а такой оператор усложняет чтение запросов.

#? FULL OUTER JOIN

#todo Оператор FULL OUTER JOIN объединяет в себе LEFT и RIGHT JOIN и позволяет сохранить кортежи обеих таблиц.
#todo Даже если не будет соответствий, мы сохраним все записи из обеих таблиц.FULL OUTER JOIN может быть
#todo полезен в ситуациях, когда схема данных недостаточно нормализована и не хватает таблиц-справочников.

SELECT 
…
FROM
	table1
FULL OUTER JOIN table2 ON условие

#? CROSS JOIN соединяет таблицы так, что каждая запись в первой таблице присоединяется к каждой записи
#? во второй таблице, иначе говоря, даёт декартово произведение.

#todo Одно и тоже
SELECT *                SELECT *
FROM                      FROM
    sql.teams,             sql.teams
    sql.matches             CROSS JOIN sql.matches
    
#todo Условие для CROSS JOIN, в отличие от других операторов, не требуется.

#todo Пример
#* Напишите запрос, который выведет все возможные уникальные комбинации коротких названий домашней команды
#* (home_team) и коротких названий гостевой команды (away_team). Команда не может сама с собой играть,
#* то есть быть и домашней, и одновременно гостевой (в одном и том же матче). Отсортируйте запрос по
#* первому и второму столбцам.

SELECT
     distinct 
     t.short_name  home_team,
    h.short_name  away_team
FROM   
    sql.teams t
    CROSS join sql.teams h 
WHERE t.id != h.id
ORDER BY 1, 2

#? NATURAL JOIN

#* Ключевое слово natural в начале оператора JOIN позволяет не указывать условие соединения таблиц — 
#* для соединения будут использованы столбцы с одинаковым названием из этих таблиц.

NATURAL JOIN можно использовать с любыми видами соединений, которые требуют условия соединения:

→ NATURAL INNER JOIN (возможна запись NATURAL JOIN);
→ NATURAL LEFT JOIN;
→ NATURAL RIGHT JOIN;
→ NATURAL FULL OUTER JOIN.

#todo запрос

SELECT 
…
FROM          table1 NATURAL JOIN table2

#todo  будет равнозначен запросу

SELECT
…
FROM          table1 t1
INNER JOIN table2 t2 ON t1.id = t2.id AND t1.name = t2.name

#todo Пример 
#* Выведите количество матчей между командами Real Madrid CF и FC Barcelona. В поле ниже введите
#* запрос, с помощью которого вы решили задание.

SELECT
count(m.id)

FROM   
    sql.matches m
    join sql.teams t on t.api_id = m.away_team_api_id
    join sql.teams k on k.api_id = m.home_team_api_id
where (t.long_name = 'Real Madrid CF' and k.long_name = 'FC Barcelona') 
or (t.long_name = 'FC Barcelona' and k.long_name = 'Real Madrid CF')
