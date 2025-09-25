import json

def ler_arquivo(nome_arquivo):
    
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = json.load(arquivo)
    return conteudo

conteudo_json = ler_arquivo('person.json')
print(conteudo_json) 