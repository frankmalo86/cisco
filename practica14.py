import requests
import time


response = requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-04-20')
data = response.text


from ubidots import ApiClient

api = ApiClient(token='VaECzrPu75Kx0JvRaIF042z5gexlcI')
my_variable = api.get_variable('5851fae776254275cad11613')


eventos = data.split("\n")
for indice in range(len(eventos)):
    if indice > 0:
        evento = eventos[indice]
        datos = evento.split("|")
        if len(datos) == 13 and  datos[12].lower().find("ecuador"):
            if datos[10] is not "":
                magnitud = float(datos[10])
                new_value = my_variable.save_value({'value': magnitud})
                time.sleep(2)


