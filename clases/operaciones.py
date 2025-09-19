class Operaciones:
    
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    # Implementar aqui tu metodo
    def generarTablaMultiplicar(self, numero: int):
        #Imprime la tabla de multiplicar del número indicado (del 1 al 10).
        print(f"\nTabla de multiplicar del {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")