
#* Из предыдущих модулей вы узнали, как получать данные, когда они хранятся в файлах разных форматов.
#* В реальных проектах данные, как правило, не содержатся в готовом виде в каком-то файле — для анализа
#* необходимо предварительно их собрать, например скопировав с какого-нибудь стороннего веб-сайта.

#! Веб-запросы

#* Процесс получения/извлечения информации с веб-ресурсов в интернете называется web-scraping
#* (рус. веб-скрейпинг/веб-скрапинг). Веб-скрапинг может быть проделан вручную пользователем компьютера,
#* однако этот термин обычно связывают с автоматизированными процессами, реализованными с помощью кода.

#todo Какие данные можно извлечь в процессе веб-скрапинга?

#* цены на товары конкурентов для оптимизации своей стратегии ценообразования;
#* сообщения в социальных медиа, по которым можно отслеживать тренды в той или иной области;
#* отзывы о товарах/услугах компании на различных площадках, которые можно впоследствии анализировать;
#* контактные данные пользователей соцсетей или форумов для дальнейшего взаимодействия с этими пользователями;и т.д.

#* Интернет — это глобальная информационная сеть, которая позволяет компьютерам по всему миру
#* обмениваться информацией. Один компьютер (называемый клиентом) отправляет запрос в определённом
#* формате другому компьютеру (называемому сервером) и получает ответ (текст, изображение, видео и т. д.).

#* Клиент и сервер взаимодействуют между собой, обмениваясь одиночными сообщениями (не потоком данных)
#* посредством сетевых протоколов, которые формализуют общение между ними.

#todo Запрос, отправляемый клиентом с использованием протокола HTTP, состоит из нескольких элементов:

#* адрес, по которому идёт обращение (например, www.google.com);
#* техническая информация, например метод запроса;
#* дополнительные данные, например если загружается (передаётся) изображение

#todo Ответ, в свою очередь, состоит из следующих элементов:

#* код статуса ответа: например, 200 («успешно»), 404 («не найден») и т. д. (более полный список кодов статуса ответа можете посмотреть, перейдя по ссылке);
#* текст в запрошенном формате (HTML, XML, JSON и т. д.) или мультимедийные файлы;
#* прочая техническая информация.

#? МЕТОДЫ ЗАПРОСОВ В ПРОТОКОЛЕ HTTP

#* Для того чтобы указать серверу на то, какое действие мы хотим произвести с ресурсом, в протоколе HTTP используются так называемые методы. В HTTP существует несколько методов, которые описывают действия с ресурсами. Чаще всего используются GET и POST.

#todo GET — ПОЛУЧЕНИЕ РЕСУРСА

#* Метод GET запрашивает информацию из указанного источника и не может влиять на его содержимое. Запрос доступен для кэширования данных (то есть для сохранения, восстановления и дальнейшего использования) и добавления в закладки. Длина запроса ограничена (максимальная длина — 2048 символов).

#* Пример GET-запроса, отправляемого через адресную строку браузера:

#*  http://site.ru/page.php?name=dima&age=27

#todo POST — СОЗДАНИЕ РЕСУРСА

#* Метод POST используется для отправки данных, которые могут оказывать влияние на содержимое ресурса.
#* В отличие от метода GET, запросы POST не могут быть кэшированы, они не остаются в истории браузера
#* и их нельзя добавить в закладки. Длина запроса POST не ограничивается.

#* Пример POST-запроса, отправляемого через форму запроса:

"""POST / HTTP/1.0\r\n
Host: www.site.ru\r\n
Referer: http://www.site.ru/index.html\r\n
Cookie: income=1\r\n
Content-Type: application/x-www-form-urlencoded\r\n
Content-Length: 35\r\n
\r\n
login=Dima&password=12345"""

#! Библиотека requests

#todo В стандартной библиотеке Python для отправки веб-запросов существует функция urllib2, но большинство
#todo разработчиков используют стороннюю библиотеку requests (c англ. запросы), потому что её работа более
#todo стабильна, а созданный с её помощью код получается проще. Поэтому мы будем работать с библиотекой
#todo requests, а urllib2 рассматривать не будем.

#* Познакомимся с библиотекой requests, решив простую задачу — получить значения курсов валют.
#* Курс валют — полезная и регулярно обновляемая информация, но каждый раз в ручном режиме
#* получать информацию о курсе интересующей валюты трудоёмко.

#todo Разработаем код, так называемый скрипт (англ. script, рус. сценарий), — небольшую программу,
#todo которая содержит последовательность действий для автоматического выполнения задачи.

