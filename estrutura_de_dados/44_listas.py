numeros = [20, 56, 19, 40, 31]
print(f"A lista tem {len(numeros)} itens")

print(f"O index 2 da lista é o número {numeros[2]}")

""""
Alteração de itens da lista
"""

# Atualizar item da lista
numeros[4] = 230
print(f"A lista tem os números {numeros}")

# adicionar um item na lista
numeros.append(670)
print(f"A nova lista tem os números {numeros}")

# remover um item da lista pelo seu índice
del numeros[3]
print(f"Números lista: {numeros}")

# remover o último item da lista
numeros.pop()
print(f"Novos números da lista: {numeros}")
