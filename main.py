import math
from clases.operaciones import Operaciones

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    lista_numeros = [5, 9, 3, 19, 23, 1]
    print("Lista ordenada = ", test.ordenarLista(lista_numeros))
     


if __name__ == '__main__':
    main()
