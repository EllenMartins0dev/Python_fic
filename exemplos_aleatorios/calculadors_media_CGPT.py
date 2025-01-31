def calcular_media():
    numeros = []
    total = 0

    # Solicita ao usuário a quantidade de números
    quantidade = int(input("Digite a quantidade de números: "))

    # Solicita ao usuário os números e os armazena em uma lista
    for i in range(quantidade):
        numero = float(input("Digite a nota {}: ".format(i + 1)))
        numeros.append(numero)
        total += numero

    # Calcula a média
    media = total / quantidade

    # Exibe o resultado
    print("A média das notas é: {:.2f}".format(media))

# Chama a função para executar o programa
calcular_media()