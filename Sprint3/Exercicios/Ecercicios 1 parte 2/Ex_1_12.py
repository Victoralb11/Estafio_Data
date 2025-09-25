def my_map(lista,func):
    nova_lista = []
    
    for elemento in lista:
        nova_lista.append(func(elemento)) 
    return nova_lista 
def quadrado(x):
    return x**2 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(lista,quadrado)

print(resultado)