import Functions as f

# Definir el diccionario conjuntos en el ámbito global
conjuntos = {}

def ver_conjuntos():
    #Muestra todos los conjuntos creados y sus elementos.
    if not conjuntos:
        print("No hay conjuntos disponibles.")
    else:
        print("\nConjuntos almacenados:")
        for identificador, conjunto in conjuntos.items():
            print(f"{identificador}: {conjunto}")


def validar_elementos(elementos):
    #Valida que todos los elementos sean letras (A-Z) o dígitos (0-9).
    return all(el.isalnum() and len(el) == 1 and (el.isalpha() or el.isdigit()) for el in elementos)

def construir_conjunto():
    #Permite al usuario construir un nuevo conjunto con un identificador único y elementos válidos.
    global conjuntos  # Se accede al diccionario de conjuntos de manera global
    identificador = input("Ingrese un identificador para el conjunto (una palabra o letra): ").strip()
    
    if identificador in conjuntos:
        print(f"Error: Ya existe un conjunto con el identificador '{identificador}'.")
        return
    
    elementos = input("Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9) separados por espacio: ").split()
    
    if not validar_elementos(elementos):
        print("Error: Todos los elementos deben ser letras (A-Z) o dígitos (0-9).")
        return
    
    conjunto = set(elementos)
    conjuntos[identificador] = conjunto
    print(f"Conjunto '{identificador}' creado: {conjunto}")

def menu_principal():
    flag = True
    while flag:
        print("\nMenú Principal:")
        print("1. Construir conjuntos")
        print("2. Operar conjuntos")
        print("3. Ver conjuntos")
        print("4. Finalizar")
        
        opcion = input("Elija una opción (1-4): ")
        
        if opcion == "1":
            construir_conjunto()

        elif opcion == "2":
            print("Operar conjuntos")

        elif opcion == "3":
            ver_conjuntos()

        elif opcion == "4":
            flag = False
            print("Finalizando el programa.")

        else:
            print("Opción inválida. Por favor, elija una opción válida.")

# Ejecutar el menú principal
menu_principal()
