# Adicionado as rotas produtos/atualizar pelo metodo PUT, rota de produtos/remover pelo metodo DELETE 
# e adicionando o return caso ele não encontre uma rota

def executar_rota(rota, metodo, dados=None):
    if rota == "/produtos" and metodo == "GET":
        return get_produtos()

    if rota == "/produtos" and metodo == "POST":
        return post_produto(dados["nome"], dados["quantidade"])

    if rota == "/produtos/buscar" and metodo == "GET":
        return get_produto_por_nome(dados["nome"])

#-------------------------------------------------------------#-------------------------------------------------------------#

#Adicionando as rotas e metodos e return caso não encontre nenhuma rota
def executar_rota(rota, metodo, dados=None):
    if rota == "/produtos" and metodo == "GET":
        return get_produtos()

    if rota == "/produtos" and metodo == "POST":
        return post_produto(dados["nome"], dados["quantidade"])

    if rota == "/produtos/buscar" and metodo == "GET":
        return get_produto_por_nome(dados["nome"])
    
    if rota == "/produtos/atualizar" and metodo == "PUT":
        return put_produto(dados["nome"], dados["quantidade"])

    if rota == "/produtos/remover" and metodo == "DELETE":
        return delete_produto(dados["nome"])

    return "Rota não encontrada"