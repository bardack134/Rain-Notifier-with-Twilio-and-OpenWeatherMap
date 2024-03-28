import requests


API_KEY="a4268efc4142f9eb0c24aecdb6f90603"
MY_LATITUDE=43.057455
MY_LONGITUDE=43.057455


# #parametros que pasare a la api, en formatio diccionario
weather_parameters={"lat":MY_LATITUDE,
            "lon":MY_LONGITUDE,
            "appid":API_KEY,
            "units":"metric"
            }


#API de donde obtendre la informacion del clima, del website https://openweathermap.org/forecast5
weather_api="https://api.openweathermap.org/data/2.5/forecast"


# Le paso los parametros, esta informacion se consigue en la documentacion de la api
response=requests.get(weather_api, params=weather_parameters)


#imprimimos la http response code, un numero que indica el status (200 is ok....etc)
print(response.status_code)


#convertimos la respuesta tipo formaqto json
json_response=response.json()


print(json_response)