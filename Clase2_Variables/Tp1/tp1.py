#Almacene un mensaje en una variable e imprimalo en pantalla.
#Despues cambie el valor del mensaje e imprimalo nuevamente.

nombre="hola"
print(nombre)

#Almacene el nombre de una persona en un variable, imprima un mensaje para esa persona. Por ejemplo
#"Hola Fede, ¿te gustaria aprender a programar?"

nombre="Lucas"
print("hola",nombre,"te gustaria aprender a programar?")

#El numero ocho: Escriba una suma,resta,multiplicacion y division que resulten cada una en el numero ocho.
#Asegurese de utilizzar la funcion print() para ver los resultados en pantalla.Un ejemplo de linea es el 
#siguiente:
print(5+3)
#la salida deberia motrar el numero ocho tantas veces como lineas haya escrito.

suma=(2+6)
print(suma)
resta=(11-3)
print(resta)
mult=(2*4)
print(mult)
div=(40/5)
print(div)



#cree cuatro variables llamadas mi_entero, mi _decimal, mi_string y mi_booleano. Asigne  acada variable un 
#valor del tipo que le corresponda.Luego muestre en pantalla el tipo de cada variable usando la funcion type
#combinanado todo con la funcion print:
#La salida final debería contener las siguientes líneas (no importa el orden):
#<class 'int'>
#<class 'float'>
#<class 'bool'>

mi_entero=20
print(type(mi_entero))

mi_decimal=3,5
print(type(mi_decimal))

mi_string="hola"
print(type(mi_string))

mi_boleano=True
print(type(mi_boleano))

#Escriba un programa que acepte un numero decimal como entrada y lo imprima sin lugares decimales.

numero=int(3.5)
print(numero)

#¿cual es la salida de las siguientes expresiones?
#1 != 2
#Salida:>>>1!=2 True
#True == 1
#Salida:>>>True==1 False
#False != False
#Salida:>>>False!=False True
#False > 0
#Salida:>>>False>0 False
#1.0 < 1
#Salida:>>>1.0<1 False
#“test” == “test”
#Salida:>>>"test"=="test" True
#1.0 >= 1
#Salida:>>>1.0>=1 True

#(Opcional) Escriba un programa que le pida al usuario que ingrese nombre y edad. Luego muestre un mensaje 
#donde le informe el año en que va a cumplir 100.

nombre=input("ingrese un nombre")
print(nombre)

edad=input("ingrese un numero")
print(edad)

mensaje=input("informe el año en que cumplira 100 años")
print(mensaje)

#(Opcional) Escriba un programa que permita convertir una temperatura en Celsius a la escala Farenheit. La 
#fórmula es:

#Fahrenheit = (9.0/5.0) x Celsius + 32

variable=input("ingrese una temperatura en grados celcius")
tingresada=float(variable)
celciusafarenheit=(tingresada)*33.8
print(celciusafarenheit)









      
