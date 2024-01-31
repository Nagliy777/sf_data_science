
#! UNION

#? ПРИНЦИП И УСЛОВИЯ РАБОТЫ UNION

#todo Допустим, мы хотим собрать из справочников по книгам и фильмам один, так чтобы в нём
#todo содержались названия произведений, а также их описание — книга или фильм.

SELECT          book_name object_name, 'книга' object_description 
FROM          public.books
UNION ALL
SELECT          movie_title, 'фильм' 
FROM          sql.kinopoisk

#* В запросе мы использовали оператор UNION ALL — он присоединяет любой результат запроса к
#* другому «снизу» при условии, что у них одинаковая структура, а именно:
#* 1.одинаковый тип данных;
#* 2.одинаковое количество столбцов;
#* 3.одинаковый порядок столбцов согласно типу данных.

#? ВИДЫ UNION

#todo Оператор присоединения существует в двух вариантах:

#* UNION выводит только уникальные записи;
#* UNION ALL присоединяет все строки последующих таблиц к предыдущим, без ограничений по уникальности.

#todo Важно! UNION оставляет только уникальные значения, а потому требует дополнительных вычислительных
#todo мощностей и памяти (в данном случае можно провести аналогию с DISTINCT). Поэтому если вы уверены 
#todo в отсутствии дубликатов в данных или они вам не важны, предпочтительнее использовать UNION ALL.

#? СИНТАКСИС

#todo Запрос строится таким образом:

SELECT         n columns
FROM 
         table_1
UNION ALL
SELECT 
         n columns
FROM 
         table_2
...
UNION ALL
SELECT 
         n columns
FROM 
         table_n
         
#todo Результатом выполнения такого запроса будут строки table_1, table_2, ..., table_n, соединённые
#todo одни под другими и выведенные в единой выдаче.

#todo Важно! Названия итоговых колонок в выводе будут такие же, как в первом блоке SELECT, даже если
#todo они отличаются в других блоках подзапросов.

#todo Пример

#* Пришла пора испытать функцию UNION(ALL) на практике. Обратимся к нашему датасету о транспортной компании

#* и посмотрим, как сформировать справочник с ID всех таблиц и указанием объекта, к которому он относится.

SELECT
         c.city_id object_name, 'id города' object_type
FROM 
         sql.city c
UNION ALL
SELECT
         d.driver_id other_name, 'id водителя' other_type
FROM 
         sql.driver d
UNION ALL
SELECT
         s.ship_id, 'id доставки'
FROM 
         sql.shipment s
UNION ALL
SELECT
         c.cust_id, 'id клиента'
FROM 
         sql.customer c
UNION ALL
SELECT
         t.truck_id, 'id грузовика'
FROM 
         sql.truck t
ORDER BY 1

#todo Несмотря на исходные названия колонок other_name и other_type во втором подзапросе,
#todo в выводе мы получим названия, которые дали в первом блоке: object_name и object_type.

#todo Другая особенность — в применении сортировки ORDER BY: она всегда будет относиться к итоговому результату
#todo всего запроса с UNION ALL.

#todo В случаях, когда необходимо применить команду ORDER BY или LIMIT не к итоговому результату,
#todo а к каждой части запроса, можно обернуть подзапросы в скобки.

(SELECT book_name object_name, 'книга' object_descritption 
FROM public.books
ORDER BY 1
LIMIT 1)
UNION ALL
(SELECT movie_title, 'фильм' 
FROM sql.kinopoisk
ORDER BY 1
LIMIT 1)

#todo Пример
#* Напишите запрос, который создает уникальный алфавитный справочник всех городов, штатов, имён водителей
#* и производителей грузовиков. Результатом запроса должны быть два столбца: название и тип объекта
#* (city, state, driver, truck). Отсортируйте список по названию объекта, а затем — по типу.

SELECT c.city_name "название", 'city' "тип объекта"
FROM sql.city c

UNION 

SELECT c.state,  'state' 
FROM sql.city c

UNION 

SELECT d.first_name,  'driver' 
FROM sql.driver d

UNION 

SELECT t.make,  'truck' 
FROM sql.truck t
order by "название", "тип объекта"

#? UNION и ограничение типов данных

#todo UNION может быть использован только в случае полного соответствия столбцов и их
#todo типов в объединяемых запросах.

#* Если мы всё же хотим выполнить поставленную задачу, придётся привести оба столбца к одному типу
#* данных. Не каждый текст может быть приведён к числу, зато каждое число может быть представлено
#* в текстовом формате.

#todo Для типизации в Postgres составляется запрос по модели column_name::column_type.
#todo Таким образом, чтобы перевести city_id в текст, нам потребуется написать city_id::text.

SELECT 
         c.city_id::text
FROM
         sql.city c
UNION ALL
SELECT 
         cc.city_name
FROM
         sql.city cc
         
#todo Пример    
#* Напишите запрос, который объединит в себе все почтовые индексы водителей и их телефоны в единый
#* столбец-справочник contact. Также добавьте столбец с именем водителя first_name и столбец
#* contact_type с типом контакта (phone или zip в зависимости от типа). Отсортируйте список по
#* столбцу с контактными данными в порядке возрастания, а затем — по имени водителя.   
         
SELECT d.phone contact, first_name first_name, 'phone'contact_type
FROM sql.driver d
UNION 
SELECT d.zip_code::text, first_name , 'zip'
FROM sql.driver d
order by contact, first_name

#? ВОЗМОЖНОСТИ UNION

