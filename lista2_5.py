numero = int(input("Digite um número inteiro:"))
inicio = int(input("Informe o inicio"))
fim = int(input("Informe o fim"))

 
for i in range(inicio, fim+1):
    print (f"{numero} x {i} = {numero*i}")
