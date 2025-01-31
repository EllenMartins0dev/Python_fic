import csv

cabecalho = []
dados_para_arquivo_alunos_com_media = []
nome_arquivo = "notas.csv"

with open(nome_arquivo, 'r', encoding="UTF8", newline="") as file:
    leitor = csv.reader(file, delimiter=",")
    for indice, linha in enumerate(leitor):
        if indice == 0:
            cabecalho = linha
        else:
            aluno = linha[0]
            disciplina = linha[1]
            nota1 = int(linha[2])
            nota2 = int(linha[3])
            media = (nota1 + nota2)/2
            linha_salva = [aluno, disciplina, nota1, nota2, media]
            dados_para_arquivo_alunos_com_media.append(linha_salva)

# criando arquivo novo com media
with open("74_notas_com_media.csv", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho.append("MEDIA")
    escritor.writerow(cabecalho)

    for linha in dados_para_arquivo_alunos_com_media:
        escritor.writerow(linha)

""""
1. Criar o arquivo 74_notas_aprovados.csv
2. Verificar se a média é maior ou igual a 5.5
"""

# criar arquivo para imprimir os alunos aprovados
with open("74_notas_aprovados.csv", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    cabecalho.append("Aprovado")
    escritor.writerow(cabecalho)

    for linha in dados_para_arquivo_alunos_com_media:
        media = linha[4]
        if media >= 5.5:
            linha.append("Aprovado")
            escritor.writerow(linha)

# criar arquivo para imprimir os alunos reprovados
with open("74_notas_reprovados.csv", "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    # usando o índice - acrescentando uma posição
    # cabecalho[5] = "Reprovado"
    # escritor.writerow(cabecalho)
    # usando o pop (apaga o último valor)
    cabecalho.pop(4)
    cabecalho.append("Reprovado")
    for linha in dados_para_arquivo_alunos_com_media:
        media = linha[4]
        if media < 5.5:
            linha.append("Reprovado")
            escritor.writerow(linha)

# Criar arquivo para selecionar apenas os de POO
with open("74_notas_POO", 'w', encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    for linha in dados_para_arquivo_alunos_com_media:
        disciplina = linha[1]
        if disciplina == "POO":
            escritor.writerow(linha)
