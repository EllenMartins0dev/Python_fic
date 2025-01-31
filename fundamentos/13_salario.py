salario_atual = input("Digite seu salario atual: ")
percetual_aumento = input("Digite o percentual de aumento: ")

salario_com_aumento = float(salario_atual) + (float(salario_atual) * float(percetual_aumento) / 100)

print("---- Informações do salário ----")
print(f"Seu salário atual é {salario_atual}")
print(f"Seu percentual de aumento é {percetual_aumento}")
print(f"O salário com o aumento será: {salario_com_aumento}")

