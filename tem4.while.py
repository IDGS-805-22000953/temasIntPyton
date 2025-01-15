
t = 0
while t<=10:
    print(t)
    t+=1

    print("Dame un numero para hacer una tabla de multiplicar")
tabla=input("Numero de la tabla:")
x=0
while x<=9:
    x=x+1
    resultado=int(tabla)*x
    print(resultado)