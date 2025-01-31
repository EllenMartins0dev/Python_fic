"""
Exemplo de fatiamento de string em python
OBS: sempre precisa colocar uma posição a mais
"""

cidade = "Piracicaba"
primeiras_4_letras = cidade[0:4]
print(f"As primeiras 4 letras da palavra {cidade} são {primeiras_4_letras}")

outras_letras = cidade[2:6]
print(f"Outras letras {outras_letras}")

duas_ultimas_letras = cidade[-2:]
print(f"Duas últimas letras {duas_ultimas_letras}")