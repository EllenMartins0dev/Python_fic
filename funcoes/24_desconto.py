def calculo_desconto_salario(**kwargs):
    salario_liquido = kwargs.get("salario_atual")
    percentual_desconto = kwargs.get("percentual")
    desconto_salario = salario_liquido - (salario_liquido * percentual_desconto/100)
    return desconto_salario


salario = float(input("Digite seu salário: "))
porcentagem = float(input("Digite o percentual de desconto: "))


def mensagem(salario, porcentagem, desconto_salario):
    print(f"---- Informações salário ----")
    print(f"Seu antigo salário é {salario}")
    print(f"O percentual de desconto é {porcentagem}")
    print(f"Seu novo salário é {desconto_salario} reais.")


desconto_salario = calculo_desconto_salario(salario_atual=salario, percentual=porcentagem)
mensagem(salario=salario, porcentagem=porcentagem, desconto_salario=desconto_salario)
