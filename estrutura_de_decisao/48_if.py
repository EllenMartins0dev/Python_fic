# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento
media = (nota1 + nota2)/2

if media >= 9.0:
    print(f"Está de parabéns! Sua média foi {media}")

elif media >= 5.0:
    print(f"Você está aprovado. Sua média foi {media}")

elif media >= 4.0:
    print(f"Você está de recuperação. Sua média foi {media}")

elif media < 0:
    print(f"Notas inválidas.")

else:
    print(f"Você esta reprovado. Sua média foi {media}")
