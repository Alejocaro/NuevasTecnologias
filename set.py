#Los conjuntos son inmutables
#Son desordenados, quiere decir que cuando se llama no se tiene certeza el orden que los mostrará
#No son indexables
#No permite duplicados 

vocales ={"a","e","i","o","u"}

print(len(vocales))

print(type(vocales))

#Para recorrer los conjuntos se usa in

for i in vocales:
    print(vocales)
    
#Los diccionarios tienen el metodo add y el metodo remove

vocales.add("@")
for i in vocales:
    print(vocales)
    
#Podemos remover
vocales.remove("@")
for i in vocales:
    print(vocales)
    