import numpy as np
import math


class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def promedio(self, lista):
        """
        Calcula el promedio de los números en una lista.
        """
        if len(lista) == 0:
            return 0  # evitar división entre cero
        return sum(lista) / len(lista)

    

