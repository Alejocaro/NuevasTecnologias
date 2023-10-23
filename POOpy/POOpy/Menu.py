from Persona import Persona
from Empleado import Empleado

empleado = Empleado


def menuApp():

    print("Inicialice con 1")
    init = int(input("Escriba 1"))

    while init != 0:
        print("Seleccione 1 para Registrar empleado\n"
              "Seleccione 2 para Iniciar sesión\n"
              "Seleccione 3 para salir")

        opc = int(input("Ingrese una opcion"))
        if opc == 1:
            empleado.registrar_usuario()
        elif opc == 2:
            empleado.iniciar_sesion()
            empleado.appEmpleado(empleado.iniciar_sesion, empleado.imprimir_registro())
        elif opc == 3:
            print("Salir")
            init = 0

empleado = Empleado(id= None,
                    nombre= None,
                    apellido= None,
                    correo= None,
                    contraseña= None,
                    cargo= None,
                    salario= None,
                    tipo_contrato= None)
menuApp()