#Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos números deste vetor, armazenando o resultado em outro vetor. 
#Os conjuntos têm 10 elementos cada. Imprimir todos os vetores.

original = [] #abrindo vetor dos números "originais" a serem coletados
quadrado = [] #abrindo vetor dos números quadrados, a serem obtidos a partir dos coletados

for i in range(10): #utilizamos o for pois há uma delimitação da quantidade de vezes que o loop irá rodar
    numero = (float(input("Digite um numero:"))) #coletando a informação do número do usuário
    original.append(numero) #adicionando o número à lista utilizando o comando nome_do_vetor.append(), como visto nos exercícios anteriores
    #lembrete: poderíamos fazer diretamente desse jeito: original.append(float(input("Digite um numero:")))

for num in original: #rodaremos um for, onde "num" é cada elemento constante no vetor "original", para aplicar a regra abaixo:
    elevadoadois = num**2 #declarei uma variável que irá elevar ao quadrado cada novo "num" do vetor original
    quadrado.append(elevadoadois) #adicionando o número elevado ao a dois ao vetor que criamos no começo, chamado "quadrado"
    #lembrete: poderíamos fazer diretamente desse jeito: quadrado.append(num**2)

print(original)
print(quadrado)
