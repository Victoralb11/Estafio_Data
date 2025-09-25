class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade, cor):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = cor  
avioes = [] 
avioes.append(Aviao("BOIENG456", "1500 km/h", 400, "Azul"))
avioes.append(Aviao("Embraer Praetor 600", "863 km/h", 14, "Azul"))
avioes.append(Aviao("Antonov An-2", "258 km/h", 12, "Azul")) 
for aviao in avioes:
    print(f"O avião de modelo \"{aviao.modelo}\" possui uma velocidade máxima de \"{aviao.velocidade_maxima}\", capacidade para \"{aviao.capacidade}\" passageiros e é da cor \"{aviao.cor}\".")