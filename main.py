import math
from clases.operaciones import Operaciones

def raizCuadrada(n):
    return math.sqrt(n)

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    # Realiza aqui tu prueba
    numero = float(input("Ingresa un número para la raiz cuadrada: "))
    resultado = raizCuadrada(numero)
    print(f"La raíz cuadrada de {numero} es {resultado}")

if __name__ == '__main__':
    main()
