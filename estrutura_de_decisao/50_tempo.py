temperatura = float(input("Digite a temperatura atual: "))

if temperatura <= 10:
    print(f"Muito frio. Está fazendo {temperatura}°C.")

elif temperatura <= 14:
    print(f"Frio. Está fazendo {temperatura}°C.")

elif temperatura <= 19:
    print(f"Agradável. Está fazendo {temperatura}°C.")

elif temperatura <= 25:
    print(f"Calor. Está fazendo {temperatura}°C.")

elif temperatura <= 32:
    print(f"Muito calor. Está fazendo {temperatura}°C.")

else:
    print("Temperatura não informada")
