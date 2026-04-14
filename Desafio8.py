# Na classe de ProdutoDigital eu adicionei nome e quantidade que antes não estavam presentes

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


class ProdutoDigital(Produto):
    def __init__(self, nome, quantidade, tamanho_arquivo):
        self.tamanho_arquivo = tamanho_arquivo


p1 = ProdutoDigital("Curso Python", 1, "500MB")
print(p1.nome)
print(p1.quantidade)
print(p1.tamanho_arquivo)

#-------------------------------------------------------------#-------------------------------------------------------------#

# Adicionando o nome e quantidade no __init__ da classe ProdutoDigital e adicionei o super porque por algum motivo o def mostrardados não queria funcionar
class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


class ProdutoDigital(Produto):
    def __init__(self, nome, quantidade, tamanho_arquivo):
        self.tamanho_arquivo = tamanho_arquivo
        super().__init__(nome, quantidade)

p1 = ProdutoDigital("Curso Python", 1, "500MB")
print(p1.nome)
print(p1.quantidade)
print(p1.tamanho_arquivo)

#
