# las listas son estructuras de datos luneales
# Se crean usando brackes ej: my_list = []
# Las listas son ordenadas (orden de insersion)
# Emplea metodos para manipular los items de la misma.
# Como los arrays la primera posicion inicia en 0
# Permite items duplicados
# las listas son mutables, es decir podemos agregar, actualizar o remover items
# Puede contener distintos tipos de datos


nombres = ["Juan", "Pepito", "Maria", "Lisa"]

#El metodo len valida el tamaño de la lista.
print(len(nombres))
print(type(nombres))

listaDatos = ["Pepito", "Perez", 1000100100, 1.80, True]
#print(listaDatos[2])
print(f"El numero de doc es: {listaDatos[2]}")

#Slicing de datos
print(listaDatos[0:2])
print(listaDatos[1:4])
print(listaDatos[4])
print(listaDatos[2])

