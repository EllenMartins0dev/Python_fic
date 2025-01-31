import csv

nome_arquivo = ""

with open(nome_arquivo, 'r', encoding="UTF8", newline="") as file:
    leitor = csv.reader(file, delimiter=",")
    for linha in leitor:
        print(linha)
