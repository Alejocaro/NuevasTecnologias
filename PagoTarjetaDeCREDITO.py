#Reciban por consola el valor de una compra
#Que puedan Ingresar el numero de cuotas 
#Calcular el valor de la cuota
#Usanso while queremos que imprima el plan de pago y le mueste el cupo liberado con cada pago  


valorcompra = float(input("Ingrese el valor de la compra: "))
numerocuotas = int(input("Ingrese el número de cuotas: "))
valorcuota = valorcompra / numerocuotas
cupodisponible = valorcompra

print("\nPlan de Pago:")
cuotaactual = 1
while cuotaactual <= numerocuotas:
    cupodisponible -= valorcuota
    print("Cuota", cuotaactual, "de", numerocuotas, ": $", (valorcuota), "(Cupo Liberado: $", (cupodisponible), ")")
    cuotaactual += 1
print("¡Compra pagada por completo!")
