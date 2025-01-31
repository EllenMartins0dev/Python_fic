nome_arquivo = "docs/meu_arquivo_nao_existe.txt"

try:
    with open(nome_arquivo, "r", encoding="UTF8") as arquivo:
        for aluno in arquivo.readlines():
            print(f'Aluno {aluno}')

except FileNotFoundError:
    print(f"O arquivo não foi encontrado, verifique o caminho")
