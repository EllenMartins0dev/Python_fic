cidade_saida = input("Digite a cidade de saida: ")
cidade_destino = input("Digite a cidade de destino: ")
distancia = input("Digite a distância entre elas: ")
combustivel = input("Digite qual combustível será usado: ")
combustivel_valor_por_litro = input("Valor do combustível: ")
km_litro = input("Digite a média de km por litro do veículo: ")


quantidade_litros_usados = float(distancia)/float(km_litro)
valor_total_combustivel = float(combustivel_valor_por_litro)*float(quantidade_litros_usados)

print("---- Resumo da viagem ----\n")
print(f"Cidade saída: {cidade_saida}")
print(f"Cidade destino: {cidade_destino}")
print(f"Distância entre as cidades: {distancia}")
print(f"Combustível utilizado: {combustivel}")
print(f"Valor do combustível (média por litro: {combustivel_valor_por_litro}")
print(f"Quantidade de litros necessários: {quantidade_litros_usados:.2f}")
print(f"Valor gasto em combustível na viagem: {valor_total_combustivel:.2f}")
