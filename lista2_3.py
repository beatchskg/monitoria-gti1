cont = 0
soma = 0
menor_idade = 150
maior_idade = 0

for i in range (6):
    idade = int(input("Informe sua idade."))
    if idade:
        cont += 1
        soma = soma + idade

        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade

media = soma/cont
print (f"Foram lidas {cont} idades.")
print (f"A média das idades é de {media:.2f}.")
print (f"A pessoa mais velha é {maior_idade}.")
print (f"A pessoa mais nova é {menor_idade}")
