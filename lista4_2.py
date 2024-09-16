#Faça uma função que receba uma lista de números e dois valores (limite inferior e limite superior). A função deverá retornar uma lista cujo os
#elementos são maiores ou iguais ao limite inferior e menores ou iguais ao limite superior. No programa principal (= fora da função), informe 10 números inteiros,
#armazenando-os numa lista. Informe também o limite inferior e o limite superior. Teste a função implementada e exiba o resultado.


def delimitador (lista_de_numeros, limite_inferior, limite_superior):
    nova_lista = list() # = nova_lista = []
    for num in lista_de_numeros: # for i in range()
        if num >= limite_inferior and num <= limite_superior:
            nova_lista.append(num)
    return nova_lista

#main
lista = []

for i in range(10): #o i inicial = 0, i final = 9
    numero = int(input(f"Informe o {i+1} número.")) 
    lista.append(numero) #nome_do_vetor.append(elemento_que_quero_adicionar)

lower = int(input("Informe o limite inferior.")) 
higher = int(input("Informe o limite superior.")) 

nova_lista = delimitador(lista, lower, higher)
print(f"A lista é: {nova_lista}.")

