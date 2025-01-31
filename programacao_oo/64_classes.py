from cliente import Cliente
from conta import Conta

cliente01 = Cliente("Alfredo", "123.123.123-43", "23.346.456-5", "alfredo@gmail.com", True)
cliente02 = Cliente("Ana", "343.343.343-34", "23.543.765-3", "ana@gmail.com", True)
cliente03 = Cliente("Helen", "987.934.333-08", "72.673.245-0", "helen@gmail.com", True)
cliente04 = Cliente("Peter", "294.958.435-16", "20.230.167-1", "peter_hollywood@gmail.com", True)

clientes = [
    cliente01, cliente02, cliente03, cliente04
]

for cliente in clientes:
    print(cliente)

conta01 = Conta(nome="Conta corrente", descricao="Esta é a conta corrente do senhor Alfredo", saldo=5000,
                cliente=cliente01)
conta02 = Conta(nome="Conta corrente", descricao="Esta é a conta corrente do senhora Ana", saldo=1290.99,
                cliente=cliente02)
conta03 = Conta(nome="Conta poupança", descricao="Esta é a conta corrente do senhora Helen", saldo=600.12,
                cliente=cliente03)
conta04 = Conta(nome="Conta corrente", descricao="Esta é a conta corrente do senhor Peter",
                saldo=5678987654.00, cliente=cliente04)


conta01.depositar(3000)
conta01.sacar(50)
conta01.get_extrato()
print(f"O saldo da conta do(a) Sr(a) {cliente01.nome} é {conta01.get_saldo()}")
conta02.sacar(200)
conta02.depositar(12.01)
conta02.get_extrato()
print(f"O saldo da conta do(a) Sr(a) {cliente02.nome} é {conta02.get_saldo()}")
conta03.depositar(120)
conta03.get_extrato()
print(f"O saldo da conta do(a) Sr(a) {cliente03.nome} é {conta03.get_saldo()}")
conta04.sacar(5678987654.01)
conta04.get_extrato()
print(f"O saldo da conta do(a) Sr(a) {cliente04.nome} é {conta04.get_saldo()}")

if conta01.saldo and conta02.saldo and conta03.saldo and conta04.saldo < 0.0:
    print(f"Saldo da conta insuficiente")

elif conta01.saldo >= 0.0:
    print(f"Cliente:{cliente01.nome}. Saldo disponível: {conta01.saldo:.2f}")

elif conta02.saldo >= 0.0:
    print(f"Cliente:{cliente02.nome}. Saldo disponível: {conta02.saldo:.2f}")

elif conta03.saldo >= 0.0:
    print(f"Cliente:{cliente03.nome}. Saldo disponível: {conta03.saldo:.2f}")

elif conta04.saldo >= 0.0:
    print(f"Cliente:{cliente04.nome}. Saldo disponível: {conta04.saldo:.2f}")
