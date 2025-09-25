def maiores_que_media(conteudo):
    soma = sum(conteudo.values())
    quantidade = len(conteudo)
    media = soma / quantidade

    produtos_acima_da_media = []
    for produto, preco in conteudo.items():
        if preco > media:
            produtos_acima_da_media.append((produto, preco))


    produtos_acima_da_media.sort(key=lambda x: x[1])

    return produtos_acima_da_media