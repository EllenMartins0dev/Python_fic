import pandas as pd
from random import randrange

temperaturas = {}

for dia in range(1, 31):
    # adicionando números de 1 à 30 junto a string "dia_
    chave = "dia_" + str(dia)
    # criando uma chave para o dicionário temperaturas = {}
    temperaturas[chave] = []
    for valor in range(1, 501):
        temp = randrange(5, 35)
        temperaturas[chave].append(temp)

for dia, valores in temperaturas.items():
    print(f"\n{dia}:{valores}\n")

dataframe = pd.DataFrame(temperaturas)
dataframe.to_csv("temperaturas.csv")

print(f"Informações básicas: \n{dataframe.head()}")
print(f"Informações com n° de linhas definidas: \n{dataframe.tail(10)}")
print(f"Informações com estatística: \n{dataframe.describe()}")
    