aluno = {
    "nome": "Elias",
    "idade": 18,
    "curso": "Administração",
    "disciplinas": ["RH", "Excel", "Liderança"]
}

for chave, valor in aluno.items():
    print(f"Chave: {chave}, valor: {valor}")

    if chave == "disciplinas":
        for disciplina in aluno.get("disciplinas"):
            print(f"Disciplina: {disciplina}")

    else:
        print(f"chave: {chave}, valor {valor}")
