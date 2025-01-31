def calculo_preco(**kwargs):
    dias_uso = kwargs.get("dias")
    kms_usados = kwargs.get("kms")
    preco_total = (dias_uso*60) + (kms_usados*0.15)
    return preco_total


def mostrar_preco_total(dias, kms, preco_total):
    print(f"O carro foi utilizado por {dias} dias")
    print(f"O carro andou {kms} kms")
    print(f"O valor gasto foi {preco_total} reais")


dias = int(input("Tempo de utilização do carro em dias: "))
kms = int(input("Quantidade de kms rodados no veículo: "))


preco_total = calculo_preco(dias=dias, kms=kms)
mostrar_preco_total(dias=dias, kms=kms, preco_total=preco_total)