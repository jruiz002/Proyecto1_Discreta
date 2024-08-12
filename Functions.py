import Globals as g

def union(conjunto1, conjunto2):
    # Crear un nuevo conjunto para almacenar la unión
    union = set(conjunto1)  # Copiar el primer conjunto
    
    # Añadir los elementos del segundo conjunto al nuevo conjunto
    for elemento in conjunto2:
        union.add(elemento)
    
    return union

def interseccion(conjunto1, conjunto2):
    # Crear un nuevo conjunto para almacenar la intersección
    interseccion = set()
    
    # Iterar sobre los elementos del primer conjunto
    for elemento in conjunto1:
        # Verificar si el elemento también está en el segundo conjunto
        if elemento in conjunto2:
            interseccion.add(elemento)
    
    return interseccion

# Devuelve todos los elementos que estan en el primer conjunto pero no en el segundo conjunto
def diferencia(conjunto1, conjunto2):
    # Crear un nuevo conjunto para almacenar la diferencia
    diferencia = set()
    
    # Iterar sobre cada elemento en el primer conjunto
    for elemento in conjunto1:
        # Verificar si el elemento no está en el segundo conjunto
        if elemento not in conjunto2:
            diferencia.add(elemento)
    
    return diferencia

# Esta definido como AΔB=(A−B)∪(B−A)
def diferencia_simetrica(conjunto1, conjunto2):
    # Crear un nuevo conjunto para almacenar la diferencia simétrica
    diferencia_simetrica = set()
    
    # Encontrar elementos que están en conjunto1 pero no en conjunto2
    for elemento in conjunto1:
        if elemento not in conjunto2:
            diferencia_simetrica.add(elemento)
    
    # Encontrar elementos que están en conjunto2 pero no en conjunto1
    for elemento in conjunto2:
        if elemento not in conjunto1:
            diferencia_simetrica.add(elemento)
    
    return diferencia_simetrica


def complemento(conjunto, conjunto_universal):
    # Crear un nuevo conjunto para almacenar el complemento
    complemento = set()
    
    # Encontrar elementos que están en el conjunto universal pero no en el conjunto dado
    for elemento in conjunto_universal:
        if elemento not in conjunto:
            complemento.add(elemento)
    
    return complemento

def ver_conjuntos():
    #Muestra todos los conjuntos creados y sus elementos.
    if not g.conjuntos:
        print("No hay conjuntos disponibles.")
    else:
        print("\nConjuntos almacenados:")
        for identificador, conjunto in g.conjuntos.items():
            print(f"{identificador}: {conjunto}")


def validar_elementos(elementos):
    #Valida que todos los elementos sean letras (A-Z) o dígitos (0-9).
    return all(el.isalnum() and len(el) == 1 and (el.isalpha() or el.isdigit()) for el in elementos)

def construir_conjunto():
    #Permite al usuario construir un nuevo conjunto con un identificador único y elementos válidos.
    identificador = input("Ingrese un identificador para el conjunto (una palabra o letra): ").strip()
    
    if identificador in g.conjuntos:
        print(f"Error: Ya existe un conjunto con el identificador '{identificador}'.")
        return
    
    elementos = input("Ingrese los elementos del conjunto (letras A-Z y dígitos 0-9) separados por espacio: ").split()
    
    if not validar_elementos(elementos):
        print("Error: Todos los elementos deben ser letras (A-Z) o dígitos (0-9).")
        return
    
    conjunto = set(elementos)
    g.conjuntos[identificador] = conjunto
    print(f"Conjunto '{identificador}' creado: {conjunto}")