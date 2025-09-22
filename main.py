from clases.operaciones import Operaciones

def main():
    #No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    #Realiza aqui tu prueba 
    resultado = test.restaEnriqueVelez(10, 4)
    print(f"La resta de 10 - 4 es: {resultado}")
    
    
if __name__ == '__main__':
    main()