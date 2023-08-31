import random 

vidas= 5

puntos= 0

#Si sale cero pierde una vida
#Si se genera cualquier otro numero dentro de un rango establecido, gano puntos

while vidas !=0:
    
    num = random.randint(0,9)
    
    if num != 0:
        puntos+=1
        print("Tienes ",puntos, "Puntos")
    else:
        vidas-=1
        print("Te quedan ", vidas, "vidas")