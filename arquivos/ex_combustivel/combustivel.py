import csv

nome_arquivo = "combustiveis.csv"
dados_info_combustivel = []
cabecalho = []
distancia = 569
dias_uso = 3
gasolina = 5.19
etanol = 3.39

# ler arquivo
with open(nome_arquivo, 'r', encoding="UTF8", newline="") as file:
    leitor = csv.reader(file, delimiter=",")
    for indice, linha in enumerate(leitor):
        if indice == 0:
            cabecalho = linha
            cabecalho.append("QTDE_LITROS_GASOLINA")
            cabecalho.append("QTDE_LITROS_ETANOL")
            cabecalho.append("TOTAL_GASOLINA")
            cabecalho.append("TOTAL_ETANOL")
            cabecalho.append("VALOR_TOTAL_GASOLINA")
            cabecalho.append("VALOR_TOTAL_ETANOL")
        else:
            veiculo = linha[0]
            valor_por_km = float(linha[1].replace("R$", ""))
            valor_por_dia = int(linha[2].replace("R$", ""))
            seguro = int(linha[3].replace("R$", ""))
            media_gasolina = float(linha[4])
            media_etanol = float(linha[5])
            qtd_litros_gasolina_arredondado = int((distancia / media_gasolina))
            qtd_litros_etanol_arredondado = int((distancia / media_etanol))
            linha_salva = [veiculo, valor_por_km, valor_por_dia, seguro, media_gasolina,
                           media_etanol, qtd_litros_gasolina_arredondado, qtd_litros_etanol_arredondado]
            # calculando o total de gasolina e etanol em reais
            total_gasolina = qtd_litros_gasolina_arredondado*gasolina
            total_gasolina_format = f"{total_gasolina:.2f}"
            total_etanol = qtd_litros_etanol_arredondado*etanol
            total_etanol_format = f"{total_etanol:.2f}"

            linha_salva.append(total_gasolina_format)
            linha_salva.append(total_etanol_format)

            # Calculando valor de dias por veículo
            valor_dias = dias_uso*valor_por_dia

            # Calculando valor de km por veículo
            valor_km_veiculo_total = distancia*valor_por_km

            # Calculando valor total para gasolina e veiculo

            # Considerando todas as variáveis, dias, km, seguro, toal_gasolina
            valor_total_gasolina_veiculo = valor_km_veiculo_total + valor_dias + seguro + float(total_gasolina_format)
            valor_total_gasolina_veiculo_format = f"R${valor_total_gasolina_veiculo}"

            valor_total_etanol_veiculo = valor_km_veiculo_total + valor_dias + seguro + float(total_etanol_format)
            valor_total_etanol_veiculo_format = f"R${valor_total_etanol_veiculo}"

            dados_info_combustivel.append(linha_salva)

# criando arquivo novo com litros necessários de gasolina e etanol
with open(nome_arquivo, "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(cabecalho)

    for linha_salva in dados_info_combustivel:
        escritor.writerow(linha_salva)
