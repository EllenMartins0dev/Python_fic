def calcula_salario(**kwargs):
    desconto_inss = kwargs.get("inss")/100
    desconto_plano_de_saude = kwargs.get("plano")
    total_desconto = desconto_inss + desconto_plano_de_saude
    salario_liquido = kwargs.get("salario_base") - total_desconto
    return salario_liquido


salario_atual = 5000
INSS = 8
plano_s = 129.90
salario_a_receber = calcula_salario(salario_base=salario_atual, inss=INSS, plano=plano_s)

print(f"O salário é {salario_a_receber}")