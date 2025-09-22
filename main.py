from clases.operaciones import Operaciones

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())

    # Realiza aqui tu prueba
    resultado = test.multiplica(5, 3)  # Ejemplo con 5 y 3
    print(f"Multiplicacion: {resultado}")

    print(test.potencia(2,3))
    
    lista = [5, 3, 9, 1, 4]
    print("La lista es:", lista)
    print("El número menor es:", test.minimo(lista))

    lista = [3.5, -12, 7, 0.8, -3.14, 22, -19.6, 5.5, 13, -0.75, 9.1, 4, -7, 11.11, -2, 6.66, 18, 201, 6001, -0.33, 2.2, -8.8, 0, 10, -1.5, 1.1, -20]
    print(test.ordenarLista(lista))

    

if __name__ == '__main__':
    main()
