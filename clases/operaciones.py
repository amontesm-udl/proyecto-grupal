import numpy as np
import math


class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    
    def eliminarDuplicados(self):
        lista = [1,2,2,3,4,5,5,5,6,8,9,9]
        listaDup = []
        for i in lista:
            if i not in listaDup:
                listaDup.append(i)
        return "lista sin duplicados = ", listaDup
