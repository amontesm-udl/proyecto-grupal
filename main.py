import math
from clases.operaciones import Operaciones

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())

    # Realiza aqui tu prueba
     
    lista = [10, 20, 30, 40]
    resultado = test.promedio(lista)
    print(f"El promedio de {lista} es: {resultado}")
   


if __name__ == '__main__':
    main()


