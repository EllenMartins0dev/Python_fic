# Imprimir os números ímpares de 1 até 100
# Quando a quantidade chegar em 10, parar o while

numero = 1
contador_unidades = 0

while numero <= 100:
    if (numero % 2) != 0:
        print(f"O número {numero} é ímpar")
        contador_unidades += 1

    if contador_unidades == 10:
        break

    numero += 1
