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