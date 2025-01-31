dia = input("Digite o dia de seu nascimento: ")
mes = input("Digite o mês de seu nascimento: ")
idade = input("Digite sua idade: ")

mes_em_dias = int(mes)*30
anos_em_dias = int(idade)*365

total_de_dias = int(dia) + mes_em_dias + anos_em_dias

print("---- Quanto você viveu em dias ----")
print(f"Dia: {dia}")
print(f"Mês: {mes_em_dias}")
print(f"Ano: {anos_em_dias}")
print(f"Soma total de dias: {total_de_dias}")