# Устанавливаем библиотеку requests
!pip install requests 


#* Как только библиотека установлена, импортируем её и отправим наш первый запрос к ресурсу Курсы
#* валют ЦБ РФ в XML и JSON. Используем метод get() из библиотеки requests,
#* передав ему соответствующий URL —  https://www.cbr-xml-daily.ru/daily_json.js:
    
import requests # Импортируем библиотеку requests
url = 'https://www.cbr-xml-daily.ru/daily_json.js' # Определяем значение URL страницы для запроса
response = requests.get(url) # Делаем GET-запрос к ресурсу и результат ответа сохраняем в переменной response
print(response) # Выводим значение response на экран как объект
# <Response [200]>

#* По умолчанию в квадратных скобках на экран выводится код статуса ответа. В данном случае он равен
#* 200 — то есть запрос был корректным и сервер отдал нам нужную информацию. Значение кода статуса
#* 404 означало бы, что страница по указанному адресу не найдена, а значение 403 — что синтаксис
#* GET-запроса неверный.

#todo Код ответа в виде числовой переменной можно получить с помощью метода status_code:
print(response.status_code) # Выводим числовое значение response на экран

#? РАБОТАЕМ С ОТВЕТОМ

#* Текст ответа хранится в атрибуте text. Выведем значение атрибута на экран и посмотрим на его содержимое:

print(response.text) # Выводим содержимое атрибута text переменной response на экран

#* По нашему запросу ресурс возвращает информацию в JSON-формате, однако в настоящий момент результат
#* хранится как единая строка. Проверить тип данных полученного ответа можно, воспользовавшись
#* функцией type().

#* Для того чтобы удобно было работать с полученной информацией, нам необходимо преобразовать строку
#* в словарь. В объект ответа Response  из библиотеки requests уже встроен метод json() .
#* Импортируем функцию pprint(), применим к полученному ответу метод json() и выведем
#* полученный результат на экран:

from pprint import pprint # Импортируем функцию pprint()
import json # Импортируем модуль json
currencies = response.json() # Применяем метод json()
pprint(currencies) # Выводим результат на экран

#* Теперь данные находятся в словаре и можно легко получать необходимые значения.

#* Например, по ключу Valute мы можем обратиться к вложенному словарю, который содержит информацию
#* о мировых валютах. Выведем на экран, например, информацию о евро (EUR):

pprint(currencies['Valute']['EUR']) # Выводим на экран информацию о валюте евро
print(currencies['Valute']['CZK']['Name']) # Чешских крон

#! Парсинг сайтов

#* Для примера рассмотрим страницу, содержащую статью с информацией о присуждении Нобелевской премии
#* по экономике в 2021 году, и попробуем извлечь из неё заголовок статьи, опубликованной на странице,
#* дату публикации, а также текст статьи.

#? ОСНОВЫ HTML

#* HTML (англ. HyperText Markup Language, рус. язык гипертекстовой разметки) 
#* — стандартизированный язык разметки документов в интернете. Большинство
#* веб-страниц содержат описание разметки на языке HTML. Язык HTML интерпретируется браузерами.
#* Полученный в результате интерпретации текст отображается на экране монитора компьютера
#* или мобильного устройства.

#* У корректной HTML-страницы есть заголовок и тело страницы. В заголовке (в тегах <head> … </head>)
#* размещается техническая информация, подключаются скрипты и стили. В теле <body> … </body> находятся
#* текст и данные, которые непосредственно отображаются на странице в браузере.

#todo Разметка небольшой страницы выглядит примерно так:

<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Название страницы</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1> Это заголовок страницы </h1>
        <p> Какой-то текст </p>
    </body>
</html>

#* Изучение языка HTML находится вне рамок этого курса, но для того, чтобы собирать информацию с
#*  веб-страниц, нет необходимости хорошо знать HTML. Достаточно понимать, что:

#* существуют теги с разными именами;
#* у тегов бывают атрибуты, такие как class и id;
#* теги образуют иерархическую структуру, то есть одни теги вложены в другие.

#? ПОЛУЧАЕМ СОДЕРЖИМОЕ ВЕБ-СТРАНИЦЫ

#* Для этого отправим GET-запрос с помощью библиотеки requests и метода get() и посмотрим на
#*  текст ответа на наш запрос (как мы помним, он содержится в атрибуте text):

import requests # Импортируем библиотеку requests
url = 'https://nplus1.ru/news/2021/10/11/econobel2021' # Определяем адрес страницы
response = requests.get(url)  # Выполняем GET-запрос
print(response.text)  # Выводим содержимое атрибута text

