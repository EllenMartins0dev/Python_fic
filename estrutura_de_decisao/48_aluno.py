nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = float(input("Digite a quantidade de faltas: "))

media = (nota1 + nota2)/2

if media >= 9.0 and faltas <= 3:
    print(f"Você está de parabéns! Sua média foi {media} e você teve {faltas} faltas.")

elif media >= 6.5 and faltas <= 3:
    print(f"Você foi aprovado! Sua média foi {media} e você teve {faltas} faltas.")

elif faltas == 4:
    print(f"Você está de recuperação. Sua média foi {media} e você teve {faltas} faltas.")

elif faltas > 4:
    print("Você está reprovado.")

elif media == 4.0:
    print(f"Você está de recuperação. Sua média foi {media} e você teve {faltas} faltas.")

elif media < 4.0:
    print(f"Você está reprovado.")

else:
    print("Valores indefinidos.")
