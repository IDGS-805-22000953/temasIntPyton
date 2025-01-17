import math

print("Este programa calcula la distancia entre dos puntos en una cordenada X y Y")
punto1_x = int (input("ingresa el valor x de el punto numero 1: "))
punto1_y = int (input("ingresa el valor y de el punto numero 1: "))

punto2_x = int (input("ingresa el valor x de el punto numero 2: "))
punto2_y = int (input("ingresa el valor y de el punto numero 2: "))

#commit 16 archivos
#sqrt (x2-x1)^2 + (y2-y1)^2

puntos_x = punto2_x - punto1_x
punto_xG = puntos_x**2

puntos_y = punto2_y - punto1_y
punto_yG = puntos_y**2

suma = punto_xG + punto_yG
raiz = math.sqrt(suma)

print(f"La distancia entre los puntos {punto1_x},{punto1_y} y {punto2_x},{punto2_y} es de {raiz}")