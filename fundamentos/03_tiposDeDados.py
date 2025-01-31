""""exemplo de declaração de variável
com diferentes valores"""

nome = "Alfredo"
sobrenome = "Alves"
idade = 40
esta_empregado = True
salario_hora = 5.29
dados = [1, 4, "A", False]
dicionario = {"estudar": True, "tempo": "calor"}
nada = None

cidade = "Piracicaba"

print("A cidade", cidade, "tem", len(cidade), "letras")

indice_nove = cidade[9]

print("O indice nove da palavra", cidade, "é a letra", indice_nove)

estado = "São Paulo"
cidade_estado = "A cidade", cidade, "fica no estado de", estado

print(cidade_estado)


"""
Fazendo composição de strings de forma inteligente, argumentos:
%d para números inteiros
%s para strings
%f para números decimais
%f5.2 onde os números antes e depois do ponto formatam casas decimais
"""

print("Senhor %s tem %d anos, trabalha e ganha R$%5.2f de salário por hora"
      % (nome, idade, salario_hora))

"""
Fazendo a formatação de saída de outras formas
"""

print(f"Senhor {nome} tem {idade} anos, trabalha e ganha R$ {salario_hora} por hora")

print("Senhor {0} tem {1} anos e trabalha e ganha R$ {2}".format(nome, idade, salario_hora))
