
#! Matplotlib — это библиотека Python, обладающая большим количеством возможностей
#! для визуализации и настройки отображения графиков и диаграмм.

#* Для установки библиотеки введите в командную строку (или командную строку Anaconda) следующее:
pip install matplotlib

#* Библиотека Matplotlib позволяет работать в нескольких режимах. Самый распространённый
#* и мощный по функционалу — объектно-ориентированный режим. Он основан на работе с объектами
#* фигур (figure, их ещё называют канвасами или холстами) и координатных плоскостей (axes, или
#* системы координат). 

#? Основные параметры метода scatter()

x, y — последовательности, которые будут отложены по осям абсцисс и ординат;
s — размер маркеров;
marker — вид маркеров ('o' — точки, '^' — треугольники);
c — цвет маркеров.

#todo Пример
us_data = covid_df[covid_df['country'] == 'United States']

fig = plt.figure(figsize=(8, 4))
axes = fig.add_axes([0, 0, 1, 1])
axes.scatter(
    x=us_data['people_fully_vaccinated'], 
    y=us_data['daily_confirmed'], 
    s=100,
    marker='o',
    c = 'blue'
);

#? Для построения круговых диаграмм в Matplotlib используется метод pie().

Основные параметры метода pie()

x — значения, по которым будет строиться круговая диаграмма;
labels — метки, соответствующие значениям;
autopct — формат отображения долей на диаграмме (например, '%.1f%%' означает, что округление будет производиться до первого знака после запятой и при выводе будет указан знак "%"; открывающий и закрывающий проценты означают форматирование, а внутренний — вывод знака "%");
explode — последовательность, которая определяет долю смещения сектора от центра для каждого значения из x.

#todo Пример:
#* ТОП-10 комбинаций вакцин (vaccines) по распространённости мы находим с помощью метода value_counts()

vaccine_combinations = covid_df['vaccines'].value_counts()[:10]
fig = plt.figure(figsize=(5, 5))
axes = fig.add_axes([0, 0, 1, 1])
axes.pie(
    vaccine_combinations,
    labels=vaccine_combinations.index,
    autopct='%.1f%%',
    explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
);

#!  ДОБАВЛЕНИЕ ИНФОРМАТИВНОСТИ В ГРАФИКИ

axes.set_title() — заголовок диаграммы, а также его настройки (например, параметр fontsize отвечает за размер шрифта);
axes.set_xlabel() — название оси абсцисс;
axes.set_ylabel() — название оси ординат;
axes.set_xticks() — установка отметок на оси абсцисс;
axes.set_yticks() — установка отметок на оси ординат;
axes.xaxis.set_tick_params() — управление параметрами отметок на оси абсцисс (например, параметр rotation отвечает за поворот отметок в градусах);
axes.yaxis.set_tick_params() — управление параметрами отметок на оси ординат;
axes.legend() — отображение легенды;
axes.grid() — установка сетки.

#? Для построения линейных графиков в Matplotlib используется метод plot()
#?  (не путайте с методом plot() в Pandas!). 

#todo Пример:

china_data = covid_df[covid_df['country'] == 'China']
china_grouped = china_data.groupby(['date'])[['confirmed', 'active', 'deaths', 'recovered']].sum()

#визуализация графиков
fig = plt.figure(figsize=(10, 4))
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(china_grouped['confirmed'], label='Общее число зафиксированных случаев', lw=3)
axes.plot(china_grouped['deaths'], label='Общее число смертей', lw=3)
axes.plot(china_grouped['recovered'], label='Общее число выздоровевших пациентов', lw=3)
axes.plot(china_grouped['active'], label='Общее число активных случаев', lw=3, linestyle='dashed')

#установка параметров отображения
axes.set_title('Статистика Covid-19 в Китае', fontsize=16)
axes.set_xlabel('Даты')
axes.set_ylabel('Число случаев')
axes.set_yticks(range(0, 100000, 10000))
axes.xaxis.set_tick_params(rotation=30)
axes.grid()
axes.legend();

#? Столбчатые диаграммы с помощью метода bar().
Основные параметры метода bar()

