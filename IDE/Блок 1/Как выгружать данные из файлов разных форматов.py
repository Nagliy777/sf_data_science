
#! Работа с текстовыми файлами

#?  ИСПОЛЬЗУЕМ ФУНКЦИЮ READ_TABLE()

#* Функция read_csv(), как вы уже знаете, загружает данные с разделителями из файла, URL-адреса,
#* и в качестве разделителя по умолчанию используется запятая (символ). В документации эта функция
#* описана как «Чтение данных из файла значений, разделённых запятыми (CSV), в DataFrame».

#* Функция read_table() также загружает данные с разделителями из файла, URL-адреса,
#* но в качестве разделителя по умолчанию используется символ табуляции ('\t'). В документации
#* эта функция описана как «Чтение данных из файл значений с разделителями в DataFrame».

#todo Для демонстрации использования функции read_table() выполним следующее: 

#todo используя  функцию read_csv(), считаем данные из файла countries.csv в 
#todo переменную countries_data, создав объект DataFrame;
#todo используя уже знакомую функцию to_csv(), выгрузим этот DataFrame в файл
#todo countries.txt (с расширением TXT), который сохраним в папке data. В качестве разделителя используется символ пробела (" ").

# Импорт библиотеки pandas — при выполнении последовательно всех примеров ниже
# импорт выполняется один раз
import pandas as pd 
# Загружаем данные из файла в переменную, создавая объект DataFrame
countries_data = pd.read_csv('data/countries.csv', sep=';') 
# Выгружаем данные из DataFrame в CSV-файл и сохраняем файл в папке data
countries_data.to_csv('data/countries.txt', index=False, sep=' ')

#todo Считаем данные из файла countries.txt в переменную txt_df  (объект DataFrame), применив функцию read_table() с параметрами sep=' '  и  index_col=['country'] (так мы избавимся от столбца с индексом и присвоим названия строкам, используя данные одного из столбцов). Выводим на экран полученный результат:

# Загружаем данные из файла в переменную, создавая объект DataFrame
txt_df = pd.read_table('data/countries.txt', sep=' ', index_col=['country'])
# Выводим содержимое DataFrame на экран
display(txt_df)

#? ПРИМЕНЕНИЕ ПАРАМЕТРА HEADER

#* Используя параметр header, при создании DataFrame мы учитываем наличие/отсутствие строки
#* заголовков в исходном файле данных.

#* Например, если при считывании данных из ранее сохранённого в папке data файла melb_data_ps.csv
#* указать значение параметра header=None, то первая строка исходного файла не будет восприниматься
#* как строка заголовка и будет отнесена к области данных DataFrame:

# Загружаем данные из файла в переменную, создавая объект DataFrame
melb_data = pd.read_csv('data/melb_data_ps.csv', header=None) 
# Выводим содержимое DataFrame на экран
display(melb_data)

#? РЕШАЕМ ПРОБЛЕМУ С КОДИРОВКОЙ ИСХОДНЫХ ДАННЫХ
#* При считывании файла и создании DataFrame может возникнуть проблема — при выводе на экран данные
#* будут отображаться в виде нечитаемых символов. Это связано с кодировкой символов в исходном файле.

#todo узнаем, какая кодировка символов используется в считываемом файле, для этого обратимся к субмодулю chardet.
#todo universaldetector библиотеки Universal Encoding Detector. Модуль необходимо предварительно установить с
#todo помощью стандартной команды менеджера пакетов pip: pip install chardet;
#todo при считывании файла и создании DataFrame будем использовать параметр encoding  —
#todo указывает, какой тип кодировки символов используется в считываемом файле. 

#? ЛОКАЛИЗУЕМ ПРОБЛЕМУ

#todo Считываем файл и создаем DataFrame без использования параметра encoding:
# Считываем данные из файла с неизвестной кодировкой в переменную, создавая объект DataFrame
data=pd.read_csv('data/ErrorEnCoding.csv', header=None, encoding_errors='replace') 
# Выводим содержимое DataFrame на экран
display(data)

# Выявлена проблема: при стандартном считывании содержимое файла читается некорректно. Необходимо
# указать кодировку файла при считывании.

#? ОПРЕДЕЛЯЕМ КОДИРОВКУ ФАЙЛА

#todo Приведённый ниже код поможет нам определить используемую кодировку в файле, степень достоверности,
#todo используемый язык.

# Импортируем субмодуль chardet.universal
from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()