#* Ответ содержит HTML-код страницы, к которой мы обратились.

#todo В отличие от предыдущего примера, где ответ возвращался в JSON-формате, мы не
#todo можем так просто преобразовать HTML-код в словарь и извлечь необходимую нам информацию.

#! Библиотека BeautifulSoup

#* Для поиска необходимых нам данных мы будем использовать библиотеку BeautifulSoup, которая
#* позволяет по названию тегов и их атрибутов получать содержащийся в них текст.

#* BeautifulSoup не является частью стандартной библиотеки, поэтому для начала её нужно установить.
#* Например, в Jupyter Notebook это делается с помощью такой команды:
# Устанавливаем библиотеку BeautifulSoup
!pip install beautifulsoup4 

#* После установки импортируем библиотеку в наш код:
from bs4 import BeautifulSoup # Импортируем библиотеку BeautifulSoup

#* Теперь мы можем извлекать данные из любой веб-страницы.

#* Создадим объект BeautifulSoup с именем page, указывая в качестве параметра html.parser.

import requests # Импортируем библиотеку requests
from bs4 import BeautifulSoup # Импортируем библиотеку BeautifulSoup
url = 'https://nplus1.ru/news/2021/10/11/econobel2021' # Определяем адрес страницы
response = requests.get(url) # Выполняем GET-запрос, содержимое ответа присваивается переменной response
page = BeautifulSoup(response.text, 'html.parser') # Создаём объект BeautifulSoup, указывая html-парсер
print(page.title) # Получаем тег title, отображающийся на вкладке браузера
print(page.title.text) # Выводим текст из полученного тега, который содержится в атрибуте text

#todo Если при запросе к сайту, а затем при его разборе с помощью BeautifulSoup в тексте страницы не
#todo находится нужный тег, попробуйте вывести на печать пару тысяч символов текста страницы. Если
#todo там обнаружится нечто похожее на капчу, возможно, сайт посчитал вас роботом и отказывается
#todo выдавать содержимое. Чтобы получить его, попробуйте «притвориться» браузером при запросе из скрипта:
requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#* User-Agent своего браузера можно узнать по этой ссылке.

#? ИЗВЛЕКАЕМ ЗАГОЛОВОК И ВРЕМЯ НАПИСАНИЯ СТАТЬИ

#* Предположим, что мы знаем, что в HTML-коде рассматриваемой нами страницы заголовок статьи
#* заключён в тег <h1> … </h1> (заголовок первого уровня).
#* Тогда мы можем получить его текст с помощью метода find() (с англ. найти) объекта BeautifulSoup,
#* передав ему название интересующего нас тега:

# Применяем метод find() к объекту и выводим результат на экран
print(page.find('h1').text) 

#todo Но как же узнать, в каких именно тегах заключена необходимая информация?
#* Устанавливаем курсор на элементе страницы (заголовок статьи), информацию о котором хотим получить,
#* нажимаем на правую клавишу мыши и в выпадающем списке выбираем пункт «Просмотреть код элемента» или
#* «Посмотреть код» в зависимости от браузера.
#* В открывшемся окне инструмента разработчика видим, что информация о заголовке статьи заключена
#* в теге <h1> … </h1>.

#todo Напишите функцию wiki_header, которая по адресу страницы возвращает заголовок первого уровня для
#todo статей на Wikipedia.

import requests # Импортируем библиотеку requests
from bs4 import BeautifulSoup # Импортируем библиотеку BeautifulSoup

def wiki_header(url):
    response = requests.get(url) # Выполняем GET-запрос, содержимое ответа присваивается переменной response
    page = BeautifulSoup(response.text, 'html.parser') 
    return page.find('h1').text

#? НЕУНИКАЛЬНЫЕ ТЕГИ: ИЗВЛЕКАЕМ ТЕКСТ И ДАТУ ПУБЛИКАЦИИ СТАТЬИ

#* Теперь получим сам текст статьи. Как вы уже знаете, первым делом необходимо определить, в
#* какой тег он заключён. Применим, как и ранее, инструмент разработчика.

#* Видим, что искомый текст заключён в тег  <div> … </div> . Попробуем извлечь его уже известным
#*  нам способом — с помощью метода find() — и выведем его на экран.

print(page.find('div').text) # Выводим содержимое атрибута text тега div
#* Мы увидели не то, что ожидали — кучу текста, не имеющего отношения к тому, что мы искали...

#* В чём же проблема?
#* Дело в том, что теги <div> … </div> очень распространённые и на странице их очень много.
#* Метод find() нашёл первый из них, но это не то, что нам надо.

