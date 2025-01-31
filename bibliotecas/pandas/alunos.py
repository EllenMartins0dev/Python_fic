import pandas as pd

dados = pd.read_csv("alunos.csv", sep=";")

for index, row in dados.iterrows():
    nota1 = str(row['NOTA 1'])
    nota1 = nota1.replace(",", ".")
    print(type(nota1), nota1)
    nota2 = dados['NOTA 2']
    nota2 = nota2.replace(",", ".")
    nota2 = dados['NOTA 2'].astype(float)
    print(type(nota2), nota2)
    # media_colunas = dados[['NOTA 1', 'NOTA 2']].mean()
    # print(media_colunas)