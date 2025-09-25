import random 
import random
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios...")

dados = []
for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

output_file = "nomes_aleatorios.txt"
print(f"Salvando nomes em {output_file}...")

with open(output_file, "w", encoding="utf-8") as file:
    for nome in dados:
        file.write(nome + "\n")

print(f"Arquivo {output_file} gerado com sucesso!")