#* Посмотрим на нашу страницу, используя инструмент разработчика, ещё раз.
#* Можем заметить, что у искомого текста есть свой класс — n1_material text-18 :
#todo Передадим название класса в метод find() с помощью аргумента class_ и получим текст статьи:
print(page.find('div', class_='n1_material text-18').text) # Выводим содержимое атрибута text тега div класса n1_material text-18

#* В данном случае происходит поиск точного строкового значения class атрибута, т. е.
#* выполнение строк кода:

print(page.find('div', class_='n1_material').text)
print(page.find('div', class_='n1_material text-18').text)

#* даст одинаковый результат.

#* При выполнении строки кода
print(page.find('div', class_='text-18 n1_material').text)
#*мы получим ошибку, так как такого строкового значения в области поиска нет.

#* Аналогично получим информации о теге, который содержит дату написания статьи, отображаемую
#* в левом верхнем углу страницы.

#* Итак, нам нужен тег <a> … </a> с классом "relative before:block before:w-px before:bg-current
#* before:h-4 before:absolute before:left-0 group pl-2 flex inline-flex items-center".
#* Для поиска достаточно указать в качестве класса "relative", отбросив дополнительные настройки.

#* Теперь получим данные из него с помощью уже известного метода find(), передав название нужного тега:
# Выводим на экран содержимое атрибута text тега a с классом "relative"
print(page.find('a', class_= "relative").text)

#* Задача решена — мы извлекли из контента страницы заголовок статьи, опубликованной на странице,
#* дату публикации, а также текст статьи.

#? СБОР НЕСКОЛЬКИХ ЭЛЕМЕНТОВ: СОБИРАЕМ ВСЕ ССЫЛКИ НА СТРАНИЦЕ

#* Рассмотрим ещё один сценарий: вы хотите собрать сразу несколько элементов со страницы.
#* Например, представьте, что вы хотите получить названия всех языков программирования,
#* упомянутых на странице в Wikipedia в статье про языки программирования.

#* Если требуется получить больше элементов, необходимо воспользоваться методом find_all()
#* (с англ. найти все):
url = 'https://en.wikipedia.org/wiki/List_of_programming_languages' # Задаём адрес ресурса
response = requests.get(url) # Делаем GET-запрос к ресурсу
page = BeautifulSoup(response.text, 'html.parser') # Создаём объект BeautifulSoup
links = page.find_all('a') # Ищем все ссылки на странице и сохраняем в переменной links в виде списка
print(len(links)) # Выводим количество найденных ссылок

#* Итак, на момент создания этих учебных материалов на странице содержалось 928 ссылок.
#* Посмотрим на некоторые из них:
print([link.text for link in links[500:510]]) # Выводим ссылки с 500 по 509 включительно
#* Не все ссылки соответствуют названиям языков программирования — страница содержит
#* также «служебные» ссылки, 

#* Для обработки полученных данных и исключения «лишней» информации можно, например,
#* использовать подходы, которые вы изучили в модуле PYTHON-14.

#! Работа с API

#* Вы могли убедиться, что поиск необходимой информации с выделением правильных тегов — довольно
#* трудоёмкая задача. Кроме того, подобные программы могут ломаться в случаях, когда меняется дизайн
#* сайта, его разметка или владельцы сайтов защищаются от ботов капчей

#* К счастью, многие крупные сайты предоставляют доступ к так называемым API
#todo API — это специальные разделы сайта, где информацию можно получать без разметки, а формат запросов
#todo и ответов зафиксирован. API созданы для того, чтобы облегчить взаимодействие с сайтом для сторонних
#todo разработчиков.

#? КЛЮЧ АВТОРИЗАЦИИ

#* Для того чтобы начать работать с API, обычно необходимо получить сервисный ключ авторизации — токен.

#* Токен — это средство идентификации пользователя или отдельного сеанса работы в компьютерных
#* сетях и приложениях. Различают программные и аппаратные токены.
#* Мы будем использовать программный токен, который обычно представляет собой зашифрованную 
#* последовательность символов, позволяющую точно идентифицировать объект и определить уровень
#* его привилегий. Он генерируется системой авторизации и привязывается к конкретному сеансу работы,
#* клиенту сети или пакету данных.

#* Зайдите на страницу, чтобы создать приложение (вы должны быть авторизованы ВКонтакте).
#* Дайте приложению любое название и в разделе Платформа поставьте отметку выбора напротив
#* значения Standalone-приложение:

