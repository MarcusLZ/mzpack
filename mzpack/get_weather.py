from webbrowser import get
import requests

def get_weather_city(city='Paris'):

    r = requests.get(f'https://goweather.herokuapp.com/weather/{city}')

    if r.status_code == 200:
        text_to_print =[f"Today in {city} : {r.json()['description']}, temperature: {r.json()['temperature']}, wind: {r.json()['wind']}"]
        text_to_print.append(f"Tomorrow :{r.json()['forecast'][0]['temperature']}, temperature {r.json()['forecast'][0]['wind']}")
    else:
        text_to_print = ['erreur API']


    return text_to_print


def print_weather(city='Paris'):

    for text in get_weather_city(city):
        print(text,'\n')


print_weather(city='Paris')
