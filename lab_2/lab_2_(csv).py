from csv import reader


# 1 подзадание (Вывести количество записей, у которых в поле Название строка длиннее 30 символов)

def cnt(table):
    cnt = 0
    for row in table:
        if len(row[1]) > 30:
            cnt += 1
    print(f'Кол-во книг у которых в названии больше 30 символов: {cnt}')


with open("books-en.csv", "r") as csvfile:
    table = reader(csvfile, delimiter=";")
    cnt(table)


# 2 подзадание (Реализовать поиск книги по автору,
# использовать ограничение на выдачу в зависимости от варианта (до 150 рублей))

# для поиска без учета регистра
def register(string, author):
    return string.lower().find(author.lower())


def search(table, author):
    title = []
    for row in table:
        if register(row[2], author)!= -1 and float(row[6].replace(',', '.')) < 150:
            title.append(row[1])
    print(f'Книги автора - {author}, ценой до 150:')
    if not(title):
        print(f'\t Поиск не дал результатов')
    for i in title:
        print(f'\t {i}')


while True:
    try:
        with open("books-en.csv", "r") as csvfile:
            table = reader(csvfile, delimiter=";")
            author = input("Введите автора: ")
            search(table, author)
    except FileNotFoundError:
        print('Файл "books-en.csv" не найден')


# 3 подзадание (Реализовать генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей)

def search_pro():
    pass
