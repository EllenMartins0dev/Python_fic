from aluno import Aluno
from disciplinas import Disciplina
from curso import Curso

curso_python = Curso("Proframação em Python")
gustavo = Aluno("Gustavo", 16, 1234)
gustavo.atribuir_disciplina(Disciplina("Fundamentos Python", 3.4, 9.8))
gustavo.atribuir_disciplina(Disciplina("POO com Python", 3.7, 9.9))


gabriel = Aluno("Gabriel", 16, 4567)
gustavo.atribuir_disciplina(Disciplina("Fundamentos Python", 6.4, 5.8))
gustavo.atribuir_disciplina(Disciplina("POO com Python", 6.7, 8.9))

curso_python.adicionar_aluno(gustavo)
curso_python.adicionar_aluno(gabriel)

for aluno in curso_python.alunos:
    print(f"---- Aluno: {aluno.nome} ----")
    for disciplinas in aluno.disciplinas:
        print(f"Notas: {disciplinas.nota1}, {disciplinas.nota2}")
        print(f"Media: {disciplinas.media:.2f}")
        if disciplinas.verificar_aprovado():
            print(f"Aluno {aluno.nome} aprovado")
        else:
            print(f"Aluno {aluno.nome} reprovado")

curso_eletrica = Curso("Elétrica")
aluno03 = Aluno("Aluno03", 17, 7890)
aluno03.atribuir_disciplina(Disciplina("CLP", 4.5, 7.8))
aluno03.atribuir_disciplina(Disciplina("Comandos", 7.2, 8.9))
curso_eletrica.adicionar_aluno(aluno03)

aluno04 = Aluno("Aluno04", 18, 5130)
aluno04.atribuir_disciplina(Disciplina("CLP", 3.2, 1.2))
aluno04.atribuir_disciplina(Disciplina("Comandos", 3.4, 8.9))
curso_eletrica.adicionar_aluno(aluno04)

for aluno in curso_eletrica.alunos:
    print(f"---- Aluno: {aluno.nome} ----")
    for disciplinas in aluno.disciplinas:
        print(f"Notas: {disciplinas.nota1}, {disciplinas.nota2}")
        print(f"Média: {disciplinas.media}")
        if disciplinas.verificar_aprovado:
            print(f"Aluno aprovado com média {disciplinas.media}")
        else:
            print(f"Aluno reprovado com média {disciplinas.media}")
