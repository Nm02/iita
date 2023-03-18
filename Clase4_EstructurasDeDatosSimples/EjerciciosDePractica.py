"""Pedir una palabra al usuario, meter los todos sus caracteres
en una lista y mostrarla en pantalla. """

# palabra=input("ingrese una palabra:")
# ListaCaracteres=[]
# for caracter in palabra:
#     ListaCaracteres.append(caracter)
# print(ListaCaracteres)













"""Realizar un programa que inicialice una lista con 10 numeros 
ingresados por el usuario y luego muestre en pantalla 
cual elemento es el menor"""

# ListaNumeros=[]
# for i in range(10):
#     numero=int(input("ingrese un numero:"))
#     ListaNumeros.append(numero)
# menor=ListaNumeros[0]
# for i in range(1,10):
#     if ListaNumeros[i]<menor:
#         menor=ListaNumeros[i]
# print(menor)









"""Crea una tupla que contenga todos los meses de un año. Luego pedir al 
usuario un numero y mostrar que mes representa"""

# Meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
#        "Agosto","Septiembre","Ocutubre","Noviembre","Diciembre")
# numero=int(input("Ingrese un numero del 1 al 12:"))
# print(Meses[numero-1])














"""Crear un programa que pida al ususario un nombre de un alumno, y luego 
muestre la lista de notas de ese alumno. (Usar diccionarios)"""

DiccionarioNotas={"Nicolas":[8,10,7,9],"Sebastian":[7,10,10,7],"Marina":[6,8,10,10]}
nombre=input("ingrese el nombre de un alumno y te diremos sus notas:")
print(DiccionarioNotas[nombre])