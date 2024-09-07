#Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos.

numeros = [] #abrindo um vetor
negativo = 0 #iniciando um contador de números negativos
positivo = 0 #iniciando um contador de números positivos

for i in range(10): #utilizando a função for pois o enunciado determinou a quantidade de números reais a serem inseridos
    respostas = float(input("Digite um número real:")) #coletando os números inseridos pelos usuários
    numeros.append(respostas) #adicionando as respostas dos usuários ao vetor
#lembrete: há a possibilidade de fazer diretamente assim: numeros.append(float(input("Digite um número real:")))

for elementos in numeros: #esse for rodará dentro do próprio vetor criado, analisando cada elemento que fora adicionado nele para que possamos responder a questão
    if elementos < 0: #criando condicional para descobrir quantos números inseridos foram negativos 
        negativo = negativo + 1 
  #quando iniciamos o código, o contador "negativo" estava em 0. Agora, cada vez que um número negativo for identificado no vetor, o contador rodará uma vez.
  #lembrete: poderíamos ter utilizado "negativo += 1"
    elif elementos > 0:
        positivo = positivo + elementos 
    #de maneira similar ao contador do negativo, o do positivo também iniciou em zero. Contudo, quando um número positivo for identificado, ele não apenas rodará "1" no contador,
    #ele adicionará o número do elemento, somando, assim, os elementos positivos.
    #lembrete: poderíamos ter utilizado "positivo += elementos"
print(f'A quantidade de numeros negativos foi {negativo}.')
print(f'A soma dos numeros positivos é {positivo}')
