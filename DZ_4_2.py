import pandas as pd
import numpy as np

df = pd.read_csv('steam.csv') #чтение файла

def Game_input(column, input_data, df_pr):
    if input_data == '':
        df_new = df_pr.copy()  # Если пользователь не вводит ничего, копируем весь список
        print('Вы выбрали всю категорию')
    else:
        input_data_arr = input_data.split()
        for j in range(len(input_data_arr)):
            for i in range(len(df_pr)):
                if input_data_arr[j] in df_pr[column][i]:
                    df_new = df_new.append(df_pr.loc[i], ignore_index=True)
    if (df_new.empty):
        print('К сожалению по вашим параметрам ничего не найдено, обратитесь позже')
        input()
        raise SystemExit
    return df_new

def Unique_in_column(column):
    df_f = df[column]
    app = []
    for i in range(len(df_f)):
        app.append(df_f[i].split(sep=";"))
    app_unique = []
    for i in range(len(app)):
        for j in range(len(app[i])):
            if (app[i][j] in app_unique):
                app[i][j]
            else:
                app_unique.append(app[i][j])
    return app_unique

df_columns = df.columns
df_new = pd.DataFrame(columns=df_columns)

#df_final = pd.DataFrame(columns = df.columns) #создание итогового датафрейма
#Жанр
print('Введите интересуюшие вас жанры из представленных ниже:')
un = Unique_in_column('genres')
print(un)
_genre = input() #Прием названия жанра с клавиатуры
df_final = Game_input('genres', _genre, df)

#Категория
print('Введите интересуюшие вас категории из представленных ниже:')
un = Unique_in_column('categories')
print(un)
_category = input() #Прием названия категории с клавиатуры
df_final = Game_input('categories', _category, df_final)

#Издатель
print('Введите интересуюшего разработчика из представленных ниже:')
un = Unique_in_column('developer')
print(un)
_developer = input() #Прием названия категории с клавиатуры
df_final = Game_input('developer', _developer, df_final)

#Возраст
print('Введите допустимый возраст из представленных ниже:')
un = df_final['required_age'].unique()#Unique_in_column('required_age')
print(un)
_required_age = input() #Прием названия категории с клавиатуры
df_final = df_final[df_final.required_age == int(_required_age)]

#год выпуска игры
dt_release = pd.to_datetime(df_final['release_date']).dt.year
print('Введите год, после которого выпущена игра:')
_release_date = input() #прием года с клавиатуры
df_final = df_final[pd.to_datetime(df_final['release_date']).dt.year >= int(_release_date)].reset_index(drop = True)

#Платформа
print('Введите интересующие платформы:')
un = Unique_in_column('platforms')
print(un)
_platforms = input() #Прием названия платформы с клавиатуры
df_final = Game_input('platforms', _platforms, df_final)

print('Рекомендуемые игры:', df_final['name'])
#Запись в файл
new_file = open('Recomends.txt', 'w')
for i in range(len(df_final)):
    s = df_final['name'][i] #Из-за того, что метод write() не может писать много специсимволов, делаем простой фильтр
    s1 = re.sub('[^A-Za-z0-9 ]', '', s)
    new_file.write(s1+'\n')
new_file.close()
print('Файл с рекомендациями записан, нажмите любую кнопку')
input()
