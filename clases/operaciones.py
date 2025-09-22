class Operaciones:
    
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    #Implementar aqui tu metodo
    def eliminarDuplicados(self, lista):
        listaSinDuplicados = []
        vistos = set()
        for elemento in lista:
            if elemento not in vistos:
                listaSinDuplicados.append(elemento)
                vistos.add(elemento)
        return listaSinDuplicados