#? ПЕРВЫЕ ЗАПРОСЫ К API

#todo Сделаем наш первый запрос из браузера.

#* Перейдите по следующей ниже ссылке в браузере, подставив вместо слова TOKEN
#* ваш персональный сервисный ключ доступа (токен), полученный на предыдущем шаге:
#* https://api.vk.com/method/users.get?user_id=1&v=5.95&access_token=TOKEN
# {"response":[{"id":1,"first_name":"Павел","last_name":"Дуров","can_access_closed":true,"is_closed":false}]}

#* Итак, мы сделали GET-запрос к API ВКонтакте, который состоит из следующих элементов:

#* https://api.vk.com/method — домен и URL запроса API; обычно не меняется;
#* users.get — название метода, который отдаёт определённый отчёт, в нашем
#* случае это метод для получения информации о пользователе;

#* user_id и v — параметры запроса: идентификатор пользователя, о котором
#* хотим получить информацию (в нашем примере мы запрашиваем информацию о первом пользователе),
#* и номер версии API;

#* token — токен, который выдаётся только пользователям, имеющим право
#* просматривать определённые данные, например показания счётчиков Яндекс.Метрики
#* вашего проекта; на все остальные запросы без корректного токена система отвечает отказом.

#* Если мы обратимся к документации метода users.get, то увидим, что в ней описано множество других
#* параметров, которые можно получить о пользователе (дата рождения, пол, родной город и другие)
#* — словом, всё то, что мы видим на странице пользователя в интерфейсе или приложении ВКонтакте
#* (конечно, если пользователь их указал).

#todo Добавим к запросу дату рождения и пол (согласно документации, эти параметры надо перечислять в поле fields):
https://api.vk.com/method/users.get?user_id=1&v=5.95&fields=sex,bdate&access_token=TOKEN
#* {"response":[{"id":1,"bdate":"10.10.1984","sex":2,"first_name":"Павел",
#* "last_name":"Дуров","can_access_closed":true,"is_closed":false}]}

#? ЗАПРОС К API ИЗ КОДА

#* Продолжаем пользоваться всё той же библиотекой requests.

import requests # Импортируем модуль requests
token = ' ... ' # Указываем свой сервисный токен
url = 'https://api.vk.com/method/users.get' # Указываем адрес страницы к которой делаем запрос
params = {'user_id': 1, 'v': 5.95, 'fields': 'sex,bdate', 'access_token': token, 'lang': 'ru'} # Перечисляем параметры нашего запроса в словаре params
response = requests.get(url, params=params) # Отправляем запрос
print(response.text) # Выводим текст ответа на экран

#* Мы получили строку в JSON-формате, которую можно преобразовать в словарь с помощью метода json(),
#* после чего можно с лёгкостью обращаться к различным полям.

#* Словари нагляднее выводить с помощью функции pprint(), которую мы уже использовали ранее:
from pprint import pprint # Импортируем функцию pprint()
pprint(response.json()) # Выводим содержимое словаря, содержащего ответ, на экран

#* Как вы видите, по ключу response мы можем получить список, в котором хранятся словари, содержащие
#* информацию о запрошенных нами пользователях. Мы запросили информацию лишь об одном из них, поэтому
#* список содержит только один элемент. Извлечём его:

user = response.json()['response'][0] # Извлекаем из словаря по ключу response информацию о первом пользователе
print(user['bdate']) # Выводим дату рождения первого пользователя на экран
# 10.10.1984

#* Метод users.get() позволяет запрашивать информацию о множестве (до 1 000) пользователей одновременно.
#* Для этого нужно использовать параметр user_ids и передавать id через запятую в строковом формате.
#* Например, чтобы получить информацию о пользователях с id=1, id=2, id=3, необходимо передать значение
#* параметра user_ids='1,2,3'.

ids = ",".join(map(str, range(1, 4))) # Формируем строку, содержащую информацию о поле id первых трёх пользователей
params = {'user_ids': ids, 'v': 5.95, 'fields': 'bdate', 'access_token': token, 'lang': 'ru'} # Формируем строку параметров
pprint(requests.get(url, params=params).json()) # Посылаем запрос, полученный ответ в формате JSON-строки преобразуем в словарь и выводим на экран его содержимое, используя функцию pprint()

#? СБОР ИНФОРМАЦИИ ИЗ ГРУПП

#* В одном из предыдущих юнитов в качестве примера мы собрали информацию о небольшом количестве пользователей.
#* Теперь перейдём к более реальной задаче — сбору данных о пользователях группы ВКонтакте.

