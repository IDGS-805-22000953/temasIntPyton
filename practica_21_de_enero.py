from io import open

class Fichero:
    def __init__(self, compradores, total_boletos, total_global, pagador, metodo_pago):
        self.compradores = compradores
        self.total_boletos = total_boletos
        self.total_global = total_global
        self.pagador = pagador
        self.metodo_pago = metodo_pago

    def guardar_en_archivo(self):
        try:
            with open('comprasCine.txt', 'a') as fichero:
                fichero.write("==== RESUMEN DE COMPRA ====\n")
                fichero.write(f"COMPRADORES: {', '.join(self.compradores)}\n")
                fichero.write(f"TOTAL DE BOLETOS: {self.total_boletos}\n")
                fichero.write(f"TOTAL A PAGAR (GLOBAL): {self.total_global:.2f}\n")
                fichero.write(f"PAGADOR: {self.pagador}\n")
                fichero.write(f"METODO DE PAGO: {self.metodo_pago}\n")
                fichero.write("===========================\n\n")
        except Exception as e:
            print(f"Error {e}")

class Boletos:
    precio_unitario = 12
    
    @staticmethod
    def calcular_total(boletos):
        return boletos * Boletos.precio_unitario


def calcular_descuento_global(total_boletos, total_global):
    if 3 <= total_boletos <= 5:
        return total_global * 0.10
    elif total_boletos >= 6:
        return total_global * 0.15
    return 0

def procesar_compras():
    while True:
        try:
            while True:
                cantidad_personas = int(input("Ingrese la cantidad de personas que van a comprar juntos:\n"))
                confirmacion = input(f"El número de personas a comprar es: {cantidad_personas}. ¿Deseas continuar? (s/n): ").lower()
                if confirmacion == 's':
                    break
                else:
                    print("Por favor, ingrese nuevamente la cantidad de personas.")

            while True:
                total_boletos = int(input(f"Ingrese el número total de boletos (máximo {7 * cantidad_personas}): "))
                if total_boletos <= 7 * cantidad_personas:
                    break
                else:
                    print(f"El número de boletos no puede exceder {7 * cantidad_personas}. Intente nuevamente.")

            compradores = []
            for i in range(cantidad_personas):
                nombre = input(f"Ingrese el nombre de la persona {i + 1}: ").upper()
                compradores.append(nombre)

            total_global = Boletos.calcular_total(total_boletos)
            descuento = calcular_descuento_global(total_boletos, total_global)
            total_global -= descuento
            print(f"Se aplicó un descuento de {descuento:.2f} pesos.")
            print(f"Su total es de {total_global:.2f} pesos")

            pagador = input("Ingrese el nombre de la persona que pagará la compra: ").upper()
            while pagador not in compradores:
                print("El nombre del pagador no coincide con los compradores registrados.")
                pagador = input("Ingrese el nombre de la persona que pagará la compra: ").upper()

            while True:
                respuesta_tarjeta = int(input("¿Desean pagar con tarjeta CINECO? (Aplica un descuento global del 10%)\n1.- Sí\n2.- No\n"))
                if respuesta_tarjeta == 1:
                    total_global -= total_global * 0.10
                    metodo_pago = "Tarjeta CINECO"
                    print("Se aplicó un descuento adicional del 10% por usar tarjeta CINECO.")
                    break
                elif respuesta_tarjeta == 2:
                    metodo_pago = "Efectivo"
                    print("El pago se realizará en efectivo.")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

            print("\nResumen de la compra conjunta:")
            print(f"Compradores: {', '.join(compradores)}")
            print(f"Total de boletos: {total_boletos}")
            print(f"Total global a pagar: {total_global:.2f}")
            print(f"Pagador: {pagador}")
            print(f"Método de pago: {metodo_pago}")

            archivo = Fichero(compradores, total_boletos, total_global, pagador, metodo_pago)
            archivo.guardar_en_archivo()

            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
        except Exception as e:
            print(f"Error: {e}")

def main():
    print("\nBienvenido al cine de Unicentro")
    print("El costo de los boletos es de 12 pesos \nAplica descuentos dependiendo la cantidad de boletos a comprar\nDe 3 a 5 boletos 10% de descuento\nMayor a 7 boletos un 15% de descuento")
    print("¡No se permiten más de 7 boletos de compra por persona!")
    while True:
        procesar_compras()
        continuar = input("¿Se desea realizar otra compra? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por su visita. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()