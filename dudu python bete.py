class cliente:
    def __init__(self,nome, telefone ):
        self.nome = nome
        self.telefone = telefone



def info (self):
    print("informacao do cliente")
    print(f"nome:  {self.nome}")
    print(f"telefone:  {self.telefone}")




    c1 = cliente ("eduardo", "87996610312")
    c1.info()
    print(c1.nome, c1.telefone)

    nome =input("informe seu nome")
    telefone =input("informe seu telefone")
    c1 =cliente(nome , telefone)
    c1.info()