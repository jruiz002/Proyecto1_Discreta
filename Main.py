import Functions as f

# Definir el diccionario conjuntos en el ámbito global
conjuntos = {}
conjunto_universal = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz")

# Ingresa cada elemento a su correspondiente pila
def operar_conjuntos(expresion):
    operandos = []
    operadores = []
    
    tokens = expresion.split()
    
    for token in tokens:
        if token in conjuntos:
            operandos.append(conjuntos[token])
        elif token in {'∪', '∩', '-', 'Δ', '!'}:
            while (operadores and operadores[-1] != '('):
                aplicar_operacion(operadores, operandos)
            operadores.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores[-1] != '(':
                aplicar_operacion(operadores, operandos)
            operadores.pop()
    
    while operadores:
        aplicar_operacion(operadores, operandos)
    
    return operandos[-1]

# Saca los conjuntos de la pila y los opera
def aplicar_operacion(operadores, operandos):
    operador = operadores.pop()
    if operador == '!':
        conjunto = operandos.pop()
        resultado = f.complemento(conjunto, conjunto_universal)
    else:
        conjunto2 = operandos.pop()
        conjunto1 = operandos.pop()
        if operador == '∪':
            resultado = f.union(conjunto1, conjunto2)
        elif operador == '∩':
            resultado = f.interseccion(conjunto1, conjunto2)
        elif operador == '-':
            resultado = f.diferencia(conjunto1, conjunto2)
        elif operador == 'Δ':
            resultado = f.diferencia_simetrica(conjunto1, conjunto2)
    operandos.append(resultado)

# Devuelve al usuario el resultado de las operaciones
def construir_y_operar_conjuntos():
    flag =  True
    while flag:
    
        if len(conjuntos) < 2:
            print("\nSe necesitan al menos dos conjuntos para realizar una operación.")
            return
        
        print("\nOperadores: ∪ (Union), ∩ (Interseccion), - (Diferencia), Δ (Diferencia simetrica), ! (Complemento)")
        ver_conjuntos()
        
        expresion = input("Ingrese los identificadores de conjuntos, operadores y parentesis separados por espacios: ")
        
        try:
            resultado = operar_conjuntos(expresion)
            print(f"\n'{expresion}' = {resultado}")
        except Exception as e:
            print(f"Error al procesar la operación: {e}")
        
        return

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
            construir_y_operar_conjuntos()

        elif opcion == "3":
            ver_conjuntos()

        elif opcion == "4":
            flag = False
            print("Finalizando el programa.")

        else:
            print("Opción inválida. Por favor, elija una opción válida.")

# Ejecutar el menú principal
menu_principal()

# Para utilizar complemento: ! A