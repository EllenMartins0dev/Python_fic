import csv

nome_arquivo = "docs/dedoboll.csv"
cabecalho = ["CRIAR TURMA", "TABELA DEDO PONTOS LADO A", "TABELA DEDO PONTOS LADO B"]

dados = [
    {"turma": "DEV", "pontos_lado_a": 20, "pontos_lado_b": 10},
    {"turma": "Elétrica", "pontos_lado_a": 10, "pontos_lado_b": 52},
    {"turma": "Calderaria", "pontos_lado_a": 30, "pontos_lado_b": 12},
    {"turma": "Solda", "pontos_lado_a": 13, "pontos_lado_b": 9}
]

with open(nome_arquivo, "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(cabecalho)

    for dado in dados:
        pontos_lado_a = dado.get("pontos_lado_a")
        pontos_lado_b = dado.get("pontos_lado_b")
        # total_pontos_a = sum(pontos_lado_a.values)
        print(pontos_lado_a, pontos_lado_b)
        turma = dado.get("turma")

        escritor.writerow([turma, pontos_lado_a, pontos_lado_b])
