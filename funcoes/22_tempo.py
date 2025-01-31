def calculo_segundos_totais(**kwargs):
    segundos = kwargs.get("segundos_usados")
    minutos = kwargs.get("minutos_usados")
    horas = kwargs.get("horas_usadas")
    dias = kwargs.get("dias_usados")
    minutos_em_seg = int(minutos)*60
    horas_em_seg = int(horas)*3600
    dias_sem_seg = int(dias)*(3600*24)
    segundos_totais_soma = int(segundos) + minutos_em_seg + horas_em_seg + dias_sem_seg
    return segundos_totais_soma


def mostrar_dados_em_seg(segundos_em_seg, minutos_em_seg, horas_em_seg, dias_em_seg, segundos_totais_soma):
    print(f"---- Informações ----")
    print(f"Segundos: {segundos_em_seg}")
    print(f"Minutos em segundos: {minutos_em_seg}")
    print(f"Horas em segundos: {horas_em_seg}")
    print(f"Dias em segundos: {dias_em_seg}")
    print(f"Soma total: {segundos_totais_soma}")


segundos_s = input("Digite os segundos: ")
minutos_s = input("Digite os minutos: ")
horas_s = input("Digite as horas: ")
dias_s = input("Digite os dias: ")

segundos_totais = calculo_segundos_totais(segundos_usados=segundos_s, minutos_usados=minutos_s,
                                          horas_usadas=horas_s, dias_usados=dias_s)

mostrar_dados_em_seg(segundos_em_seg=segundos_s, minutos_em_seg=minutos_s, horas_em_seg=horas_s,
                     dias_em_seg=dias_s, segundos_totais_soma=segundos_totais)
