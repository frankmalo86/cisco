datos = "usuario\contraseña\correo"
datos = "frmalo\\123456\\frmalo@espol.edu.ec"
print(datos)
print (len(datos))
print("total de back-slash:", datos.count("\\"))

usuario = datos[:datos.find("\\")]
print(usuario)

inicio = datos.find("\\") + 1
posi = datos.find("\\", inicio)
correo = datos[posi + 1:]
print(correo)

print(correo.capitalize())
print(correo.endswith("ec"))
print(correo.startswith("fmalo"))

print(correo.islower())
print(correo.isupper())

print(correo.upper())
print(correo.lower())

data = "á0001111estos0 son0 mis0 datos111000000á"
data_limpia = data.strip("á").strip("0").strip("1")
print(data_limpia)

data_limpia = data_limpia.replace("0", " ").replace("  ", " ")
print(data_limpia)

# prueba = "ImpresiÃ³n Vendedores"
# # if "Ã³" in  prueba:
# #     prueba = prueba.replace("Ã³", "ó")
#
# print(prueba)
# print(prueba.replace("Ã³", "ó"))

print(datos.split("\\"))


