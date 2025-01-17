from io import open

texto="Una linea con texto \notra linea de texto"

fichero=open('fichero.txt','w')
fichero.write(texto)

cadena2=("\nEsto es otra cadena")
fichero.write(cadena2)
fichero.close()

