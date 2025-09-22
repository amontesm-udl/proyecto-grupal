from clases.operaciones import Operaciones

def main():
    #No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    #Realiza aqui tu prueba 
    resultado = test.eliminarDuplicados([1,2,2,3,4,5,6,7,8,8,9,10])
    print("La lista de números sin duplicados es:", resultado)

if __name__ == '__main__':
    main()