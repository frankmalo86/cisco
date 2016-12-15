# import re
#
# patron = "^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
#
#
# valor = "http://www.google.com.ec"
#
# if re.match(patron, valor):
#     print ("Dirección Web valida")
# else:
#     print("Dirección Web no valida")
#
#
#
# ################################################################################
#
#
# patron = "^(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
# valor = "255.168.1.1"
#
# if re.match(patron, valor):
#     print ("Dirección ip valida")
# else:
#     print("Dirección ip no valida")
#
#
# ################################################################################
#
#
# patron = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# valor = "fmalo@espol.edu.ec"
#
# if re.match(patron, valor):
#     print ("Dirección mail valida")
# else:
#     print("Dirección mail no valida")
#
# ################################################################################

edad = 50

if  10 > edad > 1 :
    print ("Niñez")
elif 18 > edad > 11:
    print ("Adolosencia")
elif 65 > edad > 19:
    print ("Madurez")
else:
    print ("Vejez")
