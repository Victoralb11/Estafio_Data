animais = [
    "Lobo", "Corvo", "Falcão", "Pantera", "Serpente",
    "Jaguar", "Águia", "Dragão", "Raposa", "Hiena",
    "Tigre Branco", "Cobra", "Gato Preto", "Urso Pardo", "Lêmure",
    "Tubarão Branco", "Escorpião", "Morcego", "Leopardo das Neves", "Harpia"
]

animais.sort()

with open("animais_edgy.csv", "w", encoding="utf-8") as arquivo:
    arquivo.writelines([f"{animal}\n" for animal in animais])

print("Os itens foram armazenados no arquivo 'animais_edgy.csv'.")