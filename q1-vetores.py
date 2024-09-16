tamanhos = []

quantidade_tv = int(input('Informe a quantidade de TVs vendidas hoje.'))

for i in range(quantidade_tv):
    tamanhos.append(float(input('Informe os tamanhos das TVs vendidas.')))

media = sum(tamanhos)/quantidade_tv

print(f'A média de tamanho das TVs vendidas foi: {media}')
print(f'A menor TV vendida foi {min(tamanhos)} e a maior TV vendida foi {max(tamanhos)}')

