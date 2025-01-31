carro = input("Digite o modelo do carro: ")
cidade_saida = input("Digite a cidade de saída: ")
cidade_destino = input("Digite a cidade de destino: ")
distancia = float(input("Digite a distância que irá percorrer (em km): "))
kms_por_litro_g = float(input("Informe os kms por litro com o combustível gasolina: "))
kms_por_litro_e = float(input("Informe os kms por litro com o combustível etanol: "))
combustivel_etanol = 3.79
combustivel_gasolina = 5.59

print(f"\n---- Calculo da sua viagem ----")
print(f"Cidade de saída: {cidade_saida.title()}")
print(f"Cidade de destino: {cidade_destino.title()}")

valor_total_e = (distancia/kms_por_litro_e)*combustivel_etanol
valor_total_g = (distancia/kms_por_litro_g)*combustivel_gasolina

if valor_total_g > valor_total_e:
    print(f"De acordo com as informações do carro {carro.title()}, compensa você utilizar o etanol, pois assim pagará "
          f"{valor_total_e:.2f} reais (Valor etanol considerado: {combustivel_etanol}).")

elif valor_total_e > valor_total_g:
    print(f"De acordo com as informações do carro {carro.title()}, compensa você utilizar a gasolina, "
          f"pois pagará {valor_total_g:.2f} reais (Valor gasolina considerado: {combustivel_gasolina}).")

elif valor_total_e == valor_total_g:
    print(f"De acordo com as informações do carro {carro.title()}, "
          f"você pode utilizar o combustível de seu agrado, pois o valor será o mesmo: {valor_total_g:.2f} reais.")

else:
    print("Valores indefinidos.")
