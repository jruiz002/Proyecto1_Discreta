# Importa el módulo `Globals` como `g`. Este módulo se asume que contiene datos globales, como conjuntos almacenados.
import Globals as g

# Función que calcula la unión de dos conjuntos
def union(conjunto1, conjunto2):
    # Crear un nuevo conjunto para almacenar la unión
    union = set(conjunto1)  # Copia el primer conjunto en el nuevo conjunto
    
    # Añadir los elementos del segundo conjunto al nuevo conjunto
    for elemento in conjunto2:
        union.add(elemento)  # Agrega el elemento al conjunto de unión
    
    return union  # Devuelve el conjunto que contiene todos los elementos de ambos conjuntos

# Función que calcula la intersección de dos conjuntos
def interseccion(conjunto1, conjunto2):
    # Crear un nuevo conjunto para almacenar la intersección
    interseccion = set()
    
    # Iterar sobre los elementos del primer conjunto
    for elemento in conjunto1:
        # Verificar si el elemento también está en el segundo conjunto
        if elemento in conjunto2:
            interseccion.add(elemento)  # Agrega el elemento al conjunto de intersección
    
    return interseccion  # Devuelve el conjunto de elementos comunes a ambos conjuntos

# Función que calcula la diferencia entre dos conjuntos
def diferencia(conjunto1, conjunto2):
    # Crear un nuevo conjunto para almacenar la diferencia
    diferencia = set()
    
    # Iterar sobre cada elemento en el primer conjunto
    for elemento in conjunto1:
        # Verificar si el elemento no está en el segundo conjunto
        if elemento not in conjunto2:
            diferencia.add(elemento)  # Agrega el elemento al conjunto de diferencia
    
    return diferencia  # Devuelve el conjunto de elementos en el primer conjunto pero no en el segundo

# Función que calcula la diferencia simétrica entre dos conjuntos
# La diferencia simétrica se define como AΔB = (A - B) ∪ (B - A)
def diferencia_simetrica(conjunto1, conjunto2):
    # Crear un nuevo conjunto para almacenar la diferencia simétrica
    diferencia_simetrica = set()
    
    # Encontrar elementos que están en conjunto1 pero no en conjunto2
    for elemento in conjunto1:
        if elemento not in conjunto2:
            diferencia_simetrica.add(elemento)  # Agrega el elemento al conjunto de diferencia simétrica
    
    # Encontrar elementos que están en conjunto2 pero no en conjunto1
    for elemento in conjunto2:
        if elemento not in conjunto1:
            diferencia_simetrica.add(elemento)  # Agrega el elemento al conjunto de diferencia simétrica
    
    return diferencia_simetrica  # Devuelve el conjunto de elementos que están en uno de los conjuntos pero no en ambos

# Función que calcula el complemento de un conjunto respecto a un conjunto universal
def complemento(conjunto, conjunto_universal):
    # Crear un nuevo conjunto para almacenar el complemento
    complemento = set()
    
    # Encontrar elementos que están en el conjunto universal pero no en el conjunto dado
    for elemento in conjunto_universal:
        if elemento not in conjunto:
            complemento.add(elemento)  # Agrega el elemento al conjunto de complemento
    
    return complemento  # Devuelve el conjunto de elementos en el conjunto universal pero no en el conjunto dado

# Función que muestra todos los conjuntos creados y sus elementos
def ver_conjuntos():
    # Verifica si hay conjuntos disponibles
    if not g.conjuntos:
        print("No hay conjuntos disponibles.")  # Mensaje si no hay conjuntos
    else:
        print("\nConjuntos almacenados:")
        # Itera sobre los conjuntos y muestra su identificador y elementos
        for identificador, conjunto in g.conjuntos.items():
            print(f"{identificador}: {conjunto}")

# Función que valida que todos los elementos sean letras (A-Z) o dígitos (0-9)
def validar_elementos(elementos):
    return all(el.isalnum() and len(el) == 1 and (el.isalpha() or el.isdigit()) for el in elementos)

# Función que permite al usuario construir un nuevo conjunto
def construir_conjunto():
    # Solicita al usuario un identificador para el conjunto
    identificador = input("Ingrese un identificador para el conjunto (una palabra o letra): ").strip()
    
    # Verifica si ya existe un conjunto con el identificador proporcionado
    if identificador in g.conjuntos:
        print(f"Error: Ya existe un conjunto con el identificador '{identificador}'.")  # Mensaje de error
        return
    
    # Solicita al usuario los elementos del conjunto, separados por espacio
    elementos = input("Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9) separados por espacio: ").split()
    
    # Valida que todos los elementos sean válidos
    if not validar_elementos(elementos):
        print("Error: Todos los elementos deben ser letras (A-Z) o dígitos (0-9).")  # Mensaje de error
        return
    
    # Crea el conjunto y lo almacena en el diccionario global con el identificador proporcionado
    conjunto = set(elementos)
    g.conjuntos[identificador] = conjunto
    print(f"Conjunto '{identificador}' creado: {conjunto}")  # Mensaje de éxito
