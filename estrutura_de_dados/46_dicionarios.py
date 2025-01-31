aluno = dict(nome="Sérgio", idade=18, matriculado=True)
print(f"Informações do Aluno: {aluno}")

aluno_eletrica = {
    "nome": "Elias Silvia Santos",
    "idade": 17,
    "cidade": "Piracicaba",
    "curso": "Elétrica",
    "disciplinas": ["CLP", "Comandos Elétricos"],
    "matriculado": True,
    "dias_do_curso": {
        "segunda": True,
        "terca": False
    }
}

print(f"Informações do aluno de elétrica: {aluno_eletrica}\n")

# Acessando as propriedades
nome = aluno_eletrica.get("nome")
print(f"O aluno chama-se {nome}")
print(f"Idade aluno: {aluno_eletrica.get('idade')}")
print(f"O aluno esta no curso {aluno_eletrica.get('curso', 'Não tem a propriedade')}")

# Acessando itens
aluno_eletrica['curso'] = "Desenvolvimento de Sistema"
print(f"Novas informações {aluno_eletrica}")
