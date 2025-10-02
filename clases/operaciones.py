import numpy as np
import math


class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    
    def eliminarDuplicados(self, lista):
        listaDup = []
        for i in lista:
            if i not in listaDup:
                listaDup.append(i)
        return "lista sin duplicados = ", listaDup
