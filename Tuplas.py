
#Son inmutables
#Contienen distinitos tipos de datos
#Si se requiere añadir se debe convertir primero en un lista
#Se puede acceder la tupla indicando el indice de la misma, el cual comienza desde cero
#Para recorrer la lista usamos el ciclo for
#Podemos hacer join entre tuplas
#Para reconocer el tamñan usamos la función len(dias_semana)
#Las tuplas permiten duplicar 

dias_semana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(type(dias_semana))
print(dir(dias_semana))
#Funcion len es para medir tamaño de la tupla
print(len(dias_semana))

print(dias_semana[0])
print(dias_semana[1])
print(dias_semana[2])
print(dias_semana[3])
print(dias_semana[4])
print(dias_semana[5])
print(dias_semana[6])

#Podemos hacer slincing indicando el rango que queremos imprimir

print(dias_semana[:6])
print(dias_semana[0:])
print(dias_semana[-1:])

#Para recorrer la tupa usamos for para iterar por los indices 

for i in range(len(dias_semana)):
    print(dias_semana[i])

#Para cambiar algún valor de la tupla o añadir debemos primero convertirla a una lista:

dias_semana_lista = list(dias_semana)

print(type(dias_semana_lista))

dias_semana_lista.append("Festivo")

print(dias_semana_lista[:8])

dias_semana_lista.pop()

print(dias_semana_lista[:8])

dias_semana = tuple (dias_semana_lista)

print(type(dias_semana))