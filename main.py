import math
from clases.operaciones import Operaciones

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())

    # Realiza aqui tu prueba

    numeros = [4, 10, 2, 33, 7]
    resultado = test.maximo(numeros)

    if resultado is not None:
        print("El número mayor es:", resultado)
    else:
        print("La lista está vacía")
   

if __name__ == '__main__':
    main()
