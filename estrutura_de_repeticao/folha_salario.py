cargos = [
    {"cargo": "Gerente", "salario": 6890},
    {"cargo": "Programador", "salario": 4290},
    {"cargo": "Assistente RH", "salario": 2990},
    {"cargo": "Diretor", "salario": 12490},
    {"cargo": "Vendedor", "salario": 3670.99},
]

salario_atual = 0
for cargo in cargos:
    cargo_atual = cargo.get("cargo")
    salario_atual = cargo.get("salario")


descontos = [
     {"desconto": "vale_transporte", "valorVT": 1.09},
     {"desconto": "vale_refeicao", "valorVR": 1.89},
     {"desconto": "plano_odontologico", "valorPO": 29.90},
     {"desconto": "plano_de_saude", "valorPS": 109.90}
]

for desconto in descontos:
    vale_transporte = desconto.get("valorVT")
    vale_refeicao = desconto.get("valorVR")
    plano_odontologico = desconto.get("valorPO")
    plano_de_saude = desconto.get("valorPS")


funcionarios = [
    {"nome": "Alfredo", "dependentes": 3, "vale_transporte": "Sim"},
    {"nome": "Eliza", "dependentes": 2, "vale_transporte": "Não"},
    {"nome": "Silas", "dependentes": 4, "vale_transporte": "Não"},
    {"nome": "Francisco", "dependentes": 5, "vale_transporte": "Sim"},
    {"nome": "Maria", "dependentes": 1, "vale_transporte": "Não"},
    {"nome": "Danilo", "dependentes": 2, "vale_transporte": "Não"},
    {"nome": "Mariana", "dependentes": 3, "vale_transporte": "Sim"},
]

if salario_atual < 1320:
    percentual_INSS = 0.075
    percentual_IRPF = 0.025

elif salario_atual < 2571.29:
    percentual_INSS = 0.09
    percentual_IRPF = 0.045

elif salario_atual < 3856.94:
    percentual_INSS = 0.12
    percentual_IRPF = 0.085

elif salario_atual > 3856.94:
    percentual_INSS = 0.14
    percentual_IRPF = 0.145


for funcionario in funcionarios:
    nome = funcionario.get("nome")
    vale_transporte_ = funcionario.get("vale_transporte")
    dependentes = funcionario.get("dependentes")
    valor_plano_saude = desconto.get("valorPS") * dependentes
    valor_plano_odonto = desconto.get("valorPO") * dependentes
    desconto_total = salario_atual - (valor_plano_odonto + valor_plano_saude + percentual_INSS + percentual_IRPF)
