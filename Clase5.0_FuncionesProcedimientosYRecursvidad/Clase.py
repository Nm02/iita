# def Saludar(nombre, mensaje="¿Como estas?"):
#     print(f"hola {nombre},{mensaje}")

# Saludar("Nicolas","¿Hiciste el tp?")
# Saludar("Nicolas")

# def EsPrimo(numero):
#     for i in range(numero-1,1,-1):
#         if numero%i == 0:
#             return False
#     return True


# Ingreso = int(input("Ingrese un numero: "))
# for i in range(2,Ingreso+1):
#     if EsPrimo(i):
#         print(i)


"""Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si 
la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se 
considerará válida si contiene el símbolo "@"."""

def MailValido(Mail):
    if "@" in Mail:
        return True
    else:
        return False
    
def MailValidoSegundaForma(Mail):
    posicion=Mail.find("@")
    if posicion==-1:
        return False
    else:
        return True
    
# Mail=input("ingrese su mail:")
# # print(MailValido(Mail))
# print(MailValidoSegundaForma(Mail))


"""3. Definir una función
que muestre el factorial de un número"""
def factorial(numero):
    factorial=1
    while numero>0:
        factorial=factorial*numero
        numero=numero-1
    return factorial

def factorialRecursivo(numero):
    if numero==0 or numero==1:
        return 1
    else:
        return numero*factorialRecursivo(numero)
print(factorialRecursivo(5))

5*4*3*2*1
4*3*2*1

