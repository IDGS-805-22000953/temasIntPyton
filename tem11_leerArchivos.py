from io import open
fichero=open('fichero.txt','r')
#texto1=fichero.read()
texto1=fichero.readlines()
print(texto1)
#fichero.seek(1)
print(type(texto1))
fichero.close()

"""
for i in texto1:
    print (i)
"""
#print(texto1)