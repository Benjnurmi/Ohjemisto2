# OpenWeather

import requests
import json

hakusana = input("Anna paikkakunta: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "http://api.openweathermap.org/geo/1.0/direct?q={city name}&limit={1}&appid={aa5950862092a3aa271d37b0a614f8d4}" + hakusana
pyyntö1 = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={aa5950862092a3aa271d37b0a614f8d4}" + hakusana

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=2))
        for a in json_vastaus:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")

try:
    vastaus = requests.get(pyyntö1)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=2))
        for a in json_vastaus:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")

