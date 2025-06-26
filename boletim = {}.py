boletim = {}
qtd_alunos = int(input("Informe a quantidade de  alunos que deseja cadastrar: "))
for i in range(qtd_alunos):
    nome = input("Informe o nome do aluno: ")
    nota = float(input(f"Informe a nota(entre 0 e 10) do aluno {nome}: "))
    boletim[nome] = nota




print("-"*50)
for nome, nota in boletim.items():
    print(f"o aluno {nome} tem nota igual a {nota} ")
print("-"*50)
busca_aluno = input("Informe o nome do aluno para saber sa sua nota: ")
if busca_aluno in boletim:
    print(f"A nota do aluno {busca_aluno} é: {boletim[busca_aluno]}  ")
print("-"*50)

else:
    
    print("O nome informado nao esta cadastrado!")
    print("-"*50)
