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
    def ordenarLista(self, lista):
        return sorted(lista)
    
    def maximo(self, lista):
        #Realizar la operacion asignada

        if not lista:  # si la lista está vacía
            return None

        mayor = lista[0]
        for numero in lista:
            if numero > mayor:
                mayor = numero
        return mayor
     

    def minimo(self, lista):
        #Realizar la operacion asignada
        return min(lista)

    
    def esImpar(self, numero):
        
        if numero % 2 != 0:
            return "El número es impar."
        else:
           return "El número  no es impar (es par)."

    
    def espar(self,numero):

        if numero % 2 == 0:
            return "El número es par."
        else:
            return "El número no es par."

    
    def eliminarDuplicados(self, lista):
        listaDup = []
        for i in lista:
            if i not in listaDup:
                listaDup.append(i)
        return "lista sin duplicados = ", listaDup

