# O erro está na linha 7 onde a variável quantidade não consegue ser chamado pelo qtd porquê os nomes são diferentes
# e quando o valor da variável é int (inteiro) o + não funciona tendo que ser substituido por , {} ou quantidade = "10" ao invés de = 10

nome = "Pizza"
quantidade = 10

print("Produto: " + nome)
print("Quantidade: " + qtd)

#-------------------------------------------------------------#-------------------------------------------------------------#

#Trocando o = 10 por "10"
nome = "Pizza"
quantidade = "10"

print("Produto: " + nome)
print("Quantidade: " + quantidade)

# Trocando o + por ,
nome = "Pizza"
quantidade = 10

print("Produto: " + nome)
print("Quantidade:", quantidade)
