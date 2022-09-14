
#не забуть подгрузить дата сет и фотографию 

import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


#задаем загаловок сайта
st.markdown('''<h1 style='text-align: center; color: black;'
            >Анализ чаевых (Деньги оставленные в благодарность к счету безвозмездо) </h1>''', 
            unsafe_allow_html=True)
if st.button('Посмотреть картинку с деньгими и людьми'):
    st.image("вставь картинку")

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
path = '/Users/borodincempion/visualization-tip-research-with/tips.csv'
df = pd.read_csv(path, index_col=0)




st.header('Для начала нам потребуется выбрать метод которым мы визуализируем иследование для вас ', anchor='relevance') 


#Даем студенту возможность выбрать самому задачу и данные (вместе с их описанием)
type_info = st.expander('Информация о методах визуализации')
type_info.markdown("""
**Таблица** вид отображения [таблицей](https://ru.wikipedia.org/wiki/Таблица)
(в условиях данной задачи : скорее **ОБЗОРНЫЙ** вид данных на который опирается данная визуализация.)
\n**Базовый график** - предсказание данных на уже настроеном отображении для наглядности и **обще/информативного**  обзора. 
\n**Пользовательский график** - то что вы настроите под себя (**наш визуалиционный сахар**)
""")

options = st.radio('Выберите метод визуализации',
  ('Таблица', 'Базовый график', "Пользовательский график"))



if options == 'Таблица':
    expander_info = st.expander("Информация о данных:")
    expander_info.markdown(
"""
\n**tips.csv**: Хранит в себе информацию трам пам пам .
""")
    if st.checkbox('Буду смотреть размер таблицы'):
            shape = st.radio(
            "Размер таблицы",
            ('Строки', 'Столбцы'))
            if shape == 'Строки':
                st.write('Количество строк:', df.shape[0])
            elif shape == 'Столбцы':
                st.write('Количество столбцов:', df.shape[1])  
    if st.checkbox('Показать таблицу по строчно'):

        number = st.number_input('Сколько строк показать', min_value=1, max_value=df.shape[0])
        st.write('не забудь пролистывать вниз если дабавишь много строк')       
        st.dataframe(df.loc[:number])
    if st.checkbox('Показать таблицу по по колоночно так чисто для визуала'):
        number = st.number_input('Сколько колонок показать', min_value=1, max_value=df.shape[1])
        st.dataframe(df[df.columns[:number]])




if options == 'Базовый график':
    with st.expander('График формы распределения BoxPlot (Ящик с усами)'):
        st.write(""" Диаграмма показывает распределение значений в выборке и основные статистические показатели: медиану (линия внутри ящика), верхний(75%) и нижний(25%) квартили, наблюдаемые минимумы и максимумы (усы), а также выбросы""")
        st.info(''' Квартили -  значения, которые делят данные на 4 группы (25%,50%,75%,100%), содержащие приблизительно равное количество наблюдений. 
        \nПо сути, это то же самое, что и перцентиль. То есть нижний квартиль - 25 перцентиль, а верхний квартиль - 75 перцентиль
        ''')
        st.write('Посмотрим на распределние чаевых по дням недели')
        box = px.box(df, x=df['day'], y=df['tip'])
        st.plotly_chart(box, use_container_width=True)

        st.write('Сравним размер чаевых которые оставляют male/female')
        box = px.box(df, x=df['sex'], y=df['tip'])
        st.plotly_chart(box, use_container_width=True)

        st.write('А так же размеры счетов  male/female')

        box = px.box(df, x=df['sex'], y=df['total_bill'])
        st.plotly_chart(box, use_container_width=True)


        st.write('В конце сравним размеры счетов по дням недели а так же по курящим и нет')
        fig1 = plt.Figure()
        ax = fig1.subplots()
        sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=df, ax = ax)
        st.pyplot(fig1, clear_figure=None)


        st.write('В конце сравним размеры чаевых по дням недели а так же по курящим и нет')
        fig1 = plt.Figure()
        ax = fig1.subplots()
        sns.boxplot(x="sex", y="tip",
            hue="smoker", palette=["m", "g"],
            data=df, ax = ax)
        st.pyplot(fig1, clear_figure=None)





if options == 'Пользовательский график':
    st.info(''' Попробуй сам выбрать параметры что бы более наглядно отобразить для себя информацию (не выбирай два одинаковых!))))''')
    with st.expander('График формы распределения BoxPlot (Ящик с усами)'):
        st.write(""" Диаграмма показывает распределение значений в выборке и основные статистические показатели: медиану (линия внутри ящика), верхний(75%) и нижний(25%) квартили, наблюдаемые минимумы и максимумы (усы), а также выбросы""")
        st.info(''' Квартили -  значения, которые делят данные на 4 группы (25%,50%,75%,100%), содержащие приблизительно равное количество наблюдений. 
        \nПо сути, это то же самое, что и перцентиль. То есть нижний квартиль - 25 перцентиль, а верхний квартиль - 75 перцентиль
        ''')







        with st.form(key='box_plot'):



            ax_x = st.selectbox('Выберите, что будет по горизонтали', df.columns.tolist())
            ax_y = st.selectbox('Выберите, что будет по вертикали', df.columns.tolist())
            button_box = st.form_submit_button('Построить')
            if button_box:
                box = px.box(df, x=ax_x, y=ax_y)
                st.plotly_chart(box, use_container_width=True)
    

    with st.expander('График формы распределения BarPlot'):

        st.write(""" У нас есть категориальная переменная и её цифровое значение. Барплот аггрегирует данные по значениям категориальной переменной и применяет определённую функцию к значениям соответсвующих групп цифровой переменной. По умолчанию эта функция — среднее.""")

        with st.form(key='Bar_plot'):
            
            ax_x = st.selectbox('Выберите, что будет по горизонтали', df.columns.tolist())
            ax_y = st.selectbox('Выберите, что будет по вертикали', df.columns.tolist())
            fig = plt.Figure()
            ax = fig.subplots()
            sns.barplot(
                x=df[ax_x], y=df[ax_y], color="goldenrod", ax = ax
            )
            ax.set_xlabel("day")
            ax.set_ylabel("total_bill")
            button_box = st.form_submit_button('Построить')
            if button_box:

                st.pyplot(fig)
