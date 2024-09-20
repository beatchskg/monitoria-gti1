horas = int(input("Digite quantas horas você treina por mês."))

if horas <= 10:
    pontos = horas * 2
elif 11 >= horas <= 20:
    pontos = horas * 5
else:
    pontos = horas * 10

print (f"Você acumulou {pontos} pontos esse mês!")
