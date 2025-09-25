def somar_numeros(string_n):
    numeros = map(int, string_n.split(','))
    soma = sum(numeros)
    return soma 
string_n = "1,3,4,6,10,76" 
resultado = somar_numeros(string_n) 

print(resultado)