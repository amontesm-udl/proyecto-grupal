from clases.operaciones import Operaciones

def main():
    #No cambiar estas lineas
    test = Operaciones()
    print(test.saludoAlejandroMontes())
    
    #Realiza aqui tu prueba 
def main():
    op = Operaciones()

    while True:
        print("\n--- MENÚ ---")
        print("1. Escribir texto y palabra para contar")
        print("2. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            texto = input("Escribe el texto: ")
            palabra = input("Escribe la palabra que quieres buscar: ")

            print(op.saludoAlejandroMontes())
            print(f"La palabra '{palabra}' aparece {op.contarPalabraEnTexto(texto, palabra)} veces en el texto.")

        elif opcion == "2":
            print("Saliendo del programa... ¡Adiós!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()