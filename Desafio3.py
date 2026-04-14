# Falta o Parâmetro (self) não está dentro do campo dos parâmetros (nome, quantidade) após o init
# e não está sendo mostrado a quantidade do produto 1 quando o programa é rodado tendo que adicionar o print (p1.quantidade)

class Produto:
    def __init__(nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

p1 = Produto("Mouse", 10)
print(p1.nome)

#-------------------------------------------------------------#-------------------------------------------------------------#

# Adicionando o self e adicionando o p1.quantidade (tanto pode colocar embaixo com mais um () parênteses ou mostrar os dois juntos usando o ,)
class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

p1 = Produto("Mouse", 10)
print(p1.nome, p1.quantidade)
