# José Gerardo Ruiz García - 23719
# Gerardo André Fernández Cruz - 23763

# NOTA: Para realizar operaciones compuestas entre conjuntos se deben de usar paréntesis separados 
# es decir que siempre que se usen paréntesis se debe de poner un espacio, a continuación, 
# se muestra un ejemplo: ( A ∪ ( B ∩ C ) )


# Se importan las funciones definidas en los módulos `Functions` y `Tokenizer`
import Functions as f
import Tokenizer as t

# Bandera que controla la ejecución del bucle principal
flag = True

# Bucle principal que se ejecuta mientras `flag` sea True
while flag:
    # Muestra el menú principal con las opciones disponibles
    print("\nMenú Principal:")
    print("1. Construir conjuntos")
    print("2. Operar conjuntos")
    print("3. Ver conjuntos")
    print("4. Finalizar")

    # Solicita al usuario que elija una opción del menú
    opcion = input("Elija una opción (1-4): ")

    # Ejecuta la opción seleccionada por el usuario
    if opcion == "1":
        # Llama a la función para construir conjuntos desde el módulo `Functions`
        f.construir_conjunto()

    elif opcion == "2":
        # Llama a la función para construir y operar conjuntos desde el módulo `Tokenizer`
        t.construir_y_operar_conjuntos()

    elif opcion == "3":
        # Llama a la función para ver los conjuntos desde el módulo `Functions`
        f.ver_conjuntos()

    elif opcion == "4":
        # Cambia la bandera para salir del bucle y finalizar el programa
        flag = False
        print("Finalizando el programa.")

    else:
        # Muestra un mensaje de error si la opción elegida no es válida
        print("Opción inválida. Por favor, elija una opción válida.")
