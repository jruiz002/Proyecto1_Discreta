# Importa el módulo `Functions` como `f`, que contiene funciones para operar con conjuntos
# Importa el módulo `Globals` como `g`, que contiene datos globales como los conjuntos y el conjunto universal
import Functions as f
import Globals as g

# Función que opera sobre conjuntos dados una expresión
def operar_conjuntos(expresion):
    operandos = []  # Pila para almacenar los conjuntos (operandos)
    operadores = []  # Pila para almacenar los operadores (como ∪, ∩, -)

    # Divide la expresión en tokens (elementos individuales)
    tokens = expresion.split()
    
    for token in tokens:
        if token in g.conjuntos:
            # Si el token es un identificador de conjunto, se añade a la pila de operandos
            operandos.append(g.conjuntos[token])
        elif token in {'∪', '∩', '-', 'Δ', '!'}:
            # Si el token es un operador, se aplica la operación mientras haya operadores en la pila
            while (operadores and operadores[-1] != '('):
                aplicar_operacion(operadores, operandos)
            operadores.append(token)  # Añade el operador a la pila de operadores
        elif token == '(':
            # Si el token es un paréntesis de apertura, se añade a la pila de operadores
            operadores.append(token)
        elif token == ')':
            # Si el token es un paréntesis de cierre, se aplican operaciones hasta encontrar el paréntesis de apertura
            while operadores[-1] != '(':
                aplicar_operacion(operadores, operandos)
            operadores.pop()  # Elimina el paréntesis de apertura de la pila de operadores
    
    # Aplica todas las operaciones restantes en la pila de operadores
    while operadores:
        aplicar_operacion(operadores, operandos)
    
    return operandos[-1]  # Devuelve el resultado final de la expresión

# Función que aplica la operación correspondiente a los operadores y operandos
def aplicar_operacion(operadores, operandos):
    operador = operadores.pop()  # Obtiene el operador en la parte superior de la pila de operadores
    if operador == '!':
        conjunto = operandos.pop()  # Obtiene el último conjunto en la pila de operandos
        resultado = f.complemento(conjunto, g.conjunto_universal)  # Calcula el complemento del conjunto
    else:
        conjunto2 = operandos.pop()  # Obtiene el segundo conjunto en la pila de operandos
        conjunto1 = operandos.pop()  # Obtiene el primer conjunto en la pila de operandos
        # Aplica la operación correspondiente según el operador
        if operador == '∪':
            resultado = f.union(conjunto1, conjunto2)  # Unión de conjuntos
        elif operador == '∩':
            resultado = f.interseccion(conjunto1, conjunto2)  # Intersección de conjuntos
        elif operador == '-':
            resultado = f.diferencia(conjunto1, conjunto2)  # Diferencia de conjuntos
        elif operador == 'Δ':
            resultado = f.diferencia_simetrica(conjunto1, conjunto2)  # Diferencia simétrica de conjuntos
    operandos.append(resultado)  # Añade el resultado de la operación a la pila de operandos

# Función principal que construye y opera conjuntos
def construir_y_operar_conjuntos():
    flag = True
    while flag:
        # Verifica si hay al menos dos conjuntos para realizar una operación
        if len(g.conjuntos) < 2:
            print("\nSe necesitan al menos dos conjuntos para realizar una operación.")
            return
        
        # Muestra los operadores disponibles y los conjuntos actuales
        print("\nOperadores: ∪ (Union), ∩ (Interseccion), - (Diferencia), Δ (Diferencia simetrica), ! (Complemento)")
        f.ver_conjuntos()
        
        # Solicita al usuario la expresión para operar sobre los conjuntos
        expresion = input("Ingrese los identificadores de conjuntos, operadores y parentesis separados por espacios: ")
        
        try:
            # Procesa la expresión e imprime el resultado
            resultado = operar_conjuntos(expresion)
            print(f"\n'{expresion}' = {resultado}")
        except Exception as e:
            # Captura y muestra cualquier error que ocurra durante el procesamiento
            print(f"Error al procesar la operación: {e}")
        
        return  # Sale de la función después de procesar la expresión
