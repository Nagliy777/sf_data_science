
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