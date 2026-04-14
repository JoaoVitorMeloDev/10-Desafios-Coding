# Na parte do mostrar_dados(): dentro dos () Parenteses deveria existir o self

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def mostrar_dados():
        print(f"{self.nome} - {self.quantidade}")

p1 = Produto("Teclado", 5)
p1.mostrar_dados()

#-------------------------------------------------------------#-------------------------------------------------------------#

# Adicionado o self dentro do def mostrar_dados()
class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def mostrar_dados(self):
        print(f"{self.nome} - {self.quantidade}")

p1 = Produto("Teclado", 5)
p1.mostrar_dados()

#Por que minha solução é melhor - Permite acessar os atributos do objeto corretamente, Segue o padrão da programação orientada a objetos, Evita erro de execução.
