import requests
from constants import*



# #parametros que pasare a la api, en formatio diccionario
weather_parameters={"lat":MY_LATITUDE,
            "lon":MY_LONGITUDE,
            "appid":API_KEY,
            "units":"metric",
            "cnt":5 #para los primeros 5 chequeos del clima,  1 dia tiene 8 chequeos, en total son 40 chequeos que son en total 5 dias
            }


#API de donde obtendre la informacion del clima, del website https://openweathermap.org/forecast5
weather_api="https://api.openweathermap.org/data/2.5/forecast"


# Le paso los parametros, esta informacion se consigue en la documentacion de la api
response=requests.get(weather_api, params=weather_parameters)


#imprimimos la http response code, un numero que indica el status (200 is ok....etc)
print(response.status_code)


# returns an HTTPError object if an error has occurred during the process.
print(response.raise_for_status())


#convertimos la respuesta tipo formaqto json
json_response=response.json()


print(json_response)