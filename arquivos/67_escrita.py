alunos = ["Alfredro", "Silas", "Maria", "Humberto"]

nome_arquivo = "docs/arquivo.txt"

with open(nome_arquivo, "w") as arquivo:
    for aluno in alunos:
        arquivo.write(f'{aluno} \n')
