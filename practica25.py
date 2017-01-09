import requests
import json

url = "http://earthquake.usgs.gov/fdsnws/event/1/query"
g_format = "text"

def validar_magnitud(func):
    def envoltura(evento):
        datos = func(evento)
        if len(datos)!= 13 or datos[10] == '':
            return None
        else:
            return datos
    return envoltura

def preparar_url(format = "text", **kwargs):
    global url
    global g_format

    g_format = format
    url += "?format=%s"%format
    argumentos = ""
    for k,v in kwargs.items():
        argumentos += "&%s=%s" % (k,v)
    url += argumentos

def realizar_requerimiento():
    response = requests.get(url)
    if g_format == "text":
        return response.text
    if g_format == "geojson":
        return json.loads(response.text)


def obtener_eventos(base_completa, q=None):
    if isinstance(base_completa, str):
        eventos = base_completa.split("\n")
        resultado = []
        count = 0
        for evento in eventos:
            if q is not None and evento.lower().find(q.lower()) >= 0:
                resultado.append(evento)
            else:
                if count != 0:
                    resultado.append(evento)
            count+=1
        return resultado

    if isinstance(base_completa, dict):
        resultado = []
        for evento in base_completa["features"]:
            if q is not None and evento["properties"]["place"].lower().find(q.lower()) >= 0:
                l = ["","",str(evento["geometry"]["coordinates"][0]),str(evento["geometry"]["coordinates"][1]),"","","","","","",str(evento["properties"]["mag"]),"",str(evento["properties"]["place"]),""]
                resultado.append("|".join(l))
        return resultado

@validar_magnitud
def obtener_datos(evento):
    return evento.split("|")

def presentacion_datos(datos):
    for dato in datos:
        plantilla = """
*********************************************
magnitud = %s
lugar = %s
longitud = %s
latitud = %s
*********************************************
""" % (dato[10], dato[12], dato[3], dato[2])
        print(plantilla)

#############################################################################

preparar_url( format="geojson", starttime="2016-04-15", endtime="2016-04-30",
             orderby = "magnitude", limit = "20")
base = realizar_requerimiento()
eventos = obtener_eventos(base, q="ecuador")
data = []
for evento in eventos:
    lista = obtener_datos(evento)
    if lista is not None:
        data.append(lista)

presentacion_datos(data)

