class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def contarPalabraEnTexto(self, texto, palabra):
        texto = texto.lower()
        palabra = palabra.lower()
        palabras = texto.split()
        return palabras.count(palabra)


