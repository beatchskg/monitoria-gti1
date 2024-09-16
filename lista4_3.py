import os
os.system('cls')

#Desenvolva uma função que permita receber uma variável
#inteira X inúmeras vezes ( = WHILE TRUE!!!!!) 
# #(deve parar quando o valor digitado for igual a zero) = WHILE TRUE!!!!. 
# Como retorno da função, para cada valor lido deverá ser
#imprimido a sequência de 1 até X (o número digitado), com um espaço
#entre cada número e seu sucessor.

def sequencia(x):
    for i in range(1, x+1): 
        print(i, end=" ")
    print()

#main
while True:
    x = int(input("Informe um número."))
    if x != 0:
        sequencia(x)
    else:
        break
