﻿# -*- coding: utf-8 -*-

import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(lat, lon, appid):
    url = '{}?lat={}&lon={}&appid={}'.format(base_url, lat, lon, appid)
    response = requests.get(url)
    data = response.json()
    country = data.get('sys')['country']
    name = data.get('name')
    temp = float(data.get('main')['temp']) - 273.15
    wind = data.get('wind')['speed']
    cloud = data.get('weather')[0]['description']
    humidity = data.get('main')['humidity']
    
    message = '''
Country: {}, {}
Temp: {} °C
Wind: {} m/s
Cloudiness: {}
Humidity: {} %
'''.format(name, country, round(temp, 1), wind, cloud, humidity)
    
    return message