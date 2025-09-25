def conta_vogais(texto:str)-> int:
    vogais = filter(lambda x: x.lower() in 'aeiou', texto)
    
    return len(list(vogais))