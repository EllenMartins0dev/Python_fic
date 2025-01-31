# Imprimir os números pares de 1 até 100
numero = 1

while numero <= 100:
    # % operador resto da divisão
    if (numero % 2) == 0:
        print(f"O número {numero} é par")

    numero += 1
