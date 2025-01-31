
try:
    numeros = [1, 2, 50, 70, 345]
    print(f"O número na posição 5 é {numeros[5]}")
except IndexError as erro_indice:
    print(f"Erro ao acessar o indice {erro_indice}")
