#2. Crie um programa que vai ler vários números e colocá-los em uma lista até que -1 seja digitado (não deve ser adicionado). Depois disso, mostre:
#a) quantos números foram digitados.
#b) a lista de valores, ordenada de forma decrescente
#c) se o valor 5 está ou não na lista

numeros = [] #como determinado na questão, abrimos um vetor para armazenar as informações que serão coletadas

while True:
#a utilização de while True se dá por dois motivos: 
#o primeiro, porque não há especificação de vezes que iremos colher a informação no enunciado. 
#a segunda, porque temos o comando que irá encerrar o loop
    informacoes = float(input("Informe um número aleatório. Ao inserir -1 o loop encerra.")) #colhendo as informações dos usuários
    if informacoes != -1: #há uma parte importante na questão que fala "o -1 não deve ser inserido na lista", logo, devemos criar uma regra para que isso não aconteça.
        numeros.append(informacoes)
    #a condicional aqui criada, então, serve como fato de exclusão do -1 no momento em que formos adicionar ao vetor, através do .append, as informações coletadas, uma vez
    #que ela diz que apenas numeros DIFERENTES de -1 serão adicionados
    elif informacoes == -1: #aqui também poderíamos utilizar o "else"
        break

#a) quantos números foram digitados.

print(f"A quantidade de números digitados foi {len(numeros)}") 
#como a questão quer saber o TOTAL de informações armazenadas, utilizamos o len(nome_do_vetor), como explicado na questão anterior.

#b) a lista de valores, ordenada de forma decrescente

numeros.sort(reverse=True) 
#o comando nome_do_vetor.sort() o ordena em ordem CRESCENTE, a utilização do reverse=True garante que os itens armazenados no vetor apareçam em ordem DECRESCENTE
print (f"A ordem de números decrescente é {numeros}")

#c) se o valor 5 está ou não na lista
if numeros.count(5) <= 0: 
#fazendo uso do .count(), que conta o elemento específico dentro de uma lista, conseguimos verificar se a contagem é abaixo/igual a ZERO, de modo que o print é o seguinte:
    print("O número 5 não consta na lista.")
else: #utilizando do else, uma vez que, se a regra do if não for verdadeira, haverá número 5 na lista, e esse será o print:
    print(f"O número 5 foi inserido {numeros.count(5)}")
    


