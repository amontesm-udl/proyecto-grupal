from clases.operaciones import Operaciones

def main():
    # No cambiar estas líneas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    # Realiza aquí tu prueba
    repeticiones = test.contarPalabraEnTexto("hola mundo hola", "hola")
    print(f"Las palabras que se repiten son {repeticiones}")

if __name__ == "__main__":
    main()
