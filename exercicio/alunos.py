class Alunos:
    def __init__(self, nome, matricula, curso, n1, n2, n3, n4):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = 0.0

    def media_disciplina1(self):
        media1 = (self.n1 + self.n2)/2

    def media_disciplina2(self):
        media2 = (self.n3 + self.n4)/2
