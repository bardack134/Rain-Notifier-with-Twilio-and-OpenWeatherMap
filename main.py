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


#list donde se guardaran los weather id
weather_id_list=[]


#TODO:CHEQUIAAR LA CONDICION DEL CLIMA PARA LAS SGTS HORAS DEL DIA
#weather_list es una lista de diccionarios
weather_list=json_response["list"]


#itirenamos sobre la lista de diccionarios
for item in weather_list:
    # print(item)
    #item viene siendo cada diccionario de la lista de diccionarios, accedemos al valor 'weather' de cada diccionario y lo guardamos en una variable
    # print(type(item['weather']))
    item_weather=item['weather']
    # print(item_weather)
    
    
    #item weather es una lista de diccionarios, itirenamos sobre esta segunda lista
    for item_2 in item_weather:
        
        #item_2 representa un diccionario de la lista de diccionarios, accedemos al valor 'id', que es el que nos interesa 
        weather_id=item_2['id']
        
        #agregamos el valor a la lista weather_id_list
        weather_id_list.append(weather_id)
    
print(weather_id_list)
   



       
    