# Desenvolva um programa que possua um vetor de 10 números inteiros. 
# Após o usuário inserir os valores, mostre quantos desses números 
# são maiores, menores e iguais ao primeiro elemento do vetor.

# Inicializa um vetor (lista) para armazenar 10 números inteiros
numeros = []

# Recebe 10 números inteiros do usuário e armazena no vetor
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# O primeiro elemento do vetor será comparado com os outros
primeiro_elemento = numeros[0]

# Inicializa contadores para os números maiores, menores e iguais ao primeiro elemento
maiores = 0
menores = 0
iguais = 0

# Percorre o vetor e compara cada número com o primeiro elemento
for numero in numeros:
    if numero > primeiro_elemento:
        maiores += 1
    elif numero < primeiro_elemento:
        menores += 1
    else:
        iguais += 1

# Exibe os resultados
print(f"\nQuantidade de números maiores que o primeiro elemento ({primeiro_elemento}): {maiores}")
print(f"Quantidade de números menores que o primeiro elemento ({primeiro_elemento}): {menores}")
print(f"Quantidade de números iguais ao primeiro elemento ({primeiro_elemento}): {iguais}")

