cont = 0

while True:
    codigo = int(input("Digite o código de cadastro do caixão desejado."))
    if codigo == -1:
        print(f"Programa encerrado.")
        break
    cont += 1
print (f"A quantidade de caixões cadastrados foi {cont}.")
