# Exemplo de uso de classe em python

from carro import Carro
from aluno import Aluno
from atividade import Atividade
from disciplina import Disciplina

carro1 = Carro()
carro2 = Carro()
print(f"Carro: {carro1.marca}")

aluno01 = Aluno("Elias dos Santos", 19, "elias@gmail.com")
aluno02 = Aluno("Maria dos Santos", 17, "maria@gmail.com")
aluno03 = Aluno(idade=16, nome="Suzana", email="suzaninhax2@gmail.com")
gabriel_fonseca = Aluno("Gabriel Fonseca", 16, "gabriel@gmail.com")
joao_pedro_mendes = Aluno("João Pedro Mendes", 16, "joaozinho@gmail.com")
ellen = Aluno("Ellen", 16, "ellen@gmail.com")
sarah = Aluno("Sarah", 16, "sarah@gmail.com")

print(f"Alunos: {aluno01.nome}, {aluno02.nome}")

atividade_logica = Atividade('Resolver atividade de lógica de programação')
atividade_poo = Atividade("Criar classes POO", 8.0)
atividade_html = Atividade(descricao_atividade='Criar página HTML', nota_maxima_atividade=7.0)

d_atv_upper = atividade_html.descricao.upper()
print(atividade_html, d_atv_upper)

poo = Disciplina(nome="Programação Orientada Objeto")
print(f"1: {poo}")
poo.aprovar()
print(f"2: {poo}")
poo.atribuir_curso("Técnico Desenvolvimento Sistemas")
print(f"3: {poo}")
