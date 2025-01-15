
import os
def funcion1():
    os.system('cls')
    print("Dame dos numeros: ")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    res=num1+num2
    print(f"La suma de {num1} + {num2} es {res}")

def funcion2():
        print("Hola soy la funcion 2")


def run():
     os.system('cls')
     print("Menu de opciones")
     print("Suma dos numeros")
     print("Otra opcion")
     print("Salir")
     opcion = int(input("Ingrese una opcion: "))
     if opcion == 1:
           funcion1()
     if opcion == 2:
         funcion2()

if __name__ == "__main__":
     run()

"""
op=int(input("Numero: "))
if op==1:
    funcion1()
else:
    funcion2()
"""