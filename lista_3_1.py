# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Linux
# 3- Mac OS
# 4- Outro

# Você foi contratado para desenvolver um programa (utilizando vetores) que leia o resultado da enquete e informe ao final o resultado da mesma. O programa 
# deverá ler os votos até ser informado o valor 0, que encerra a entrada dos dados. Os valores referentes a cada uma das opções devem ser armazenados
# num vetor. Após os dados terem sido informados, o programa deverá calcular o total de votos de cada um dos concorrentes.

codigo_so = [] #abrindo o vetor que irá armazenar as informações colhidas no input

while True: 
#a utilização de while True se dá por dois motivos: o primeiro, porque não há especificação de vezes que iremos colher a informação no enunciado. a segunda, porque temos o comando que irá encerrar o loop
    sistemas_escolhidos = int(input("Qual o melhor Sistema Operacional para uso em servidores? Escolha 1 - Windows, 2 - Linux, 3 - Mac OS, 4 - Outros. Escolha 0 para encerrar o programa."))
    if sistemas_escolhidos != 0: 
#a questao determina que o número 0 encerra o programa, logo, todo número diferente de zero (e dentre os determinados na pergunta), deverão ser contabilizados
        codigo_so.append(sistemas_escolhidos) #o comando .append adiciona a informação coletada na variável acima (sistemas_escolhidos) ao vetor criado
    elif sistemas_escolhidos == 0: #como dito na questão, ao inserir o número "0", o sistema para de rodar. Nesse caso, também poderíamos fazer uso do "else".
        break

print(f"O número de Windows foi {codigo_so.count(1)}.") #o .count() é uma função utilizada para contabilizar quantas vezes o elemento inserido dentro dos parenteses aparece na lista
print(f"O número de Linux foi {codigo_so.count(2)}.")
print(f"O número de Mac foi {codigo_so.count(3)}.")
print(f"O número de Outros foi {codigo_so.count(4)}.")
print(len(codigo_so)) #o len(nome_do_vetor) é um comando para ler o tamanho do vetor. em melhores palavras, a quantidade de informação adicionada dentro dele
