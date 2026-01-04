import re


#task_1_Все слова от 3 до 5 букв; все числа больше 3 знаков

file_1 = open('text_1.txt')
list_1 = []
for i in file_1:
    ans = re.findall(r"\b[a-zA-Z]{3,5}\b|\b\d{3,}", i)
    for i in ans:
        list_1.append(i)

print(list_1)

#task_2_Все открывающие теги без повторений

from collections import OrderedDict

with open('text_2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

pattern = r'<([a-zA-Z][a-zA-Z0-9]*)(?:\s+[^>/]*)?>(?!\s*</\1>)'
tags = re.findall(pattern, html_content)
unique_tags = list(OrderedDict.fromkeys(tags))
print("Уникальные открывающие теги (без самозакрывающихся):")
for tag in unique_tags:
    print(f"<{tag}>")

#task_3_Приведите эту базу данных в нормальный вид, расположив данные в вышеуказанном порядке

import csv

big_date = []
file = open("text_3.txt")
file_3 = file.readline()
file_3 = file_3.split(" ")
file_3 = file_3[0:-1]
with open('users_list.csv', 'w', newline='') as csvfile:
    for i in range(0, len(file_3), 5):
        date = []
        for a in range(5):
            date.append(file_3[i+a])

        date = ' '.join(date)
        # ДАТА
        time = (re.findall(r'\b[0-9]{4}-[0-9]{2}-[0-9]{2}\b', date))[0]
        date = date.replace(f'{time}', '')
        # ССЫЛКА
        url = (re.findall(r'\b[h][t][t][p].*[://].*[/]', date))[0]
        date = date.replace(f'{url}', '')
        # ПОЧТА
        email = (re.findall(r'\b[0-9a-zA-Z]*[@].*[.][a-zA-Z]*\b', date))[0]
        date = date.replace(f'{email}', '')
        # ИНДЕКС
        indx = (re.findall(r'\b\d{1,3}\b', date))[0]
        date = date.replace(f'{indx}', '')
        # ИМЯ
        name = (re.findall(r'\b\w*\b', date))[0]
        date = date.replace(f'{name}', '')
        #==================================================================
        date = [f'{indx}', f'{name}', f'{email}', f'{time}', f'{url}']
        writer = csv.writer(csvfile)
        writer.writerow(date)