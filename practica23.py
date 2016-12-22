import  requests
import json

url = "http://things.ubidots.com/api/v1.6/variables/5851fae776254275cad11613/values"

parametros = {"format":"json", "token":"VaECzrPu75Kx0JvRaIF042z5gexlcI"}
response = requests.get(url=url, params=parametros)

datos = json.loads(response.text)
for resultado in datos["results"]:
    print("valor", resultado["value"])
    print("Creado en", resultado["created_at"])
    for k,v in resultado["context"].items():
        print(k, v)
    print("###########################################")

