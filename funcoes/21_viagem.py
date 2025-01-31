def calculo_valor_total_combustivel(**kwargs):
    distancia = input("Digite a distância entre as duas cidades: ")
    km_por_litro = input("Digite o km por litro do veiculo: ")
    litros_usados = float(distancia)/float(km_por_litro)
    combustivel_valor_por_litro = kwargs.get("gasolina")
    valor_total_combustivel = float(combustivel_valor_por_litro)*litros_usados
    return valor_total_combustivel


cidade_saida = input("Digite a cidade de saida: ")
cidade_destino = input("Digite a cidade de destino: ")
combustivel = input("Digite o combustível utilizado: ")

gasto_total = calculo_valor_total_combustivel(gasolina=5.99)


print("---- Resumo da viagem ----\n")
print(f"Cidade saída: {cidade_saida}")
print(f"Cidade destino: {cidade_destino}")
print(f"Combustível utilizado: {combustivel}")
print(f"O valor gasto será {gasto_total:.2f}")
