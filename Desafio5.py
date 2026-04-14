# Tem um diferente de != ao lado do nome.lower(): fazendo com que ele não retorne o produto

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() != nome.lower():
                return produto
        return "Produto não encontrado"
    
#-------------------------------------------------------------#-------------------------------------------------------------#   

# Substituindo o != por ==
class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return "Produto não encontrado"

# Por que minha solução é melhor - Corrige a lógica da busca, Garante que o produto retornado seja o correto, Evita resultados inesperados.
