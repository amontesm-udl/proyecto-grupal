import math
from clases.operaciones import Operaciones

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    lista_numeros = [5, 9, 3, 19, 23, 1]
    print("Lista ordenada = ", test.ordenarLista(lista_numeros))
     
    # Realiza aqui tu prueba

    print(test.esImpar(5))
   
    print(test.espar(8))

    print(test.eliminarDuplicados([1,2,2,3,4,5,5,8,9,6,6]))

    numeros = [4, 10, 2, 33, 7]
    resultado = test.maximo(numeros)

    if resultado is not None:
        print("El número mayor es:", resultado)
    else:
        print("La lista está vacía")
   

if __name__ == '__main__':
    main()
