import Functions as f
import Globals as g

# Ingresa cada elemento a su correspondiente pila
def operar_conjuntos(expresion):
    operandos = []
    operadores = []
    
    tokens = expresion.split()
    
    for token in tokens:
        if token in g.conjuntos:
            operandos.append(g.conjuntos[token])
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
        resultado = f.complemento(conjunto, g.conjunto_universal)
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
    
        if len(g.conjuntos) < 2:
            print("\nSe necesitan al menos dos conjuntos para realizar una operación.")
            return
        
        print("\nOperadores: ∪ (Union), ∩ (Interseccion), - (Diferencia), Δ (Diferencia simetrica), ! (Complemento)")
        f.ver_conjuntos()
        
        expresion = input("Ingrese los identificadores de conjuntos, operadores y parentesis separados por espacios: ")
        
        try:
            resultado = operar_conjuntos(expresion)
            print(f"\n'{expresion}' = {resultado}")
        except Exception as e:
            print(f"Error al procesar la operación: {e}")
        
        return