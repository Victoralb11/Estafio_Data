import hashlib 

while True:
    resposta = input("deseja encriptar uma string ? (s/n)")
    if resposta.lower() == 'n':
        print("Encerrando o programa.")
        break
    elif resposta.lower() == 's':
        String = input("Digite a palavra ou frase que deseja encriptar:")
        hash_sha1 = hashlib.sha1()
        hash_sha1.update(String.encode('utf-8'))
        hash_resultado = hash_sha1.hexdigest()
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

    print("Hash SHA-1:", hash_resultado)