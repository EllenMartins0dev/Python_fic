import json

animais = [
    {"animal": "Cachorro Pastor", "idade": 3, "fator_idade_humano": 12, "idade_de_humano": 0},
    {"animal": "Cachorro Fila", "idade": 4, "fator_idade_humano": 10, "idade_de_humano": 0},
    {"animal": "Cachorro Golden", "idade": 2, "fator_idade_humano": 8, "idade_de_humano": 0},
    {"animal": "Papagaio", "idade": 8, "fator_idade_humano": 5, "idade_de_humano": 0},
    {"animal": "Gato Siamês", "idade": 4, "fator_idade_humano": 7, "idade_de_humano": 0},
    {"animal": "Cachorro Husk", "idade": 3, "fator_idade_humano": 9, "idade_de_humano": 0},
]

for animal in animais:
    # idade * fator_idade_humano
    idade_de_humano = animal.get("idade")*animal.get("fator_idade_humano")
    animal["idade_de_humano"] = idade_de_humano
    eh_cachorro = animal.get("animal").startswith("Cachorro")

    if eh_cachorro and animal.get("idade_de_humano") >= 30:
        print("---- Informações Animal ----")
        print(json.dumps(animal, sort_keys=True, indent=2))
