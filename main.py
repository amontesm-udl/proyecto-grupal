from clases.operaciones import Operaciones

def main():
    #No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    #Realiza aqui tu prueba 
    
    # Lista de 10 números 
    numeros = [15, 1, 2, 3, 4, 5, -6, 41, 10, 15]

    print("\n=== Prueba de 10 números ===")
    for n in numeros:
        print(f"{n}: {test.esImpar(n)}")
    
if __name__ == '__main__':
    main()