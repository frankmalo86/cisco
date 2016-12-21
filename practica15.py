lista = ["Frank", "Carlos", "Lourdes", "Ana", "Mercedes",
         "Maria", "Maria Belén", "Fernando"]
lista_2 = [nombre.upper() for nombre in lista if nombre.lower().startswith("m")]
print(lista_2)
