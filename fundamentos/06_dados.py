nome = "Ellen"
sobrenome = "Martins"
idade = 16
endereco = "Rua Valinhos, N° 50, Cecap"
cidade = "Piracicaba"
estado = "São Paulo"

print(f"A aluna {nome} {sobrenome} tem {16} anos e mora na "
      f"{endereco} na cidade de {cidade}, estado de {estado}")

# informações em scanne
seu_nome = str(input("Digite seu nome:"))
seu_sobrenome = str(input("Digite seu sobrenome:"))
sua_idade = int(input("Digite sua idade:"))
seu_endereco = str(input("Digite seu endereço (Rua, número e bairro:"))
sua_cidade = str(input("Digite sua cidade:"))
seu_estado = str(input("Digite seu estado:"))

print(f"Seu nome é {seu_nome} {seu_sobrenome}, você tem {sua_idade} anos, mora em {seu_endereco}, na cidade de {sua_cidade}, no estado de {seu_estado}")
