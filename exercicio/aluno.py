from disciplinas import Disciplina


class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self. idade = idade
        self.matricula = matricula
        self.disciplinas = []

    def atribuir_disciplina(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
