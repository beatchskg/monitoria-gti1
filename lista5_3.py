#Um corretor quer analisar como foi sua venda no dia. 
# Desenvolva um programa que receba a quantidade de apartamentos 
# vendidos e:

    #a) Implemente um vetor de números reais chamado areas, correspondente à área de cada apartamento vendido.
    #b) Calcule e mostre a soma das áreas.
    #c) Mostre o maior e o menor apartamento vendido.

# Solicita ao usuário a quantidade de apartamentos vendidos
quantidade = int(input("Digite a quantidade de apartamentos vendidos: "))

# Inicializa uma lista (vetor) chamada areas
areas = []

# Recebe a área de cada apartamento e armazena na lista
for i in range(quantidade):
    area = float(input(f"Digite a área do apartamento {i+1} em metros quadrados: "))
    areas.append(area)

# Calcula a soma das áreas dos apartamentos vendidos
soma_areas = sum(areas)

# Encontra o maior e o menor apartamento vendido
maior_apartamento = max(areas)
menor_apartamento = min(areas)

# Exibe os resultados
print(f"\nA soma total das áreas dos apartamentos vendidos é: {soma_areas:.2f} m²")
print(f"O maior apartamento vendido tem: {maior_apartamento:.2f} m²")
print(f"O menor apartamento vendido tem: {menor_apartamento:.2f} m²")
