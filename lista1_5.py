time1 = input("Digite o nome do seu time.")
time2 = input("Digite o nome do seu time.")
gols1 = input(f"Digite a quantidade de gols do {time1}.")
gols2 = input(f"Digite a quantidade de gols do {time2}.")

if gols1 > gols2:
    print (f"O {time1} é campeão!")
elif gols2 > gols1:
    print (f"O {time2} é campeão!")
else:
    print (f"Os times {time1} e {time2} empataram.")
