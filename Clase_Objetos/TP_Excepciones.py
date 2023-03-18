"""Para cada uno de los siguientes casos, distinga el tipo de error y describa por qué se da:
- print(5/0)
- print 3
- int(‘hola’)
- res = 3 + ‘5’
"""


"""Suma: Un problema común cuando se pide que el usuario ingrese valores numéricos es el
ingreso de texto en vez de números. Cuando intente convertir el input a un int, se
encontrará con un ValueError. Escriba una función suma() que pida dos números, los sume
y muestre el resultado. Capture el ValueError si se da, y muestre un mensaje de error. """
# def Suma_Dos_Numeros():
#     try:
#         numero1=int(input("ingrese el primer numero para sumar: "))
#         numero2=int(input("ingrese el segundo numero para sumar: "))
#         return numero1+numero2
#     except ValueError as error:
#         return error
    
# print(Suma_Dos_Numeros())

"""Suma robusta: Encierre su código del ejercicio anterior en un ciclo while para que el
usuario pueda seguir ingresando números incluso si se equivoca."""
# def Suma_Dos_Numeros():
#     while True:
#         try:
#             numero1=int(input("ingrese el primer numero para sumar: "))
#         except ValueError as error:
#             print(error)
#         else:
#             break
#     while True:
#         try:
#             numero2=int(input("ingrese el segundo numero para sumar: "))
#         except ValueError as error:
#             print(error)
#         else:
#             break
#     return numero1+numero2

# print(Suma_Dos_Numeros())

"""Perros y gatos: Cree dos archivos, gatos.txt y perros.txt. Guarde al menos tres nombres de
gato en el primer archivo y al menos tres de perro en el segundo. Escriba un programa que
intente leer estos archivos y muestre su contenido en la pantalla. Encierre su codigo en un
bloque try-except de manera que se capture el error FileNotFoundError y se muestre un
mensaje de ayuda si algún archivo no existe. Mueva alguno de los archivos a otro
directorio en su sistema y pruebe el bloque except.
"""
# def Leer_Archivo():
#     try:
#         Archivo=open("C:\\Users\\109\\Documents\\nico\\iita\\Clase_Objetos\\Gatos.txt","r")
#         Lineas=Archivo.readlines()
#         for linea in Lineas:
#             print(linea.replace("\n",""))
#         Archivo.close()
#         Archivo=open("C:\\Users\\109\\Documents\\nico\\iita\\Clase_Objetos\\Perros.txt","r")
#         Lineas=Archivo.readlines()
#         for linea in Lineas:
#             print(linea)
#         Archivo.close()

#     except FileNotFoundError as error:
#         print(error)

# Leer_Archivo()

"""Perros y gatos silenciosos: Modifique su bloque except del ejercicio anterior para que falle
silenciosamente (no de muestras de que se produjo un error) si falta cualquiera de los
archivos"""
# def Leer_Archivo():
#     try:
#         Archivo=open("C:\\Users\\109\\Documents\\nico\\iita\\Clase_Objetos\\Gatos.txt","r")
#         Lineas=Archivo.readlines()
#         for linea in Lineas:
#             print(linea)
#         Archivo.close()
#         Archivo=open("C:\\Users\\109\\Documents\\nico\\iita\\Clase_Objetos\\Perros.txt","r")
#         Lineas=Archivo.readlines()
#         for linea in Lineas:
#             print(linea)
#         Archivo.close()

#     except FileNotFoundError as error:
#         pass

# Leer_Archivo()

"""Número favorito: Escriba un programa que lea un archivo
numeros_favoritos.txt, que contiene los números favoritos del usuario, y los muestre en
pantalla. Si el archivo no existe, pida al usuario que los ingrese y almacénelos en el archivo.
Asegúrese de que ambos casos funcionan bien"""
# def Numeros_Favoritos():
#     try:
#         Archivo=open("C:\\Users\\109\\Documents\\nico\\iita\\Clase_Objetos\\Numeros_Favoritos.txt","r")
#         Lineas=Archivo.readlines()
#         for linea in Lineas:
#             print(linea)
#         Archivo.close()
#     except FileNotFoundError:
#         Archivo=open("C:\\Users\\109\\Documents\\nico\\iita\\Clase_Objetos\\Numeros_Favoritos.txt","w")
#         while True:
#             try:
#                 numero=int(input("ingrese un numero favorito: "))
#                 Archivo.write(str(numero)+"\n")

#             except ValueError:
#                 print("Debe ingresar un numero.")
#             else:
#                 Seguir=input("Ingrese salir para salir: ")
#                 if Seguir=="salir":
#                     break
#         Archivo.close()

# Numeros_Favoritos()

"""Escriba un programa que el archivo con el texto que encontró y determine cuántas veces la
palabra “el” ocurre en el texto."""
# def Contar_palabras(palabra):
#     try:
#         Archivo=open("C:\\Users\\109\\Documents\\nico\\iita\\Clase_Objetos\\Texto.txt","r")
#         Lineas=Archivo.readlines()
#         contador=0
#         for linea in Lineas:
#             contador+=linea.lower().count(palabra)
#         Archivo.close()
#         print(f"la palabra se repite {contador} veces.")

#     except FileNotFoundError as error:
#         print("no encontre el archivo.")

# Contar_palabras("el")