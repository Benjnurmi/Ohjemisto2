# Chuck Norris -vitsin kertoja

# Tapa 1
import requests

pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()

print(vastaus["value"])



# Tapa 2
import requests
import json

def chuck():

    pyyntö = "https://api.chucknorris.io/jokes/random"
    vastaus = requests.get(pyyntö)
    j = json.loads(vastaus.text)
    
    print(j["value"])

chuck()



# Tapa 3
"""import requests
import json

pyynto = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=1)
            print(a["value"])
    elif vastaus.status_code<200:
        print ("Hakua ei voitu suorittaa.")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")"""
