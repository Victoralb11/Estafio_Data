import csv

with open('estudantes.csv') as arquivo:
    ler = csv.reader(arquivo, delimiter=',')
    for linha in sorted(ler):
        notas = list(map(int, linha[1:]))
        notas_ord = sorted(notas, reverse=True)[:3]
        media = round(sum(notas_ord)/3, 2)
        print(f"Nome: {linha[0]} Notas: {notas_ord} Média: {media}")