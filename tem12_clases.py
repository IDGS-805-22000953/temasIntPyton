class OperasBas:
    #Declaracion de propiedas
    num1 = 0
    num2 = 0
    res = 0
    #Declaracion del constructor de la clase
    def __init__(self, a, b):
        self.num1=a
        self.num2=b
    #Declaracion de los metodos de clase
    def sum(self):
        self.res=self.num1+self.num2
        print(f"La salida es: {self.res}")
        
def main():
    obj = OperasBas(3,4)
    obj.sum()
    
if __name__ == "__main__":
    main()
        