with open('data/ErrorEnCoding.csv', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
print(detector.close())

#* С достоверностью примерно 84 % тип используемой в файле кодировки — koi8-r. Повторим считывание файла,
#* используя полученные данные.

#* При открытии файла использовалась конструкция with ... as ... (с англ. «с... как...»). 
#* Эта конструкция применяется для гарантии того, что критические функции и методы (в данном случае метод 
#* .close() закрывает открытый ранее файл) будут выполнены в любом случае.

#? СЧИТЫВАЕМ ФАЙЛ, УКАЗАВ КОДИРОВКУ

# Создаем DataFrame из файла, явно указав кодировку символов, и выводим его содержимое на экран
data=pd.read_csv('data/ErrorEnCoding.csv', encoding='koi8-r', header=None)
display(data)

#* Проблема, связанная с кодировкой файла, решена.

#? ЧТЕНИЕ ФАЙЛА ПО ССЫЛКЕ, ИСПОЛЬЗУЯ ФУНКЦИЮ READ_TABLE()

data = pd.read_table('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/melb_data.csv', sep=',')
display(data)

#? ЧТЕНИЕ/ЗАПИСЬ АРХИВИРОВАННЫХ CSV-ФАЙЛОВ

#* Большие по размеру CSV-файлы для экономии памяти часто «упаковывают» в архив, например zip. 

#todo файл в zip-архиве должен быть один (если файлов в архиве несколько, то можно разархивировать файлы
#todo и работать с каждым вне архива.

data = pd.read_csv('data/students_performance.zip')
display(data)

#* В функции to_csv() предусмотрен механизм, позволяющий проводить упаковку CSV-файлов в zip-архив.
#* Проделаем обратную операцию — данные из DataFrame data запишем в CSV-файл, упакуем полученный файл
#* в zip-архив «на лету» и сохраним полученный архив в папке data, выполнив следующий код:

# Определяем параметры архивирования — метод сжатия, имя файла в архиве
compression_opts = dict(method='zip', archive_name='out.csv') 
data.to_csv('data/out.zip', index=False, compression=compression_opts)

#* В ходе выполнения кода содержимое DataFrame сохранено в файле out.csv, файл упакован в архив out.zip,
#* а архив записан в каталог data.

#! Работа с файлами Excel

#* XLS- и XLSX-файлы могут помимо данных включать формулы, изображения, графики и содержат информацию о форматировании.

#? СЧИТЫВАНИЕ ДАННЫХ ИЗ ФАЙЛА EXCEL

#* В pandas предусмотрена функция для удобного чтения XLS- и XLSX- файлов: read_excel(). Синтаксис обеих функций практически идентичен.

grades = pd.read_excel('data/grades.xlsx')
display(grades.head())

#? СЧИТЫВАНИЕ ДАННЫХ ИЗ ФАЙЛА EXCEL ПО ССЫЛКЕ
data = pd.read_excel('https://github.com/asaydn/test/raw/master/january.xlsx', skiprows=3)
display(data)

#* io — первый параметр, в который мы передаём адрес файла, который хотим прочитать.
#* Кроме адреса на диске, можно передавать адрес в интернете.

#* sheet_name —  ссылка на лист в Excel-файле (возможные значения данного параметра:
#* 0 — значение по умолчанию, загружается первый лист; 'Sheet1' — можно передать название листа;
#* обычно листы называются 'SheetX', где X — номер листа, но могут использоваться и другие названия;
#* [0, 1, 'Sheet3'] — список, содержащий номера или названия листов; в таком случае Pandas вернёт
#* словарь, в котором ключами будут номера или названия листов, а значениями — их содержимое в
#* виде DataFrame; None — если передать такое значение, то pandas прочитает все листы и вернёт их
#* в виде словаря, как в предыдущем пункте).

#* na_values — список значений, которые будут считаться пропусками ( ‘’, ‘#N/A’, ‘ N/A’, ‘#NA’, ‘-1.#IND’,
#*  ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, ‘NA’, ‘NULL’, ‘NaN’, ‘n/a’, ‘nan’, ‘null’).

#todo По умолчанию в DataFrame читается информация из первого листа, однако read_excel()  позволяет выбрать,
#todo из какого именно листа загружать данные. Сделать это можно с помощью параметра sheet_name
#todo (рус. имя_листа). Например, чтобы прочесть данные из второго листа (ML) файла, выполним код:

grades = pd.read_excel('data/grades.xlsx', sheet_name='ML')
display(grades.head())

#? ВЫГРУЗКА ДАННЫХ ИЗ DATAFRAME В EXCEL-ФАЙЛ

# Сохраняем данные из DataFrame grades в файл grades_new.xlsx в папке data
grades.to_excel('data/grades_new.xlsx')

#* В этом случае будет создан один лист с именем по умолчанию "Sheet1"
#* Также мы сохраним и индекс — в данных будет находиться лишний столбец.

#todo Чтобы создать лист с определённым именем (например, Example) и не сохранять индекс, в метод  to_excel()
#todo необходимо передать параметры sheet_name='Example' и index=False:

# Сохраняем данные из DataFrame grades в файл grades_new.xlsx (на листе 'Example') в папке data
grades.to_excel('data/grades_new.xlsx', sheet_name='Example', index=False)

#! JSON. Что это?

#todo JSON — это простой, структурированный формат обмена данными, основанный на использовании текста.

#* Под обменом данных в этом контексте чаще всего подразумевается передача данных по компьютерным сетям,
#* например пересылка данных от сервера к браузеру.

#* Аббревиатура JSON расшифровывается как JavaScript Object Notation, в переводе на русский — система
#* обозначения/записи объектов JavaScript. Несмотря на то, что JSON изначально основывался на языке
#* программирования JavaScript, он является общепризнанным форматом обмена данными, и многие языки
#* программирования, включая Python, содержат эффективные инструменты для работы с ним.

#? МОДУЛИ ДЛЯ РАБОТЫ С JSON
#* Для работы с данными в формате JSON используется модуль json из стандартной библиотеки языка Python
#* функция pprint(), с помощью которой можно красиво выводить на экран содержимое JSON-файла
# Импортируем модуль json
import json
# Импортируем функцию pprint()
from pprint import pprint

#? КАК ВЫГЛЯДИТ JSON-ФАЙЛ?

#* Информация в формате JSON представляет собой (в закодированном виде) одну из двух структур:
#* набор пар "ключ-значение", где ключ — это всегда строковая величина (в Python такая структура преобразуется в словарь);
#* упорядоченный набор значений (при чтении JSON-файла в Python эта структура будет преобразована в список).

#todo Формат JSON допускает неограниченное количество вложений этих структур друг в друга.

#? ОТКРЫВАЕМ JSON-ФАЙЛ

#* Чтобы перевести данные из формата JSON в формат, который можно обрабатывать инструментами Python,
#* необходимо выполнить процедуру, которая называется десериализация (декодирование данных). Обратный
#* процесс, связанный с переводом структур данных Python в формат JSON, называется сериализацией.

#todo Для выполнения десериализации мы воспользуемся методом load() (от англ. загрузить) модуля json,
#todo который принимает на вход ссылку на открытый JSON-файл:

# Открываем файл и связываем его с объектом "f"
with open('recipes.json') as f:  
    # Загружаем содержимое открытого файла в переменную recipes  
    recipes = json.load(f)
    
#? ИЗВЛЕКАЕМ ДАННЫЕ ИЗ JSON-ФАЙЛА

#* Давайте выясним некоторые детали о блюде, которое записано первым в списке блюд. Его индекс — 0,
#* и информация о нём хранится в словаре. Чтобы узнать ID этого блюда, мы можем обратиться к
#* соответствующему ключу словаря, выполнив следующий код:

recipes[0]['id']

#* Аналогичным образом, для получения списка ингредиентов первого блюда в списке мы можем использовать
#* тот же код, заменив в нём ключ 'id' на 'ingredients'

#todo Мы также можем извлечь информацию о конкретном блюде по его ID. Для этого необходимо с помощью цикла,
#todo например for, перебрать все элементы списка, проверяя ключ 'id',  и извлечь нужную информацию,
#todo когда мы наконец найдем нужное блюдо.

#? ИЗ JSON В PANDAS
#* Как вы помните, после десериализации наши данные были преобразованы в список, элементами
#* которого являются вложенные словари, содержащие по три пары "ключ-значение". 
#* Поскольку структура всех вложенных словарей одинакова, мы можем создать DataFrame на основе списка,
#* не проводя с ним никаких дополнительных манипуляций:

# Импортируем модуль json
import json 
# Импортируем функцию pprint()
from pprint import pprint 
# Импортируем модуль pandas
import pandas as pd 
# Открываем файл и связываем его с объектом "f"
with open('recipes.json') as f: 
    # Загружаем содержимое открытого файла в переменную recipes
    recipes = json.load(f) 
# Создаём объект DataFrame из списка recipes
df = pd.DataFrame(recipes) 
# Выводим на экран первые строки полученного DataFrame
display(df.head())

#* Для непосредственного считывания содержимого файла recipes.json в переменную df (объект DataFrame)
#* используйте функцию read_json() (с англ. читать_json).

# Импортируем модуль pandas
import pandas as pd 
# Создаём объект DataFrame, загружая содержимое файла recipes.json
df = pd.read_json('recipes.json') 

#* Такая структура не очень практична, поскольку она не позволяет осуществлять группировку данных
#* и выполнять многие другие операции, связанные с исследованием ингредиентов разных блюд. Например,
#* представьте, что вы хотите отфильтровать блюда, состоящие не более чем из пяти ингредиентов, или блюда,
#* не содержащие мяса. Сделать это, когда ингредиенты блюд хранятся в списках, не очень просто.

#todo пример
#* Создадим функцию для заполнения значения в каждой ячейке. Функция будет проверять наличие конкретного
#* ингредиента в столбце ingredients для текущего блюда и возвращать 1, если ингредиент есть в рецепте, и 0, если он отсутствует.

#todo Функция будет возвращать 1, если ингредиент есть в рецепте, и 0, если он отсутствует:

# Определяем имя функции и передаваемые аргументы    
def contains(ingredient_list): 
    # Если ингредиент есть в текущем блюде,
    if ingredient_name in ingredient_list:   
        # возвращаем значение 1
        return 1 
    # Если ингредиента нет в текущем блюде,
    else: 
        # возвращаем значение 0
        return 0
    
#* Осталось лишь перебрать все ингредиенты из ранее созданного реестра all_ingredients с помощью цикла
#* for  и создать в DataFrame столбец с соответствующим названием, заполнив его единицами и нулями.
#* Для этого применим к DataFrame, а точнее, к столбцу ingredients функцию contains().

# Последовательно перебираем ингредиенты в реестре all_ingredients
for ingredient_name in all_ingredients: 
    # В DataFrame cоздаем столбец с именем текущего ингредиента 
    # и заполняем его единицами и нулями,
    # используя ранее созданную функцию contains
    df[ingredient_name] = df['ingredients'].apply(contains)
    
# Заменяем список ингредиентов в рецепте на их количество 
df['ingredients'] = df['ingredients'].apply(len) 
# Выводим содержимое полученного DataFrame на экран
display(df)

#? СОХРАНЯЕМ DATAFRAME В CSV-ФАЙЛЕ

#* Если мы планируем продолжать работать с DataFrame, созданными на основе данных, которые мы получили
#* в JSON-формате, то полезно будет сохранить промежуточный DataFrame в виде CSV-файла.

df.to_csv('recipes.csv', index = False)

#? ИЗ PANDAS В JSON

#*Решим обратную задачу и создадим JSON-файл из сохранённого ранее CSV-файла, который
#*получили в конце предыдущего этапа. 

#* Теперь, используя только данные из этого файла, нам нужно в точности воссоздать структуру исходного
#* JSON-файла. Мы помним, что после десериализации данные представляли собой список, состоящий из словарей.
#* В каждом словаре хранилась информация о рецепте одного блюда. Каждый словарь состоял из трёх пар "ключ-значение".
#* Первая пара содержала название кухни, к которой относилось блюдо, вторая — id блюда, и третья — список ингредиентов
#* входящих в состав блюда.

#todo Напишите код для создания списка id всех блюд, нужны только уникальные значения представленных в DataFrame.
#todo Результирующий список занесите в переменную ids

ids = list(df['id'].unique())

#todo Напишите код для создания списка ингредиентов всех блюд, представленных в DataFrame.
#todo Результирующий список занесите в переменную ingredients.

ingredients = list(df.columns)[3:]

#* Теперь мы можем использовать подготовленные списки ids и ingredients для непосредственного создания JSON-структуры.

#* сейчас нам предстоит воссоздать эту структуру, извлекая данные из DataFrame.
#* Для этого необходимо создать:

#* пустой список new_recipes — для хранения итоговой структуры;
#* список ids — для хранения id всех блюд;
#* список ingredients — для хранения названий всех ингредиентов.

#* Написать код функции make_list(), которая принимает на вход строку DataFrame df, содержащую полные данные об одном блюде, и возвращает перечень ингредиентов, входящих в состав этого блюда в виде списка.
#* Организовать цикл с параметром, в котором будут перебираться элементы списка ids. В результате в процессе прохождения цикла параметр должен принять значение id каждого блюда.
#* На каждом шаге цикла создать словарь, содержащий три пары "ключ-значение":
#* ключу "id" присвоить текущее значение параметра цикла как целого числа;
#* ключу "cuisine" присвоить значение соответствующей кухни, которое мы получим, применив фильтр по текущему id к DataFrame df;
#* ключу "ingredients" присвоить значение списка, воспользовавшись функцией make_list(), созданной на первом шаге алгоритма.
#* Каждый созданный словарь добавить к списку new_recipes:

# Создаём пустой список для хранения итоговой структуры
new_recipes = [] 
# Организуем цикл с параметром current_id
for current_id in ids: 
    # Получаем значение соответствующей кухни, применив фильтр по текущему значению параметра цикла к DataFrame;
    cuisine = df[df['id'] == current_id]['cuisine'].iloc[0] 
    # Получаем перечень ингредиентов, входящих в состав текущего блюда
    current_ingredients = make_list(df[df['id'] == current_id]) 
    # Создаём текущий словарь
    current_recipe = {'cuisine': cuisine, 'id': int(current_id), 'ingredients': current_ingredients} 
    # Добавляем созданный словарь к списку
    new_recipes.append(current_recipe)
    
def make_list(row): # Определяем имя функции и аргументы
  ingredient_list=[] # Создаем пустой список ингредиентов проверяемого блюда
  for ingredient in ingredients: # Перебираем ингредиенты из реестра
    if row[ingredient].item()==1: # Если ингредиент входит в состав текущего блюда
      ingredient_list.append(ingredient) # Добавляем его в список ингредиентов текущего блюда
  return ingredient_list # Возвращаем список ингредиентов


#* Выполним сериализацию списка new_recipes и запишем полученные данные в файл.

#* Для сериализации  используем функцию dumps(), которой в качестве параметра передадим список new_recipes.
#* Запись в файл осуществляется с помощью метода write(). Предварительно файл необходимо открыть для записи
#* с помощью функции open() c параметром 'w' (от англ. write, рус. писать):

# Импорт модуля json
import json 
# Функция dumps() модуля json сериализирует объект Python в строку формата JSON. 
new_recipes = json.dumps(new_recipes) 

# Откроем файл new_recipes.json для записи
with open("data/new_recipes.json", "w") as write_file: 
    # Записываем содержимое подготовленные данные в файл
    write_file.write(new_recipes)
    
#todo Итак, задача по созданию JSON-файла из сохранённого ранее CSV-файла решена!

#! XML. Что это?

#* Аббревиатура XML расшифровывается как eXtensible Markup Language — расширяемый язык разметки.
#* Он (язык) позволяет описывать документы, используя теги.

#* Если вы когда-нибудь сталкивались с HTML, языком разметки для создания веб-страниц, то можете заметить,
#* что XML очень похож на него

#todo Файлы XML не всегда имеют жёсткую структуру и не обязаны её иметь, но чаще всего какая-то структура внутри
#todo файла будет. Почему? Потому что обычно XML не пишут вручную. Такие файлы генерируются кодом и читаются тоже
#todo кодом. Поэтому при наличии понятной структуры обработка файла становится намного проще.

#? ИЗВЛЕКАЕМ КОНТЕНТ ИЗ XML-ФАЙЛА

#* Данные в формате XML имеют древовидную структуру. 

#* Что такое дерево? Это структура, которая имеет узлы и связи между ними. Самый верхнеуровневый
#* узел называется корнем, а всё, что находится в самом низу, называется листьями. 

#* В файле используется набор тегов, внутри которых могут находиться другие теги со своими значениями.

#* Для работы с XML-файлами мы будем использовать модуль ElementTree , входящий в стандартный пакет xml.
#* Этот модуль позволит нам «перемещаться» по дереву XML и смотреть, что находится в каждом его узле,
#* начиная с корня и заканчивая листьями.

#* Импортируем этот модуль под псевдонимом ET: 

# Импортируем модуль ElementTree
import xml.etree.ElementTree as ET

#* Для работы со структурой файла menu.xml считаем его содержимое в переменную tree, выполнив код:
tree = ET.parse('menu.xml')

#? КОРЕНЬ

#* Запишем в переменную root корневой узел дерева tree и посмотрим, как выглядит содержимое переменной
#* root, для чего выполним код:

root = tree.getroot()
display(root)
# <Element 'menu' at 0x000001DD75EAF600>
#* Мы видим, что в корне находится 'menu'. Всё правильно, мы и предполагали увидеть именно это. 

#* Какой тип у этого объекта? Если мы вызовем встроенный в Python метод type() и передадим ему root ,
#* то увидим, что это тип xml.etree.ElementTree.Element. Такой тип будет у любого узла в дереве.

display(type(root))
# xml.etree.ElementTree.Element

#? ПОТОМКИ

#* Для того чтобы посмотреть список потомков корневого узла, выполним следующий код:
display(list(root))

# [<Element 'dish' at 0x000001DD75EAF240>,
# <Element 'dish' at 0x000001DD75EAC5E0>]

#* Если у узла нет потомков, то вернётся пустой список — []

#* Итак, использование list(root) возвращает список потомков указанного узла. У узла root, который
#* представляет меню, два потомка, а именно — два блюда, которые представлены тегами dish.
#* Для того чтобы получить список потомков второго блюда в нашем меню и вывести его на экран,
#* выполним код:
display(list(root[1]))
# [<Element 'price' at 0x000001DD75EADEE0>,
#  <Element 'weight' at 0x000001DD75EAE8E0>,
#  <Element 'class' at 0x000001DD75EAD990>]

#? АТРИБУТЫ И ТЕГИ

#* Как было сказано ранее, у узлов могут быть параметры, или атрибуты. Например, у узлов dish
#* есть атрибут name, который хранит название блюда.
#* Мы можем непосредственно обратиться к атрибутам, используя attrib.
#* Выведем на экран атрибуты первого блюда из меню:

display(root[0].attrib)
# {'name': 'Кура'}

#* В XML-узлах часто хранятся количественные показатели. Эти показатели хранятся в виде текста,
#* и прочитать их можно, обратившись к атрибуту text у соответствующего объекта типа ElementTree.Element.

#* Например, возьмём узел price первого блюда из меню:
display(root[0][0])
# <Element 'price' at 0x000001DD75EACD10>

#* Теперь прочитаем значение этого узла с помощью text:
display(root[0][0].text)
# '40'

#todo Все значения в XML, даже числовые, хранятся как строки, поэтому преобразовывать их к нужному
#todo типу вам нужно самим.

#* Например, в данном случае можно обернуть значение стоимости в int() или float().

#* Если вы хотите прочитать наименование тега конкретного узла, необходимо использовать tag. Например,
#* получим наименование тега корневого узла:

display(root.tag)
# 'menu'

#? ИСПОЛЬЗОВАНИЕ ЦИКЛОВ
#* Итак, мы научились обращаться к отдельным узлам дерева, представляющего XML-структуру,
#* и извлекать информацию о его атрибутах, значении и потомках.

#* На этом шаге мы решим задачу вывода на экран наименование всех блюд из меню, а также информацию о них
#* (иными словами, нам необходимо обойти дерево и вывести на экран значения его листьев).

#todo Используя цикл for, автоматизируем обход дерева. Для этого напишем следующий код:

for dish in root:
    for param in dish:
        print(dish.attrib['name'], param.tag, param.text)
    print()
    
    
#todo В этом коде реализован следующий алгоритм:

#* В первом (внешнем) цикле перебираем потомков корня дерева (root). Потомки перебираются последовательно
#* при помощи переменной dish. Это отдельные блюда из меню.

#* Во втором (вложенном) цикле аналогичным образом перебираем потомков каждого блюда. Этими потомками

#* являются параметры блюда — его цена (price), вес (weight) и класс (class).
#* После этого выводим на экран название блюда (значение атрибута name), название очередного
#* параметра (tag) и его значение (text).

#* Дополнительная функция print() в цикле верхнего уровня предназначена для организации более
#* удобного восприятия информации — между отдельными блюдами будет выведена пустая строка.
#* На выходе получаем:

""" Кура price 40
Кура weight 300
Кура class Мясо

Греча price 20
Греча weight 200
Греча class Крупа """

#? ЗАГРУЖАЕМ ДАННЫЕ ИЗ XML-ФАЙЛА В DATAFRAME

#todo Реализуем следующий алгоритм:

#* 1. Загрузить XML-структуру файла menu.xml в переменную root.
#* 2. Создать пустой список df_list (в него будем добавлять строчки итоговой таблицы).
#* 3. Заранее создать список column_names с именами столбцов — название блюда (name), его цена (price), вес (weight) и класс (class).
#* 4. В цикле организовать обход xml-дерева из корня по всем потомкам.
#* 5. На каждой итерации цикла сформировать в виде списка строку таблицы, содержащую информацию: наименование блюда (атрибут name узла dish) и значения потомков этого узла — узлов price, weight, class.
#* 6. Добавить сформированную строку в список df_list, используя метод append().
#* 7. Сформировать из вложенного списка DataFrame. Имена для столбцов взять из списка column_names.

import xml.etree.ElementTree as ET
tree = ET.parse('menu.xml')
root = tree.getroot()

import pandas as pd
column_names = ['name', 'price', 'weight', 'class']
df_list = []

for dish in root:
    row = [dish.attrib['name'], dish[0].text, dish[1].text, dish[2].text]
    df_list.append(row)
    df = pd.DataFrame(df_list, columns=column_names)
display(df)

#? СОЗДАЁМ XML-ФАЙЛ

#* Воссоздадим структуру нашего исходного XML-файла с нуля, руководствуясь общими рекомендациями.

#todo Чтобы создать корень дерева, используем метод Element() из класса ElementTree:

import xml.etree.ElementTree as ET

new_root = ET.Element('menu')
display(new_root)

#* Теперь мы можем добавлять новые узлы в наше дерево, используя метод SubElement() из того же класса.

#* Добавим в наше меню двух потомков корневого узла, которые будут представлять два блюда,
#* то есть будут узлами dish:

dish1 = ET.SubElement(new_root, 'dish', name='Кура')

dish2 = ET.SubElement(new_root, 'dish', name='Греча')

display(list(new_root))

#* В метод SubElement() мы передали первым аргументом узел, к которому добавляем потомка,
#* вторым аргументом — наименование нового тега (dish),  третьим аргументом — наименование
#* атрибута нового узла( name ) и его значение.

#* Аналогичным образом можно добавлять новые узлы к любым существующим узлам, не только к корню.

#* Добавим в создаваемую структуру по три потомка (атрибута) к двум новым узлам, которые будут содержать
#* информацию о блюде — о его цене (price), весе (weight) и классе (class), а также значение этих атрибутов:

price1 = ET.SubElement(dish1, "price").text = "40"
weight1 = ET.SubElement(dish1, "weight").text = "300"
class1 = ET.SubElement(dish1, "class").text = "Мясо"
display(list(dish1))

price2 = ET.SubElement(dish2, "price").text = "20"
weight2 = ET.SubElement(dish2, "weight").text = "200"
class2 = ET.SubElement(dish2, "class").text = "Крупа"
display(list(dish2))

"""[<Element 'price' at 0x000001DD75EA5990>,
 <Element 'weight' at 0x000001DD7AAEAE30>,
 <Element 'class' at 0x000001DD75EAD210>,
 <Element 'price' at 0x000001DD78B4ACA0>,
 <Element 'weight' at 0x000001DD78B4A7A0>,
 <Element 'class' at 0x000001DD78B4A1B0>]"""
 
#todo Проверим визуально корректность созданной нами структуры, выполнив фрагмент кода, разработанного ранее:
for dish in new_root:    
    for param in dish:
        print(dish.attrib['name'], param.tag, param.text)
    print()
    
#? СОХРАНЕНИЕ XML-ФАЙЛА

#*  В финале работы с файлом XML-формата запишем созданную нами структуру как XML-файл на диск.

#* Преобразуем созданный нами объект типа ElementTree.Element в строку c помощью метода tostring(),
#* передав наше новое дерево как аргумент. Сохраним эту строку на диске, используя стандартные средства Python::

new_root_string = ET.tostring(new_root)

with open("new_menu.xml", "wb") as f:
    f.write(new_root_string)
    
#todo Возможно, вы увидите проблему, связанную с кодировкой. Что делать в этом случае? Как вариант — записать
#todo файл, используя сам класс ElementTree() :

ET.ElementTree(new_root).write('new_menu_good.xml', encoding="utf-8")

#todo Для этого мы передаём в класс ElementTree() наше дерево (не его строковое представление) и вызываем
#todo метод write(). В метод мы передаём путь к новому файлу и нужную нам кодировку.
