# O erro está na linha 7 onde a variável quantidade não consegue ser chamado pelo qtd porquê os nomes são diferentes
# e quando o valor da variável é int (inteiro) o + não funciona tendo que ser substituido por , {} ou quantidade = "10" ao invés de = 10

nome = "Pizza"
quantidade = 10

print("Produto: " + nome)
print("Quantidade: " + qtd)

#-------------------------------------------------------------#-------------------------------------------------------------#

# Trocando o = 10 por "10"
nome = "Pizza"
quantidade = "10"

print("Produto: " + nome)
print("Quantidade: " + quantidade)

# Trocando o + por ,
nome = "Pizza"
quantidade = 10

print("Produto: " + nome)
print("Quantidade:", quantidade)

#Por que minha solução é melhor - Corrige o nome da variável, evita erro de referência, Usa (,) no print, que já trata diferentes tipos automaticamente Mantém o tipo int, o que é mais correto.
