nomes = ("Aluno 01", "Aluno 02", "Aluno 03")
print(f"Nomes tupla original: {nomes}")
print(f"A dupla tem {len(nomes)} itens")
print(f"O index 2 da tupla é {nomes[2]}")

# Adicionar item na tupla
nomes += ("Aluno 04", "Aluno 05")
print(f"Tupla alterada {nomes}")

# Remover item na tupla
del nomes[1]
print(f"Nomes tupla alterada: {nomes}")
