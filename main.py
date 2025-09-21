from clases.operaciones import Operaciones

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    # Realiza aqui tu prueba 
    lista = [10, 20, 30, 40, 50]
    print("La lista es:", lista)
    print("El promedio es:", test.promedio(lista))

    
if __name__ == '__main__':
    main()
