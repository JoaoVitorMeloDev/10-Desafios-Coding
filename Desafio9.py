# Falta adicionar o def mostrar dados para mostrar que um é perecivel e o outro digital

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


class ProdutoPerecivel(Produto):
    pass


class ProdutoDigital(Produto):
    pass


produtos = [
    ProdutoPerecivel("Leite", 5),
    ProdutoDigital("Curso", 1)
]

for p in produtos:
    print("Produto:", p.nome, "-", p.quantidade)
    
#-------------------------------------------------------------#-------------------------------------------------------------#

#Adicionando o def mostrar dados

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    def mostrar_dados(self):
        print(f"{self.nome} - {self.quantidade}")

class ProdutoPerecivel(Produto):
     def mostrar_dados(self):
        print(f"{self.nome} (Perecível) - {self.quantidade}")


class ProdutoDigital(Produto):
    def mostrar_dados(self):
        print(f"{self.nome} (Digital) - {self.quantidade}")


produtos = [
    ProdutoPerecivel("Leite", 5),
    ProdutoDigital("Curso", 1)
]

for p in produtos:
    p.mostrar_dados()