import requests

api_key = "16b04170c2be05136f75b3539aafc518"
while True:
    city = input('Введите свой город: ')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()
    #print(data)
    try:
        print('-------------------------------')
        print(f'Температура: {str(data['main']['temp'] - 273.15)[:5]} °C')
        print(f'Влажность: {(data["main"]['humidity'])} %')
        print(f'Давление: {str((data)['main']['pressure'] * 0.750062)[:3]} мм рт. ст.')
        print(f'-------------------------------\n')
    except KeyError:
        print("Проверьте правильно ли написан город")
        print(f'-------------------------------\n')
