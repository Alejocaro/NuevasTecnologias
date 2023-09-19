#Los diccionarios permiten tener clave: valor
#Son cambiables
#no permiten duplicados
#Desde python 3.7 son ordenados
#Permiten agregar, remover items
#Son oterables
#Poseen distintos metodos para manipular los datos 
#Admite disitintos tipos de datos

usuario = {"Nombre": "Alejandro","Apellido": "Caro", "Edad": 25}

print(usuario)
#Imprime las claves
print(usuario.keys())
#Imprime los valores
print(usuario.values())
#Para conocer el tamañao del diccionario usamos el metodo len
print(len(usuario))
print(type(usuario))

#Cuando queremos buscar in item especifico podemos usar get()

print(usuario.get("Nombre"))
print(usuario["Nombre"])

#Podemos agregar un nuevo item

usuario["correo"]="alejandroc818@gmail.com"
print(usuario.keys())
print(usuario.get("correo"))

#Para remover

usuario.pop("Nombre")
print(usuario.keys())
usuario.popitem()
print(usuario.keys())
del usuario["Edad"]
print(usuario.keys())


#Para recorrer el direccionario podemos elegir enre recorrer las claves, recorrer los valores o recorrer ambos

#ambos

for x,y in usuario.items():
    print(x,y)
    
#Recorrer claves
for x in usuario.keys():
    print(x)
    
#recorrer valores 
for y in usuario.values():
    print(y)
    
    
#Podemos tener un diccionario de diccionarios

usuario = {usuario1:{"Nombre": "Carolina","Edad": 12}, "usuario2":
    {"Nombre": "Maria", "Edad": 15},"usuario3":{"Nombre": "Camilo", "edad": 18}}


estudiante1 = {"nota1":4.2, "notas":4.3}
estudiante2 = {"nota1":4.4, "notas":4.3}
estudiante3 = {"nota1":4.5, "notas":4.1}

estudiantes = {
    "estudiantes1":estudiante1,
    "estudiantes2":estudiante2,
    "estudiantes3":estudiante3
}
print(estudiantes["estudiantes2"]["nota2"])