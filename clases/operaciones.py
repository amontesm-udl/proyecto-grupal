class Operaciones:
    
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    #Implementar aqui tu metodo
    '''
    def operacionAsignada(self):
        #Realizar la operacion asignada
    ''' 
    def modulo(self, n1, n2):
        if n2 == 0:
            return "Error: no se puede dividir entre cero"
        return n1 % n2

