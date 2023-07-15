# ######################################################################
# ### ------------------------------------------------------------- ####
# ### Potência Tech powered by iFood | Ciências de Dados com Python ####
# ### _____________________________________________________________ ####
# ######################################################################

# %%
# ######################################################################
# #########---- Exercicio 1 - Tempo Estimado de Entrega ----############
# ######################################################################
nomeRestaurante = input()
tempoEstimadoEntrega = int(input())

mensagem = f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos."
print(mensagem)

# %%
# ######################################################################
# #####---- Exercicio 2 - Calcular o Preço Final de um Pedido ----######
# ######################################################################
valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

# Calcular o preço final do pedido:
# (total dos hambúrgueres + total das bebidas).

totalH = (valorHamburguer * quantidadeHamburguer) 
totalB = (valorBebida * quantidadeBebida)

totalPagar = totalH + totalB

# Calcular o troco do pedido, considerando o preço final
# e o valor pago pelo usuário.

troco = (valorPago - totalPagar)

# Imprimir a saída no formato especificado neste desafio.

print(f"O preço final do pedido é R$ {totalPagar:.2f}. Seu troco é R$ {troco:.2f}.")
# %%
# ######################################################################
# #####-------- Exercicio 3 - Ganhe uma Sobremesa Especial -------######
# ######################################################################


valorPedido = float(input("Qual é o valor total do pedido? "))

if valorPedido >= 50:
  mensagem = f"Parabens, você ganhou uma sobremesa gratis!"
else:
  mensagem = f"Que pena, você nao ganhou nenhum brinde especial."

print(mensagem)
# %%
# ######################################################################
# ##----- Exercicio 4 - Gerenciamento de Pedidos de Comida Online ----##
# ######################################################################
def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
    # Cria as condições para aplicar o cupom de desconto (10% ou 20%).
    cupom = input("Qual é o cupom de desconto? ")
    if cupom == "10%":
        total *= 0.9
    elif cupom == "20%":
        total *= 0.8
 
    print("Valor total: {:.2f}".format(total))
 
 
if __name__ == "__main__":
    main()
# %%
# %%
# ######################################################################
# #######----- Exercicio 5 - Identificando Pedidos de Vegano ----#######
# ######################################################################

numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input("O prato é vegano? (s/n) ") == "s"

    print(f"Pedido {i}: {prato} ({'Vegano' if ehVegano else 'Não-vegano'}) - {calorias} calorias")
# %%
