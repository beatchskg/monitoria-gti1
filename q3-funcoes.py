def cms(metros):
    resultado = metros * 100
    print(f'O valor em centímetros é: {resultado}cm')

def kms(metros):
    resultado = metros/100
    print(f' O valor em quilômetros é: {resultado}km')

#main

distance = float(input('Informe o valor em metros.'))
converter = int(input('Informe para qual deseja converter (1- centímetros; 2- quilômetros)'))

if converter == 1:
    cms(distance)
if converter == 2:
    kms(distance)

