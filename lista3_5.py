# Faça um programa para cadastro de animais silvestres. Serão 10 animais cadastrados. O programa deve receber o nome do animal e perguntar em qual 
# categoria o usuário deseja cadastrá-lo (use listas, uma para cada categoria):
#1 - Réptil
#2 - Mamífero
#3 - Ave
#4 – Outro
#Por fim, o programa deve exibir as quatro listas e informar a quantidade de animais de cada categoria. Segue um exemplo abaixo:

#abrindo as listas para cada categoria de animal, conforme determinado pelo enunciado
repteis = [] 
mamiferos = []
aves = []
outros = []

for i in range(10): #o enunciado determina que serão 10 animais cadastrados, por esse motivo, utilizamos o "for"
    animal = input("Digite o nome do seu animal.") #coletando o nome do animal
    categoria = int(input("Digite a categoria do seu animal.")) # coletando categoria do animal
#as condicionais elaboradas vão envolver as duas informações obtidas (nome e categoria). a adição do nome do animal aos vetores criados, dependerá da categoria do animal.
    if categoria == 1: #nesse caso, se a categoria inserida for "1"
        repteis.append(animal) #eu posso seguir à adição do animal informado ao vetor de répteis
    elif categoria == 2: #se a categoria for 2
        mamiferos.append(animal) #posso seguir à adição do animal informado ao vetor dos mamíferos
    #o mesmo se aplica aos demais
    elif categoria == 3:
        aves.append(animal)
    else:
        outros.append(animal)
#a formatação do print dessa maneira é importante porque na questão a professor demonstra a forma que quer a saída dos dados

print(f"Repteis: {repteis}, Quantidade: {len(repteis)}") # utilizamos o len(nome_do_vetor) para contabilizar a quantidade de elementos que constam nesse vetor
print(f"Mamiferos: {mamiferos}, Quantidade: {len(mamiferos)}")
print(f"Aves: {aves}, Quantidade: {len(aves)}")
print(f"Outros: {outros}, Quantidade: {len(outros)}")
