# Imprimir os números de 0 até 10 em uma linha com for
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [print(f"Numero: {n}") for n in numeros]

n_pares = [n for n in numeros if n % 2 == 0]
n_impares = [n for n in numeros if n % 2 != 0]

cores = ["azul", "amarelo", "roxo", "azul"]
c_azul = [c for c in cores if c == "azul"]

c_azul2 = []
for c in cores:
    if c == "azul":
        c_azul2.append(c)

print(f"Pares: {n_pares}")
print(f"Ímpares: {n_impares}")

# for n in numeros:
#     if n % 2 == 0:
#         print("")
