import Functions as f
import Tokenizer as t

# Para utilizar complemento hacerlo de la siguiente manera: ! A

flag = True
while flag:
    print("\nMenú Principal:")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Ver conjuntos")
    print("4. Finalizar")

    opcion = input("Elija una opción (1-4): ")

    if opcion == "1":
        f.construir_conjunto()

    elif opcion == "2":
        t.construir_y_operar_conjuntos()

    elif opcion == "3":
        f.ver_conjuntos()

    elif opcion == "4":
        flag = False
        print("Finalizando el programa.")

    else:
        print("Opción inválida. Por favor, elija una opción válida.")