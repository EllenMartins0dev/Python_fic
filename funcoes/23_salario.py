def calculo_aumento_salario(**kwargs):
    salario_liquido = kwargs.get("salario_atual")
    percentual_aumento = kwargs.get("percentual")
    aumento_salario = salario_liquido + (salario_liquido * percentual_aumento/100)
    return aumento_salario


salario = float(input("Digite seu salário: "))
porcentagem = float(input("Digite o percentual de aumento: "))


def mensagem(salario, porcentagem, aumento_salario):
    print(f"---- Informações salário ----")
    print(f"Seu antigo salário é {salario}")
    print(f"O percentual de aumento é {porcentagem}")
    print(f"Seu novo salário é {aumento_salario} reais.")


aumento_salario = calculo_aumento_salario(salario_atual=salario, percentual=porcentagem)
mensagem(salario=salario, porcentagem=porcentagem, aumento_salario=aumento_salario)
