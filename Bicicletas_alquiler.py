bicicletas_disponibles = ["Bicicleta 1", "Bicicleta 2", "Bicicleta 3", "Bicicleta 4"]
usuarios = {}

# Función para registrar un usuario
def registrar_usuario():
    tarjeta = input("Ingrese el número de tarjeta: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo: ")
    
    usuarios[tarjeta] = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "bicicleta_prestada": None,
        "origen": None,
        "destino": None
    }

def prestar_bicicleta():
    tarjeta = input("Ingrese el número de tarjeta: ")
    
    if tarjeta in usuarios:
        if usuarios[tarjeta]["bicicleta_prestada"] is None:
            if bicicletas_disponibles:
                bicicleta = bicicletas_disponibles.pop()
                origen = input("Ingrese el origen: ")
                destino = input("Ingrese el destino: ")
                usuarios[tarjeta]["bicicleta_prestada"] = bicicleta
                usuarios[tarjeta]["origen"] = origen
                usuarios[tarjeta]["destino"] = destino
                print(f"Bicicleta prestada: {bicicleta}")
            else:
                print("Todas las bicicletas están prestadas.")
        else:
            print("Este usuario ya tiene una bicicleta prestada.")
    else:
        print("Usuario no registrado.")

def devolver_bicicleta():
    tarjeta = input("Ingrese el número de tarjeta: ")
    
    if tarjeta in usuarios:
        bicicleta_prestada = usuarios[tarjeta]["bicicleta_prestada"]
        if bicicleta_prestada is not None:
            origen = usuarios[tarjeta]["origen"]
            destino = usuarios[tarjeta]["destino"]
            bicicletas_disponibles.append(bicicleta_prestada)
            usuarios[tarjeta]["bicicleta_prestada"] = None
            usuarios[tarjeta]["origen"] = None
            usuarios[tarjeta]["destino"] = None
            print(f"Bicicleta devuelta: {bicicleta_prestada}")
            print(f"Origen: {origen}")
            print(f"Destino: {destino}")
        else:
            print("Este usuario no tiene una bicicleta prestada.")
    else:
        print("Usuario no registrado.")
def mostrar_bicicletas_prestadas():
    print("Lista de bicicletas prestadas:")
    for tarjeta, usuario in usuarios.items():
        bicicleta_prestada = usuario["bicicleta_prestada"]
        if bicicleta_prestada is not None:
            print(f"Tarjeta: {tarjeta}, Bicicleta: {bicicleta_prestada}")

# Menú principal
while True:
    print("\nMenú:")
    print("1. Registrar usuario")
    print("2. Prestar bicicleta")
    print("3. Devolver bicicleta")
    print("4. Mostrar bicicletas prestadas")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        prestar_bicicleta()
    elif opcion == "3":
        devolver_bicicleta()
    elif opcion == "4":
        mostrar_bicicletas_prestadas()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente de nuevo.")