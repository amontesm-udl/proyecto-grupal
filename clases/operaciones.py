import numpy as np
import math


class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    
    def operacionAsignada(self, lista):
        #Realizar la operacion asignada

        if not lista:  # si la lista está vacía
            return None

        mayor = lista[0]
        for numero in lista:
            if numero > mayor:
                mayor = numero
        return mayor
     

    

