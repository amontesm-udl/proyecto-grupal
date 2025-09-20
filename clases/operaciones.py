class Operaciones:
    
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    #Implementar aqui tu metodo
    def esImpar(self, numero: int) -> bool:
        #Regresa True si el número es impar, False en caso contrario.
            
        if numero % 2 == 0:
            return False
        else:
            return True