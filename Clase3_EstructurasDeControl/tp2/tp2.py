
#Pida un número al usuario y determine si es par o impar.
"""numero=int(input("ingrese un numero:"))

if numero%2==0:
    print("es par")
else:
    print("es inpar")"""

# Escriba una cadena if-elif-else que determine el estado de vida de una persona.
#• Si la persona tiene menos de 2 años, muestre un mensaje que diga que es un bebe.
#• Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
#• Si tiene al menos 4, pero menos de 12, muestre que es un niño.
#• Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
#• Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
#• Si tiene 65 o más, muestre que es un anciano. 

"""edad=int(input("ingrese su edad:"))

if edad<2:
    print("eres un bebe")
elif edad==2 or edad<4:
    print("eres un infante")
elif edad==4 or edad<12:
    print("eres un niño")
elif edad==13 or edad<20:
    print("eres un adolecente")
elif edad==20 or edad<65:
    print("eres un adulto")
else: 
    edad>65
    print("eres un anciano")
"""

#Cree un ciclo que nunca termine y ejecútelo. Puede probarlo haciendo que muestre algo en
#pantalla por cada pasada del ciclo. Para finalizarlo, presione Ctrl-C o el comando para detener
#la ejecución correspondiente a su edito

"""x=1

while True:
    print(x)
    x=x+1"""

# Escriba un programa que contenga dos ciclos while anidados que muestre los enteros del 1
#al 100, diez números por línea, como se muestra abajo:


#Resuelva el ejercicio anterior usando solo un ciclo while
"""numero=1
suma=0
while numero<=100:
    print(numero,end=("-"))
    numero=numero+1
    suma=suma+1
    if suma>=10:
        print("\n")
        suma=suma-10   """

numero=1
suma=0
while numero>100:
    print(numero,end=("-"))
    numero=numero+1
    suma=suma+1
    while suma>=10:
        print("\n")
        suma=suma-10
