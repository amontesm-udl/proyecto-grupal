from clases.operaciones import Operaciones

def main():
    #No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    #Realiza aqui tu prueba 
    lista = [5, 3, 9, 1, 4]
    print("La lista es:", lista)
    print("El número menor es:", test.minimo(lista))
    
if __name__ == '__main__':
    main()
