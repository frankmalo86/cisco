# import requests
# import time
# import datetime
#
#
# response = requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-05-20')
# data = response.text
#
#
# from ubidots import ApiClient
#
# api = ApiClient(token='VaECzrPu75Kx0JvRaIF042z5gexlcI')
# my_variable = api.get_variable('5851fae776254275cad11613')
#
#
# eventos = data.split("\n")
# eventos.reverse()
# for indice in range(len(eventos)):
#     if indice > 0:
#         evento = eventos[indice]
#         datos = evento.split("|")
#         if len(datos) == 13 and  datos[12].lower().find("ecuador") >0:
#             if datos[10]:
#                 fecha_str = datos[1]
#                 fecha_str = fecha_str[:fecha_str.index(".")]
#                 fecha_timestamp = time.mktime(datetime.datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S").timetuple())
#                 fecha_timestamp -= (5*60*60)
#                 #print (fecha_timestamp)
#                 magnitud = float(datos[10])
#                 lat = float(datos[2])
#                 lon = float(datos[3])
#                 new_value = my_variable.save_value({'value': magnitud, 'timestamp': int(fecha_timestamp * 1e3), "context":{"lat":lat, "lng":lon}})
#                 time.sleep(2)

###################################################################################################################

# l = [[1,2,"test"], [9,7,"Frank"], [7,2, "hola"]]
# l.sort(key=lambda x: x[2])
# print(l)

###################################################################################################################

# import json, requests
# url = "http://things.ubidots.com/api/v1.6/variables/5851fae776254275cad11613/values"
#
# params = dict(
#     token='VaECzrPu75Kx0JvRaIF042z5gexlcI',
# )
#
# response = requests.get(url=url, params=params)
# print(response.text)
# data = json.loads(response.text)
# print(data['results'][0]["value"])
#
# del data['results']
# print (data)
#
# data["resultados"] = "una nueva lista"
# print(data)


# dic = {"uno":1, "dos":2}
# for item in dic:
#     print(item)
#     print(dic[item])
# print("########################################")
# for item in dic.keys():
#     print(item)
# print("########################################")
# print(dic.items())
# for k,v in dic.items():
#     print(k, v)
#
# print("########################################")
#
# for item in dic.values():
#     print(item)



