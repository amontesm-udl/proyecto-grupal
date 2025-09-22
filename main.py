from clases.operaciones import Operaciones

def main():
    #No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    #Realiza aqui tu prueba.
    numero = 4
    print(f"¿{numero} es par?:",test.esPar(numero))
    
if __name__ == '__main__':
    main()