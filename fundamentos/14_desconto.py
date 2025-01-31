nome_produto = input("Digite o produto escolhido: ")
valor_produto = input("Digite o valor: ")
desconto_produto = input("Digite o percentual de desconto: ")

calculo_desconto = float(valor_produto) - (float(valor_produto)*int(desconto_produto)/100)

print("---- informações produto ----")
print(f"Produto: {nome_produto}")
print(f"Valor do produto {valor_produto}")
print(f"Percentual de desconto: {desconto_produto}")
print(f"Valor do produto com desconto: {calculo_desconto:.2f}")