x — названия категорий, которые будут располагаться по оси абсцисс;
height — высота столбцов диаграммы, массив из показателей для визуализации (например, среднее, максимальное значение и т. д.);
width — ширина столбцов диаграммы;
color — цвет.

#todo Пример:

#!  Для добавления второй системы координат необходимо повторно применить к объекту fig метод add_axes,
#!  указав новое имя для второй системы координат.

#* Группируем таблицу по странам, находим последний по дате зафиксированный показатель с помощью метода last()
#* и выбираем ТОП-5 стран с использованием метода nlargest().

vacc_country = covid_df.groupby('country')['people_fully_vaccinated'].last().nlargest(5)
vacc_country_per_hundred = covid_df.groupby('country')['people_fully_vaccinated_per_hundred'].last().nlargest(5)

#визуализация главного графика
fig = plt.figure(figsize=(13, 4))
main_axes = fig.add_axes([0, 0, 1, 1])
main_axes.bar(x = vacc_country.index, height = vacc_country);
main_axes.set_ylabel('Число вакцинированных (2 компонент)')
main_axes.set_title('Топ 5 стран по числу полностью привитых людей')

#визуализация вспомогательного графика
insert_axes = fig.add_axes([0.6, 0.6, 0.38, 0.38])
insert_axes.bar(x = vacc_country_per_hundred.index, height = vacc_country_per_hundred, width=0.5);
insert_axes.set_ylabel('На 100 человек')
insert_axes.xaxis.set_tick_params(rotation=45)

#! SUBPLOTS

#* В большинстве случаев для отображения нескольких систем координат используется функция subplots().

#? Основные параметры метода subplots()

nrows — число строк;
ncols — число столбцов;
figsize — общий размер фигуры в дюймах (ширина и высота).

#todo Пример:
#* Например, следующий код создаст шесть координатных плоскостей, сведённых в таблицу размера 2x3:
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 5))

#? За построение гистограмм в библиотеке Matplotlib отвечает метод hist().

x — массив чисел, для которого строится гистограмма;
bins — число столбцов (корзин);
orientation — ориентация гистограммы (по умолчанию 'vertical');
color — цвет.

#todo Пример:

#* Теперь, обладая знаниями о методе subplots(), построим три графика:

#* 1. Столбчатую диаграмму, которая покажет динамику ежедневной вакцинации в России.
#* 2. Линейный график изменения ежедневной заболеваемости в стране.
#* 3. Гистограмму ежедневной заболеваемости в стране.

#* Фильтруем таблицу covid_df по признаку страны и выбираем записи только для России.

#* Для того чтобы отобразить график в соответствующей координатной плоскости, нужно обратиться
#* к списку axes по индексу (от 0 до 2). Дальнейшая настройка графиков вам уже известна.

russia_data = covid_df[covid_df["country"] == "Russia"]

# визуализация систем координат
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))

# столбчатая диаграмма
axes[0].bar(
    x=russia_data["date"],
    height=russia_data["daily_vaccinations"],
    label="Число вакцинированных",
)
axes[0].set_title("Ежедневная вакцинация в России")
axes[0].xaxis.set_tick_params(rotation=45)

# линейный график
axes[1].plot(
    russia_data["date"],
    russia_data["daily_confirmed"],
    label="Число заболевших",
    color="tomato",
    lw=2,
)
axes[1].set_title("Ежедневная заболеваемость в России")
axes[1].xaxis.set_tick_params(rotation=45)

# гистограмма
axes[2].hist(
    x=russia_data["daily_confirmed"], label=["Число заболевших"], color="lime", bins=20
)
axes[2].set_title("Гистограмма заболеваемости в России")
axes[2].xaxis.set_tick_params(rotation=30)

#! Также стоит отметить, что, помимо объектно-ориентированного подхода в работе с библиотекой Matplotlib,
#! вы можете встретить и модульный подход.

#* Модульный подход основан на обращении к модулю pyplot (plt) напрямую, а не средствами объектов фигур
#* и плоскостей. Например, следующий код строит столбчатую диаграмму: по оси x откладываются элементы
#*  списка names (названия групп), а высоту столбцов определяет список values.

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.bar(names, values)
plt.show()