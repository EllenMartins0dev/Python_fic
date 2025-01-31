""""
Exemplo de criação de arquivo com python
MODO  OPERAÇÃO
r     leitura
w     escrita
a     escrito, mas preserva de conteúdo
"""
nome_arquivo = "numeros.txt"
arquivo = open(nome_arquivo, "w")

for numero in range(1, 101):
    arquivo.write(f'{numero}\n')

arquivo.close()
