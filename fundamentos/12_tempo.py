dias = input("Digite a quantidade de dias: ")
horas = input("Digite a quantidade de horas: ")
minutos = input("Digite a quantidade de minutos: ")
segundos = input("Digite a quantidade de segundos: ")

minutos_em_segundos = int(minutos)*60
horas_em_segundos = int(horas)*3600
dias_em_segundos = int(dias)*86400

total_de_segundos = int(segundos) + minutos_em_segundos+horas_em_segundos+dias_em_segundos
print("---- Informações em segundos ----")
print(f"Dias: {dias_em_segundos}")
print(f"Horas: {horas_em_segundos}")
print(f"Minutos: {minutos_em_segundos}")
print(f"Segundos: {segundos}")
print(f"Soma total: {total_de_segundos}")
