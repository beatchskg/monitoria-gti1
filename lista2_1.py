peso_oitenta = 0
soma = 0

pessoas = int(input("Informe a quantidade de pessoas"))

for i in pessoas:
    peso = float(input("Informe seu peso."))
    soma += peso

media = soma/pessoas
print (f"A média de pesos é {media}")
    
if peso > 80:
    peso_oitenta += 1
    print (f"A quantidade de pessoas acima de 80kg é {peso_oitenta}.")
