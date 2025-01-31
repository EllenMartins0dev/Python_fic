import csv

nome_arquivo = "docs/temperaturas.csv"
cabecalho = ["DIA DA SEMANA", "TEMPERATURA"]
dados = [
    {"dia": "Segunda-Feira", "temperatura": 13.2},
    {"dia": "Terça-Feira", "temperatura": 27.8},
    {"dia": "Quarta-Feira", "temperatura": 13.8},
    {"dia": "Quinta-Feira", "temperatura": 22.9},
    {"dia": "Sexta-Feira", "temperatura": 18.9},
    {"dia": "Sábado", "temperatura": 18.7},
    {"dia": "Domingo", "temperatura": 9.9}
]

with open(nome_arquivo, "w", encoding="UTF8", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(cabecalho)

    for dado in dados:
        dia = dado.get("dia")
        valor = dado.get("temperatura")
        escritor.writerow([dia, valor])
