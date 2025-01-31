class Atividade:
    def __init__(self, descricao_atividade: str, nota_maxima_atividade=10.0):
        self.descricao = descricao_atividade
        self.nota_maxima = nota_maxima_atividade

    def __str__(self):
        return f"A atividade {self.descricao} tem a nota máxima de {self.nota_maxima}"


