import requests
from constants import*
# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN



# #parametros que pasare a la api, en formatio diccionario
weather_parameters={"lat":MY_LATITUDE,
            "lon":MY_LONGITUDE,
            "appid":api_key,
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
        
        #item_2 representa un diccionario de la lista de diccionarios 'item_weather', accedemos al valor 'id', que es el que nos interesa 
        weather_id=item_2['id']
        
        #agregamos el valor a la lista weather_id_list
        weather_id_list.append(weather_id)
    
print(weather_id_list)
   

#NOTE:(https://openweathermap.org/weather-conditions), mirando la api documentation, encontramos que todos los 'id' menos a 600 representan lluvia


#itirenamos sobre nuestra 'weather_id_list' para comparar nuestros id si son menores o mayores a 600
# will_rain=False
# for id in weather_id_list:
#     if id<600:
#         will_rain=True     

# if will_rain==True:
#     #codigo sacado de la documentacion de twilio
#     # https://www.twilio.com/docs/messaging/tutorials/how-to-send-sms-messages/python#send-an-sms-message-in-python-via-the-rest-api
#     client = Client(account_sid, auth_token)

    
#     message = client.messages \
#         .create(
#             body='It is going to rain today. Remember to bring an umbrella',
#             from_='+14243560102',
#             to=MY_NUMBER
#         )

#     print(message.status)