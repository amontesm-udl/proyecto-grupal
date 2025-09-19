from clases.operaciones import Operaciones

def main():
    # No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())

    # Realiza aqui tu prueba
    resultado = test.multiplica(5, 3)  # Ejemplo con 5 y 3
    print(f"Multiplicacion: {resultado}")

if __name__ == '__main__':
    main()