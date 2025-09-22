import math
from clases.operaciones import Operaciones

def raizCuadrada(n):
    return math.sqrt(n)

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())

    # Realiza aqui tu prueba
    resultado = test.multiplica(5, 3)  # Ejemplo con 5 y 3
    print(f"Multiplicacion: {resultado}")

    print(test.potencia(2, 3))
    
    # Realiza aqui tu prueba.
    numero = 4
    print(f"¿{numero} es par?:", test.esPar(numero))

    # Prueba con un número par
    print(f"10: {test.esImpar(10)}")   
    
    # Prueba con un número impar
    print(f"7: {test.esImpar(7)}")    
    
    # Realiza aqui tu prueba
    lista = [10, 20, 30, 40, 50]
    print("El promedio es:", test.promedio(lista))

    repeticiones = test.contarPalabraEnTexto("hola mundo hola", "hola")
    print(f"Las palabras que se repiten son {repeticiones}")

    resultado = test.resta(10, 4)
    print(f"La resta de 10 - 4 es: {resultado}")
   
    resultado = test.eliminarDuplicados([1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10])
    print("La lista de números sin duplicados es:", resultado)

    resultado = raizCuadrada(25)
    print(f"La raíz cuadrada de {numero} es {resultado}")

    test.generarTablaMultiplicar(5)  # Ejemplo con el número 5

    lista = [5, 3, 9, 1, 4]
    print("La lista es:", lista)
    print("El número menor es:", test.minimo(lista))

    lista = [3.5, -12, 7, 0.8, -3.14, 22, -19.6, 5.5, 13, -0.75, 9.1, 4, -7, 11.11, -2, 6.66, 18, 201, 6001, -0.33, 2.2, -8.8, 0, 10, -1.5, 1.1, -20]
    print(test.ordenarLista(lista))

    # Prueba para numeroMayor (Sarahí)
    print("El mayor de 5, 3, 7 es:", test.numeroMayor(5, 3, 7))  
    print("El mayor de 1, 10, 2 es:", test.numeroMayor(1, 10, 2))  

if __name__ == '__main__':
    main()