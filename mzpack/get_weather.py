import requests

def get_weather_city(city='Paris'):

    r = requests.get(f'https://goweather.herokuapp.com/weather/{city}')

    if r.status_code == 200:
        print(f'Today in {city} :',str(r.json()['description']), ', temperature: ', str(r.json()['temperature']),', wind: ',str(r.json()['wind']))
        print('Tomorrow :',str(r.json()['forecast'][0]['temperature']),', temperature :', str(r.json()['forecast'][0]['wind']))
    else:
        print('erreur API')
