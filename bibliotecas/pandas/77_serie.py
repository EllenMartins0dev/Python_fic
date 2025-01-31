import pandas as pd

notas = [3.9, 2.0, 1.3, 7.8, 9.0]
serie = pd.Series(data=notas)
print(f"A informação contida na série é \n{serie}")
print(f"\nEstatística: \n{serie.describe()}")
print(f"\nValor mínimo: \n{serie.min()}")
print(f"\nValor máximo: \n{serie.max()}")
print(f"\nMédia: \n{serie.mean()}")

notas_alunos = {
    "aluno01": 6.9,
    "aluno02": 2.9,
    "aluno03": 1.2,
    "aluno04": 9.9,
}
serie_alunos = pd.Series(notas_alunos)
print(f"\n\nA informação da série é \n{serie_alunos}")
estatistica_notas = serie.to_string(float_format="{:.6f}".format)
print(f"\nEstatística notas: \n{estatistica_notas}")
print(f"\nNota mínima: \n{serie_alunos.min()}")
print(f"\nNota máxima: \n{serie_alunos.max()}")
print(f"\nMédia das notas: \n{serie_alunos.mean():.2f}")


