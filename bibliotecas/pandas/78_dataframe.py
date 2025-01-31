from pandas import DataFrame, Series

notas_alunos = {
    "alunos": Series(data=["aluno01", "aluno02", "aluno03"]),
    "nota1": Series(data=[2.9, 2.2, 7.1]),
    "nota2": Series(data=[4.9, 2.8, 9.1]),
}

dataframe = DataFrame(notas_alunos)
print(f"Dados dos alunos: \n{dataframe}")

filtro_1 = DataFrame(notas_alunos, index=[1, 2])
print(f"\n\nFiltro 1: \n{filtro_1}")

filtro_2 = DataFrame(notas_alunos, columns=["alunos", "nota2"])
print(f"\n\nFiltro 2: \n{filtro_2}")
