import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}

while True:
    x = int(input(f'\tВведите номер страницы (1 - 100): '))
    print('-----------------------------------------------')
    if 1 <= x and x <= 100:
        url = f"https://api.hh.ru/vacancies?page={x - 1}"
        response = requests.get(url, headers=headers)
        data = response.json()

        for i in range(0, 20):
            print(f'\t\tВАКАНСИЯ {i + 1}')
            print('-----------------------------------------------')
            print(f'Вакансия: {data['items'][i]['name']}')
            print(f'Работадатель: {data['items'][i]['employer']['name']}')
            if data['items'][i]['salary'] == None:
                print('Зарплата: не указана')
            elif data['items'][i]['salary']['from'] == None:
                print(f'Зарплата({data['items'][i]['salary']['currency']}): до {data['items'][i]['salary']['to']}')
            elif data['items'][i]['salary']['to'] == None:
                print(f'Зарплата({data['items'][i]['salary']['currency']}): от {data['items'][i]['salary']['from']}')
            else:
                print(f'Зарплата({data['items'][i]['salary']['currency']}): от {data['items'][i]['salary']['from']} до {data['items'][i]['salary']['to']}')
            print(f'Опыт работы: {data['items'][i]['experience']['name']}')
            print(f'Локация: {data['items'][i]['area']['name']}')
            print(f'Ссылка на вакансию: {data['items'][i]['alternate_url']}')
            print(f'-----------------------------------------------\n')
    else:
        print("Такой страницы не существует")
        print(f'-----------------------------------------------\n')