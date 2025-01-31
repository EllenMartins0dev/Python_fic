from aluno import Aluno


class Curso:
    def __init__(self, nome: str):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)
