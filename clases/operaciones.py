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

    def multiplica(self, n1, n2):
        # Realizar la operación asignada
        return n1 * n2

    def potencia(self,n1,n2):
        return n1**n2

    def minimo(self, lista):
        """
        Realizar la operacion asignada
        """
        if not lista:
            raise ValueError("La lista no puede estar vacía")
        menor = lista[0]
        for num in lista[1:]:
            if num < menor:
                menor = num
        return menor

    
    def ordenarLista(self, lista):
        return sorted(lista)



        
