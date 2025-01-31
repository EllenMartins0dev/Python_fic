print("Calculadora do Amor")

nome1 = input("Digite o nome da primeira pessoa: ")
nome2 = input("Digite o nome da segunda pessoa: ")

# Convertendo os nomes para letras minúsculas e removendo espaços em branco
nome1 = nome1.lower().replace(" ", "")
nome2 = nome2.lower().replace(" ", "")

# Contando a quantidade de letras em cada nome
total1 = 0
total2 = 0

for letra in nome1:
    total1 += ord(letra) - ord('a') + 1

for letra in nome2:
    total2 += ord(letra) - ord('a') + 1

# Calculando a porcentagem de compatibilidade
compatibilidade = (total1 + total2) % 101

print("A compatibilidade entre", nome1.capitalize(), "e", nome2.capitalize(), "é de", compatibilidade, "%.")
