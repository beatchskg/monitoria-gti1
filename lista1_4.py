roupas = int(input("Digite a quantidade de roupas compradas."))
valor = float(input("Digite quanto você gastou."))
codigo = int(input("Digite o código da condição de pagamento optada."))

if roupas > 2:
    if codigo == 1:
        valor_final = valor * 0.8
        print (f"O desconto foi aplicado e o novo valor da sua compra é de {valor_final}!")
    else:
        print (f"Não houve aplicação de desconto à sua compra. Foi pago o valor total de {valor}, no crédito.")
else:
    print ("Sua compra não atende aos requisitos do desconto.")