#todoСтоит отметить, что есть много сервисов, которые выгружают похожую статистику из соцсетей.
#todo Однако им свойственны недостатки универсальных решений:

#todo 1.не учитываются все особенности вашего проекта;
#todo 2.используется фиксированный набор метрик, дополнительную обработку данных приходится делать вам;
#todo 3.не всегда бесплатны и вряд ли позволят работать с большими объёмами данных.

#* Теперь мы научимся считать произвольные метрики групп, собирая данные из API и работая
#* с двумя ограничениями, которые свойственны практически всем системам:

#* 1.ограничение на количество вызовов в единицу времени;
#* 2.ограничение на количество выгружаемых строк за один запрос.

#* Давайте рассмотрим, как работать с этими ограничениями на примере выгрузки списка пользователей группы
#* https://vk.com/vk социальной сети ВКонтакте.

#* Обратимся к документации, чтобы узнать, какие методы нам доступны для групп, — для
#* получения списка пользователей группы доступен метод groups.getMembers.

#* Согласно документации, обязательным параметром данного метода является group_id
#* — идентификатор, или короткое имя, группы. В нашем случае это vk: https://vk.com/vk.
#* Протестируем, как работает метод в самом простом случае, — получим id участников группы:

import requests # Импортируем модуль requests
token = ' ... ' # Указываем свой сервисный токен
url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес обращения
params = {'group_id': 'vk', 'v': 5.95, 'access_token': token} # Формируем строку параметров
response = requests.get(url, params = params) # Посылаем запрос
data = response.json() # Ответ сохраняем в переменной data в формате словаря
print(data) # Выводим содержимое переменной data на экран (отображён фрагмент)
#{'response': {'count': 13428145, 'items': [6, 19, 47, 54,

#* По ключу count мы можем получить общее число участников группы,
#* а список по ключу items хранит их id. Посмотрим на него поближе:

print(len(data['response']['items'])) # Выводим на экран количество элементов словаря
# 1000

#* Мы видим, что всего пользователей в группе больше 11 миллионов, а получили мы только первую тысячу
#* пользователей группы. По информации, указанной в документации о параметре count, это максимум,
#* который может отдать API за один раз.

#* Для получения следующей тысячи пользователей можно воспользоваться параметром offset (с англ. смещение),
#* который передвинет начало отсчёта. Для выгрузки всех пользователей группы будем в цикле выгружать по
#* 1000 пользователей (count будет всегда равен 1000), увеличивая смещение offset на величину count.

#* Для тренировки напишем цикл выгрузки первых 20 пользователей со значением count=5. Иными словами, мы
#* будем выгружать по пять пользователей за запрос до тех пор, пока не получим информацию о 20 пользователях.

#* Давайте выведем на экран первые 20 пользователей из нашей первой попытки получить информацию о 1000
#* пользователей, чтобы мы могли сверить результат выгрузки из 20 пользователей:
users_for_checking = data['response']['items'][:20] # Загружаем в переменную информацию об id первых 20 пользователей в виде списка
print(users_for_checking) # Выводим перечень id первых 20 пользователей
#[6, 19, 47, 54, 79, 177, 198, 212, 219, 239, 243, 345, 407, 421, 431, 450, 467, 485, 510, 550]

#* Теперь используем count и offset, чтобы получить те же id по пять за раз:
import requests # Импортируем модуль requests
token = ' ... ' # Указываем свой сервисный токен
url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес обращения
count = 5 
offset = 0 
user_ids = [] 
max_count = 20 
while offset < max_count: 
    # Будем выгружать по count=5 пользователей, 
    # начиная с того места, где закончили на предыдущей итерации (offset) 
    print('Выгружаю {} пользователей с offset = {}'.format(count, offset))   
    params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token} 
    response = requests.get(url, params = params) 
    data = response.json() 
    user_ids += data['response']['items'] 
    # Увеличиваем смещение на количество строк, которое мы уже выгрузили 
    offset += count 
print(user_ids) 

#* Выгружаю 5 пользователей с offset = 0
#* Выгружаю 5 пользователей с offset = 5
#* Выгружаю 5 пользователей с offset = 10
#* Выгружаю 5 пользователей с offset = 15
#* [6, 19, 47, 54, 79, 177, 198, 212, 219, 239, 243, 345, 407, 421, 431, 450, 467, 485, 510, 550]

#todo Сравним списки, полученные двумя способами:

print(user_ids == users_for_checking) 
#* Так как результат сравнения — True, списки идентичны. Значит, второй способ работает корректно. 
#* Теперь мы можем получить данные обо всех пользователях, выставив count = 1000 и
#* max_count = data['response']['count'].

