def calculo_notas(**kwargs):
    nota1 = kwargs.get("nota1")
    nota2 = kwargs.get("nota2")
    nota3 = kwargs.get("nota3")
    nota4 = kwargs.get("nota4")
    calculo_notas_soma = ((nota1*0.15) + (nota2*0.25) + (nota3*0.4) + (nota4*0.2))/4
    return calculo_notas_soma


def mostrar_notas(nota1, nota2, nota3, nota4, calculo_notas_soma):
    print(f"---- Notas ----")
    print(f"Média nota final: {calculo_notas_soma}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Nota 3: {nota4}")


nota1 = float(input("Digite sua primeira nota (peso 15%): "))
nota2 = float(input("Digite sua segunda nota (peso 25%): "))
nota3 = float(input("Digite sua terceira nota (peso 40%): "))
nota4 = float(input("Digite sua quarta nota (peso 20%): "))

calculo_notas_soma = calculo_notas(nota1=nota1, nota2=nota2, nota3=nota3, nota4=nota4)
mostrar_notas(nota1=nota1, nota2=nota2, nota3=nota3, nota4=nota4, calculo_notas_soma=calculo_notas_soma)
