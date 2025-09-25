with open('number.txt', 'r') as file:
    numeros = file.readlines()

numeros = list(map(int, numeros))

pares = list(filter(lambda x: x % 2 == 0, numeros))

maiores_pares = sorted(pares, reverse=True)[:5]

soma_maiores_pares = sum(maiores_pares)

print(maiores_pares)  
print(soma_maiores_pares)