#listas

list1 = [10,5,3]
list2 = [1,5,2.66,1.70,89.2]
list3 = ["Lunes","Martes","Miercoles"]
list4 = ["Juan", 45, 1.92]

print(type(list1))
print(len(list1))

print (list[0])

x = 0
suma = 0
while x < len(list1):
    suma = suma + list1[x]
    x+=1
    
print(f"La suma es: {suma}")
print(list1)
print(list1[0])
list1.append(100) #Agregar elemento a la lista
print(list1)
print(list1[3])

lista5=[]

for x in range(5):
    valor = int (input("ingresa valor: "))
    lista5.append(valor)
    
print(lista5)
    
    
#Eliminar datos de una lista
print(list1)
list1.pop()
print(list1)
#Delimitar elementos de una lista



"""
Crear un programa pedir una n de numeros y almacenarlos en un arreglo la salida debera ser la siguiente:
Lista completa xxxxxx
Numeros pares de la lista: aaaaaaa
Numeros impares de la lista: nnnnn

"""

listPrueba = []
cantidad = int (input("ingresa valor de la matriz: "))

for x in range(cantidad):
    print(f"Valor en la posicion {x}")
    valor = int (input("ingresa valor: "))
    listPrueba.append(valor)
    
print(listPrueba)

matrizPar = []
matrizImpar = []
print("Numeros pares de la lista:")
for x in range (cantidad):
    doble = listPrueba[x]
    if doble % 2 == 0:
        matrizPar.append(doble)
    else:
        matrizImpar.append(doble)
print(matrizPar)


print("Numeros impares de la lista: ")
print(matrizImpar)






list1.sort() #ordenar lista
print(list1)
list1.reverse()
print(list1)

list1.remove(10)
print(list1) #?

list1.clear()
print(list1) #?












