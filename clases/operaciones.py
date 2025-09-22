class Operaciones:
    def __init__(self):
        pass  # Inicializador vacío

    def saludoAlejandroMontes(self):
        return "Mi nombre es Sarahi Silva Rocha"

    def operacionAsignada(self):
        # Realizar la operacion asignada
        pass  # Placeholder

    def generarTablaMultiplicar(self, numero: int):
        # Imprime la tabla de multiplicar del número indicado (del 1 al 10).
        print(f"\nTabla de multiplicar del {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")

    def multiplica(self, n1, n2):
        return n1 * n2

    def potencia(self, n1, n2):
        return n1 ** n2

    def minimo(self, lista):
        """
        Realizar la operacion asignada
        """
        if not lista:
            raise ValueError("La lista no puede estar vacía")
        menor = lista[0]
        for num in lista[1:]:
            if num < menor:
                menor = num
        return menor

    def ordenarLista(self, lista):
        return sorted(lista)

    # Métodos faltantes detectados en main.py
    def esPar(self, numero):
        return numero % 2 == 0

    def esImpar(self, numero):
        return numero % 2 != 0

    def promedio(self, lista):
        if not lista:
            raise ValueError("La lista no puede estar vacía")
        return sum(lista) / len(lista)

    def contarPalabraEnTexto(self, texto, palabra):
        palabras = texto.split()
        return palabras.count(palabra)

    def resta(self, n1, n2):
        return n1 - n2

    def eliminarDuplicados(self, lista):
        return list(dict.fromkeys(lista))

    #Mi nuevo método asignado (Sarahí)
    def numeroMayor(self, a, b, c):
        # Regresa el número mayor de los tres números recibidos
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
        