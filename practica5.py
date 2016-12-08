from datetime import  datetime
from sys import getsizeof

anio_nacimiento = input("Ingrese su año de nacimiento: ")
print(datetime.now().year - int(anio_nacimiento))

print(getsizeof(anio_nacimiento))