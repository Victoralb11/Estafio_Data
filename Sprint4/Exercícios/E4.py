def calcular_valor_maximo(operadores, operandos):
    def calcular_resultado(operador, operandos):
        operando1, operando2 = operandos
        if operador == '+':
            return operando1 + operando2
        elif operador == '-':
            return operando1 - operando2
        elif operador == '*':
            return operando1 * operando2
        elif operador == '/':
            return operando1 / operando2
        elif operador == '%':
            return operando1 % operando2

    operacoes = zip(operadores, operandos)

    resultados = map(lambda x: calcular_resultado(x[0], x[1]), operacoes)

    return max(resultados)