import re

#Чтение файла
with open('aristotle.txt', encoding = 'utf-8-sig') as file:
    array = [row.strip() for row in file]

# расчет количества знаков
cnt_file = 0
for i in range(len(array)):
    cnt_file += len(array[i])

# расчет количества знаков без пробелов
array_no_space = []  # новый массив
cnt_file_no_space = 0
for i in range(len(array)):
    array_no_space.append(array[i].replace(" ", ""))  # удаляем пробелы в новом массиве
    cnt_file_no_space += len(array_no_space[i])

# расчет количества символов без знаков препинания
array_no_sign = []  # новый массив
cnt_file_no_sign = 0
for i in range(len(array)):
    array_no_sign.append(re.sub(r'[^\w\s]', '', array[i]))  # удаляем знаки препинания в новом массиве
    cnt_file_no_sign += len(array_no_sign[i])

# расчет количества слов в тексте
array_words = []
cnt_file_words = 0
for i in range(len(array_no_sign)):
    array_words.append(array_no_sign[i].split())
    cnt_file_words += len(array_words[i])

# расчет количества предложений
cnt_sentences = 0
for i in range(len(array)):
    cnt_sentences += sum(array[i].count(x) for x in ('^.!?'))

print('Количество символов = ' + str(cnt_file))
print('Количество символов без пробелов = ' + str(cnt_file_no_space))
print('Количество символов без знаков препнания = ' + str(cnt_file_no_sign))
print('Количество слов в тексте = ' + str(cnt_file_words))
print('Количество предложений в тексте = ' + str(cnt_sentences))
input()