#? ОГРАНИЧЕНИЕ ПО ЧАСТОТЕ ЗАПРОСОВ

#* В API часто добавляют ограничение по частоте запросов, чтобы отдельно взятые пользователи
#* слишком сильно не перегружали сервер. Подобное ограничение есть и у ВКонтакте — в документации
#* указано, что можно делать не более трёх запросов в секунду.

#todo Чтобы не следить за частотой отправки запросов с секундомером в руках, мы можем после каждого запроса
#todo делать паузу. В этом случае, даже если код будет выполняться на самом быстром компьютере, мы не нарушим
#todo установленное ограничение, так как периодичность отправки запросов будет искусственно замедлена.

#todo Воспользуемся библиотекой time и методом sleep, с помощью которого мы можем добавить паузу, например
#todo в 0.5 секунд, после каждого запроса:

import requests # Импортируем модуль requests
import time # Импортируем модуль time
token = ' ... ' # Указываем свой сервисный токен
url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес страницы, к которой делаем запрос
count = 1000 
offset = 0  
user_ids = []  
while offset < 5000: 
    params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token} 
    response = requests.get(url, params = params) 
    data = response.json() 
    user_ids += data['response']['items'] 
    offset += count 
    print('Ожидаю 0.5 секунды...') 
    time.sleep(0.5) 
print('Цикл завершен, offset =',offset) 

#* Ожидаю 0.5 секунды...
#* Ожидаю 0.5 секунды...
#* Ожидаю 0.5 секунды...
#* Ожидаю 0.5 секунды...
#* Ожидаю 0.5 секунды...
#* Цикл завершен, offset = 5000

#? ЛАЙКИ, РЕПОСТЫ И КОММЕНТАРИИ

#* Через API новостной ленты ВКонтакте мы можем получить информацию о взаимодействии с сообщениями в ленте.

#* Для примера продолжим работать с группой https://vk.com/vk и рассмотрим последние 100
#* сообщений в новостной ленте.

#* Примечание: обратите внимание, что т.к. сообщения в новостной ленте непрерывно обновляются,
#* то ваш результат выполнения кода ниже будет отличаться от нашего варианта.

#* Для получения информации о сообщениях на стене в API ВКонтакте предусмотрен метод wall.get. Применим его:

import requests # Импортируем модуль requests
from pprint import pprint # Импортируем функцию pprint()
token = ' ... ' # Указываем свой сервисный токен
url = 'https://api.vk.com/method/wall.get' # Указываем адрес страницы, к которой делаем запрос
params = {'domain': 'vk', 'filter': 'owner', 'count': 1000, 'offset': 0, 'access_token': token, 'v': 5.95} 
response = requests.get(url, params = params) 
pprint(response.json()) 

#* Посмотрим на количество результатов:

len(response.json()['response']['items'])
## 100
#* Посмотрим на информацию об отдельном сообщении:

response.json()['response']['items'][0] 

#* В полях comments, likes и reposts содержится статистика по взаимодействию с сообщением пользователей
#* (на момент получения информации) — число комментариев, лайков и репостов.

#* Давайте соберём итоговую статистику для последних десяти непустых сообщений в словарь stats.
#* В качестве ключа будем использовать начало сообщения (если начало сообщения пустое, то информацию
#* о таком сообщении проигнорируем), в качестве значения — список с тремя интересующими нас
#* метриками и временем публикации (комментарии, лайки, репосты, дата публикации):

stats = {} 
count_post = 0 # Счётчик «непустых» сообщений
for record in response.json()['response']['items'][:]:
    title = record['text'][:30] 
    if title: 
        stats[title] = [record['comments']['count'], record['likes']['count'], record['reposts']['count'], record['date']] 
        count_post += 1 
    if count_post < 10: 
        continue 
    else: 
        break 
pprint(stats)

#todo Мы рассмотрели базовое взаимодействие с пользователями и группами. ВКонтакте
#todo предоставляет достаточно широкие возможности в своём API: всё, что можно
#todo делать вручную через браузер, доступно и в API.

#? ДРУГИЕ API

#* Вы познакомились с интерфейсами прикладного программирования — API (на примере API социальной 
#*  сети ВКонтакте).

#* API для разработчиков предоставляют и многие другие платформы. Вот список, пожалуй,
#*  самых популярных из них:

