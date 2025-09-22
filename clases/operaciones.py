class Operaciones:
    
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    # Implementar aqui tu metodo
    def suma(self, n1, n2):
        """
        Regresa la suma de dos números
        """
        return n1 + n2

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



        
