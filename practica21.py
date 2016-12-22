OPCIONES = (
    ("Opcion 1", 1),
    ("Opcion 2", 2)
)

#print(OPCIONES[0][1])
##OPCIONES[0][1] = 10


a = ("Opcion 1", 1)
la = list(a)
la[1] = 2
a = tuple(la)
print(a)


