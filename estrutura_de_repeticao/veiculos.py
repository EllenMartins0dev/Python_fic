from operator import itemgetter
import heapq
import json

veiculos = [
    {"veiculo": "Hb20", "valor_por_km": 0.89, "valor_por_dia": 67.90, "seguro": 129.90, "media_km_gasolina": 12,
     "media_km_etanol": 10},
    {"veiculo": "Mobi", "valor_por_km": 0.79, "valor_por_dia": 62.90, "seguro": 119.90, "media_km_gasolina": 15,
     "media_km_etanol": 13},
    {"veiculo": "Voyage", "valor_por_km": 1.09, "valor_por_dia": 89.90, "seguro": 79.90, "media_km_gasolina": 9,
     "media_km_etanol": 7},
    {"veiculo": "Spin", "valor_por_km": 0.99, "valor_por_dia": 99.90, "seguro": 109.90, "media_km_gasolina": 8,
     "media_km_etanol": 6},
    {"veiculo": "Cronos", "valor_por_km": 1.19, "valor_por_dia": 99.90, "seguro": 59.90, "media_km_gasolina": 11,
     "media_km_etanol": 9},
    {"veiculo": "Argo", "valor_por_km": 0.89, "valor_por_dia": 49.90, "seguro": 159.90, "media_km_gasolina": 13,
     "media_km_etanol": 11},
    {"veiculo": "Logan", "valor_por_km": 0.67, "valor_por_dia": 69.90, "seguro": 109.90, "media_km_gasolina": 10,
     "media_km_etanol": 8},
]

print(json.dumps(veiculos, sort_keys=True, indent=2))

distancia = 890
gasolina = 5.29
etanol = 3.39
dia_uso = 3

for veiculo in veiculos:
    carro = veiculo.get("veiculo")
    # dia de uso * valor por dia
    total_uso = veiculo.get("valor_por_dia")*dia_uso
    # valor uso gasolina
    total_gasolina = (distancia/veiculo.get("media_km_gasolina"))*veiculo.get("valor_por_km")*gasolina
    # valor uso etanol
    total_etanol = (distancia/veiculo.get("media_km_gasolina"))*veiculo.get("valor_por_km")*etanol
    print(f"\nVocê vai gastar com o carro {carro}, {total_uso:.2f} reais por dia, {total_gasolina:.2f} "
          f"reais com gasolina e {total_etanol:.2f} reais com etanol. Valor total da viagem com gasolina:"
          f" {total_uso + total_gasolina} ou valor total da viagem com etanol: {total_uso + total_etanol}:")

# Printa os 3 menores valores da lista
menores_dicionarios = heapq.nsmallest(3, veiculos, key=itemgetter('veiculo'))
print("Os 3 menores dicionários:")
for dicionario in menores_dicionarios:
    print(f"Menor custo: {dicionario}")
    """"
    A função heapq.nsmallest() é usada para obter os 3 dicionários com os menores valores em 'chave1', 
    usando itemgetter('chave1') como a função de chave. O resultado é armazenado na lista 
    menores_dicionarios e, em seguida, é percorrida em um loop para imprimir cada um dos dicionários.
    """

# Printa os valores em ordem crescente
lista_ordenada = sorted(veiculos, key=lambda x: x['veiculo'])
print("Lista de dicionários ordenada:")
for dicionario in lista_ordenada:
    print(dicionario)

""""
Usar a função sorted() com o parâmetro key para especificar 
a chave pela qual você deseja ordenar os dicionários.
"""