#* Помимо соединения разнородных сущностей в единый справочник, UNION ALL часто используется для
#* подведения промежуточных итогов и выведения результатов агрегатных функций.

#todo Пример
#* Напишите запрос, который выводит общее число доставок total_shipments, а также количество
#* доставок в каждый день. Необходимые столбцы: date_period, cnt_shipment. Не забывайте о единой
#* типизации. Упорядочите по убыванию столбца date_period.
SELECT
         s.ship_date::text date_period,
         count(s.ship_id) cnt_shipment 
FROM
         sql.shipment s
group by s.ship_date
UNION all
SELECT
         'total_shipments',
         count(s.ship_id)
FROM
         sql.shipment s
ORDER BY date_period DESC

#? UNION и дополнительные условия

#* UNION также может быть использован для разделения существующей выборки по критерию
#* «выполнение определённого условия».

#todo Например, с помощью UNION можно отобразить, у кого из водителей заполнен столбец с номером телефона.

SELECT
         d.first_name,
         d.last_name,
         'телефон заполнен' phone_info
FROM
         sql.driver d
WHERE d.phone IS NOT NULL

UNION

SELECT
         d.first_name,
         d.last_name,
         'телефон не заполнен' phone_info
FROM
         sql.driver d
WHERE d.phone IS NULL

#todo  Пример
#* Напишите запрос, который выведет все города и штаты, в которых они расположены, а также информацию о том,
#* была ли осуществлена доставка в этот город:
#* если в город была осуществлена доставка, то выводим 'доставка осуществлялась';
#* если нет — выводим 'доставка не осуществлялась'.
#* Столбцы к выводу: city_name, state, shipping_status. Отсортируйте в алфавитном порядке по
#* городу, а затем — по штату.


SELECT 
     c.city_name AS city_name,
     c.state AS state,
    'доставка осуществлялась' AS shipping_status
FROM 
    sql.city c
    LEFT JOIN sql.shipment s ON c.city_id=s.city_id
WHERE s.city_id IS NOT NULL
UNION
SELECT 
     c.city_name AS city_name,
     c.state AS state,
    'доставка не осуществлялась' AS shipping_status
FROM 
    sql.city c
    LEFT JOIN sql.shipment s ON c.city_id=s.city_id 
WHERE s.city_id IS NULL
ORDER BY 1, 2

#? UNION и ручная генерация

#* UNION можно использовать для создания справочников прямо в коде запроса. К примеру, если мы хотим
#* вручную ввести какие-то значения и произвести с ними некоторые манипуляции или дополнить
#* существующую выдачу своими значениями.

#todo Составим запрос, который позволит вывести первые три буквы алфавита и их порядковые номера.

SELECT 
         'a' letter,'1' ordinal_position
UNION 
SELECT 
         'b','2'
UNION 
SELECT
         'c','3'


#todo Напишите запрос, который выберет наибольшее из значений:1000000, 541, -500, 100
SELECT
    1000000 as result
union
SELECT
    541 as result
union

SELECT
    -500 as result
union

SELECT
    100 as result
    
order by result desc
limit 1

#? ИСКЛЮЧАЕМ ПОВТОРЯЮЩИЕСЯ ДАННЫЕ. EXCEPT

#todo Предположим, нам нужно узнать, в какие города осуществлялась доставка, за исключением тех,
#todo в которых проживают водители.

SELECT
         c.city_name
FROM
         sql.shipment s
JOIN sql.city c ON s.city_id = c.city_id
EXCEPT
SELECT
         cc.city_name
FROM
         sql.driver d 
JOIN sql.city cc ON d.city_id=cc.city_id
ORDER BY 1

#* Все водители проживают в городе Memphis, и мы видим, что он не выводится в результате запроса.
#* Как вы, должно быть, заметили, для решения этой задачи мы использовали оператор EXCEPT.

#* Синтаксис выглядит следующим образом:

SELECT 
         n columns
FROM 
         table_1
EXCEPT
SELECT 
         n columns
FROM 
         table_2
         

#todo Пример
#* Выведите список zip-кодов, которые есть в таблице sql.driver, но отсутствуют в таблице sql.customer.
#* Отсортируйте по возрастанию, столбец к выводу — zip. В поле ниже введите запрос, с помощью которого
#* вы решили эту задачу.
SELECT
         d.zip_code
FROM
         sql.driver d
EXCEPT
SELECT
         c.zip
FROM
         sql.driver d
JOIN sql.customer c ON d.zip_code=c.zip

#? ВЫБИРАЕМ ОБЩИЕ ДАННЫЕ. INTERSECT

#todo Предположим, нам надо вывести совпадающие по названию города и штаты.
SELECT          c.city_name object_name
FROM          sql.city c
INTERSECT
SELECT 
         cc.state
FROM          sql.city cc
ORDER BY 


#todo Пример
#* Напишите запрос, который выведет список id городов, в которых есть и клиенты, и доставки, и водители.
SELECT          c.city_id 
FROM          sql.city c

INTERSECT
SELECT 
         s.city_id           
FROM         sql.city as c 
            join sql.shipment  AS s  ON s.city_id = c.city_id 

INTERSECT
SELECT 
         cus.city_id                 
FROM         sql.city as c 
            join sql.customer AS cus  ON cus.city_id = c.city_id            

INTERSECT
SELECT 
         d.city_id                  
FROM         sql.city as c 
            join sql.driver AS d  ON d.city_id = c.city_id  
            
#todo Структура
SELECT          N columns
FROM          table_1
UNION / UNION ALL / EXCEPT / INTERSECT 
SELECT          N columns
FROM          table_2