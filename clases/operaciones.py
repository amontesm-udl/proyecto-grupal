import numpy as np
import math


class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    '''
    def operacionAsignada(self):
        #Realizar la operacion asignada
    ''' 
    def esImpar(self, numero):
        
        if numero % 2 != 0:
            return "El número es impar."
        else:
           return "El número  no es impar (es par)."
    

    

