nome = input("Nome do viajante: ")
destinos = ["Paris", "NY", "Tóquio", "RJ", "Londres"]
for i, d in enumerate(destinos): print(f"{i+1} - {d}")
escolha = int(input("Destino nº: "))
print(f"{nome} escolheu {destinos[escolha - 1]}")


nome = input("Nome do solicitante: ")
livros = ["1984", "Dom Casmurro", "Harry Potter", "O Hobbit", "Capitães da Areia",
          "O Pequeno Príncipe", "It", "Memórias", "Senhor dos Anéis", "Revolução dos Bichos"]
for i, l in enumerate(livros): print(f"{i+1} - {l}")
escolha = int(input("Livro nº: "))
print(f"{nome} escolheu {livros[escolha - 1]}")


nome = input("Seu nome: ")
frutas = ["Banana", "Maçã", "Uva", "Abacaxi", "Melancia"]
for i, f in enumerate(frutas): print(f"{i+1} - {f}")
escolha = int(input("Fruta nº: "))
print(f"{nome} escolheu {frutas[escolha - 1]}")


class Contato:
    def __init__(self, nome, tel): self.nome, self.tel = nome, tel
    def __str__(self): return f"{self.nome} - {self.tel}"

class Agenda:
    def __init__(self): self.contatos = []
    def adicionar(self, nome, tel): self.contatos.append(Contato(nome, tel)) 
    def mostrar(self): [print(c) for c in self.contatos]

a = Agenda()
a.adicionar("Ana", "9999-0001")
a.adicionar("Leo", "9999-0002")
a.mostrar()


class Pessoa: 
    def __init__(self, nome): self.nome = nome
class Aluno(Pessoa): pass
class Professor(Pessoa): pass

class Curso:
    def __init__(self, nome): 
        self.nome, self.alunos, self.professores = nome, set(), set()
    def add_aluno(self, a): self.alunos.add(a.nome)
    def add_prof(self, p): self.professores.add(p.nome)
    def mostrar(self):
        print("Curso:", self.nome)
        print("Alunos:", self.alunos)
        print("Professores:", self.professores)

curso = Curso("Python")
curso.add_aluno(Aluno("Maria"))
curso.add_aluno(Aluno("João"))
curso.add_prof(Professor("Pedro"))
curso.mostrar()
