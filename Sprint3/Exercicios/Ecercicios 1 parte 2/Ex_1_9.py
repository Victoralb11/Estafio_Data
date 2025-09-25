primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31] 

pessoas = []

for x in range(len(primeirosNomes)):
    pessoa = {
        'nome': primeirosNomes[x],
        'sobrenome': sobreNomes[x],
        'idade': idades[x],
        }
    pessoas.append(pessoa) 
for index, pessoa in enumerate(pessoas):
    print(f"{index} - {pessoa['nome']} {pessoa['sobrenome']} está com {pessoa['idade']} anos"))