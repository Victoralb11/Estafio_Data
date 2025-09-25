def remover_duplos(lista):
    return sorted(set(lista))

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = remover_duplos(lista)
print(resultado)