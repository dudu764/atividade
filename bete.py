funcionarios = {}

for i in range(int(input("Quantos funcionários? "))):
    nome = input("Nome: ")
    salario = float(input("Salário: R$ "))
    funcionarios[nome] = salario

for nome, salario in funcionarios.items():
    print(f"{nome}: R$ {salario:.2f}")

while True:
    nome = input("Nome para ver o salário: ")
    if nome in funcionarios: