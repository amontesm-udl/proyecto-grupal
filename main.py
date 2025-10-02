import math
from clases.operaciones import Operaciones

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    # Realiza aqui tu prueba
    l = [10, -3, -10, 0, -60, 78]
    print(f"El número menor de la lista {l} es: {test.minimo(l)}")

    print(test.esImpar(5))
   
    print(test.espar(8))

    print(test.eliminarDuplicados([1,2,2,3,4,5,5,8,9,6,6]))


if __name__ == '__main__':
    main()
