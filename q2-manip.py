guests = []
duplicated = []

while True:
    novo_convidado = input("Digite o nome do convidado:").upper()
    if novo_convidado == "SAIR":
        break
    else:
        guests.append(novo_convidado)

nomes_file = open('RSVP.txt', 'a+')
nomes_file.writelines("\n".join(guests))
nomes_file.close()

for convidado in guests:
    if guests.count(convidado) > 1:
        if convidado not in duplicated:
            duplicated.append(convidado)

print(f'As pessoas com nome repetido são: {duplicated}')