#* Google Maps API
#* YouTube API
#* Twitter API
#* Facebook API
#* Вы также можете воспользоваться интернет-поиском, указав в поисковой строке, например,
#* «курсы валют API» или «прогноз погоды api», — среди первых результатов выдачи чаще
#* всего с лёгкостью можно найти ссылки на необходимый функционал.

#! Как настроить регулярную выгрузку данных

#? СКРИПТЫ

#* Как уже говорилось, скриптом принято называть небольшую компьютерную программу,
#* которая автоматизирует выполнение некоторой задачи. Программы, которые мы
#* создаём на языке Python, также являются скриптами.

#* А что делать, если вам нужно, чтобы ваш скрипт запускался иногда? Каждую пятницу, 13-го? 
#* В день рождения супруга (или супруги)? Или просто каждый час?

#* В этом случае вам нужен автоматический запуск скриптов, или, как часто его называют программисты,
#* запуск по крону — от английского акронима Cron (англ. Command Run ON) — названия системы для
#* автоматического запуска программ и скриптов на сервере в определённое время.

#todo Автоматический запуск может понадобиться, например:

#* если вы хотите с определённой периодичностью скачивать новую информацию с сайтов,
#* например выполнять парсинг новостей для последующего анализа (как мы уже знаем, этот
#* процесс называется web-scraping);

#* если ваш скрипт должен следить за курсом акций и каждую минуту делать запрос по API,
#* чтобы получить новые котировки;

#* если вы написали обучающую платформу и вам нужно каждый час проверять, кто из студентов
#* приступил к занятиям и насколько успешно продвигается их обучение;

#* если у вас есть 500 вендинговых автоматов по продаже солнечных очков и каждые пять минут
#* вы должны опрашивать все автоматы, чтобы узнать, не закончились ли очки.

#? КАК НАСТРОИТЬ АВТОМАТИЧЕСКИЙ ЗАПУСК

#* Исполняемый по расписанию код часто называют задачей (англ. task). Для планирования задач
#* в Python есть несколько библиотек, среди которых — популярный и простой в использовании
#* модуль schedule (c англ. расписание). Он позволяет запускать код как с определённым
#* интервалом, так и в заданное время.

#* Модуль schedule не входит в стандартную библиотеку Python, поэтому его необходимо установить:

# Устанавливаем библиотеку schedule
!pip install schedule 

#* Для того чтобы у нас появилась возможность использовать модуль в коде, импортируем его:
import schedule # Импортируем модуль schedule

#? ПОСТАНОВКА ЗАДАЧИ

#* Рассмотрим вариант автоматического запуска простой функции, которая выводит на
#* экран короткое сообщение:

def task(): 
    print('Hello! I am a task!') 
    return 

#* Для запуска задачи через определённые интервалы времени в модуле schedule
#* используется метод every(), который получает в качестве единственного аргумента
#* число, указывающее, как часто следует запускать код.

#* Далее вызывается метод, определяющий единицы измерения промежутков времени, через
#* которые будет выполняться функция. В нашем примере это минуты. Вот как будет выглядеть итоговый код:
schedule.every(15).minutes.do(task)

#* Если бы мы хотели запускать задачу, например, каждый час, то могли бы написать:

schedule.every(1).hour.do(task) 

#? ВЫПОЛНЕНИЕ ФУНКЦИИ

#* Бесконечный цикл необходим чтобы запускать наш менеджер расписания (schedule)
#* постоянно, чтобы постоянно проверять, не пришло ли время снова выполнить задачу.

#* Внутри цикла мы будем вызывать особый метод run_pending() для объекта schedule, который
#* будет проверять, нет ли задачи, которую пора выполнить.

#* После вызова метода run_pending() нужно будет сделать небольшую паузу, после
#* которой можно будет снова проверять, не пришло ли время для выполнения какой-либо функции.

#* Давайте напишем этот код.

#* Для создания паузы мы будем использовать метод sleep из модуля time,
#* поэтому наш код начнётся с импорта данного модуля:

import time 

#todo while True: 
#todo     schedule.run_pending() 
#todo     time.sleep(1) - пауза в одну секунду
    
#todo Вот какой код в итоге получился:

import schedule

def task(): 
    print('Hello! I am a task!') 
    return

schedule.every(15).minutes.do(task)

import time 
#todo while True: 
#todo     schedule.run_pending() 
#todo     time.sleep(1) - пауза в одну секунду
    
#* Этот код будет каждую секунду проверять, не надо ли выполнить какую-то задачу, и раз в 15
#* минут будет выводить на экран фразу: "Hello! I am a task!" Вывод сообщения будет повторяться
#* до тех пор, пока вы не остановите выполнение скрипта.


