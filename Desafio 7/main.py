from services.estoque import executar_rota


print(executar_rota("/produtos", "POST", {"nome": "Pizza", "quantidade": 10}))
print(executar_rota("/produtos", "GET"))