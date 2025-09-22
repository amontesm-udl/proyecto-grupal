from clases.operaciones import Operaciones

def main():
    #No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    #Realiza aqui tu prueba 
    
     # Prueba con un número par
    print(f"10: {test.esImpar(10)}")   
    
    # Prueba con un número impar
    print(f"7: {test.esImpar(7)}")    
    
if __name__ == '__main__':
    main()