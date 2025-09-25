palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    
    palavra_tratada = palavra.replace(" ", "").lower()
    
    
    if palavra_tratada == palavra_tratada[::-1]:
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")