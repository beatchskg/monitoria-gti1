import os
os.system('cls')

#Faça um programa que receba um valor em horas e dê duas opções ao
#usuário, converter em minutos ou em segundos. A partir da escolha do
#usuário, o programa deverá chamar a função específica de conversão. A
#função para converter horas em minutos deverá receber como parâmetro a
#hora e retornar o valor em minutos. A função para converter horas em
#segundos deverá receber como parâmetro a hora e retornar o valor em
#segundos. No programa principal (MAIN) imprima o valor retornado pela função.

#converter hora em minuto
#converter hora em segundos
#escolher a conversão

def minutos(x):
    return x*60
def segundos(x):
    return x*360
def converter(opcao, x):
    if opcao not in (1,2):
        print('Opção inválida! Escolha entre 1 ou 2.')
        return
    elif opcao == 1:
        novo_valor = minutos(horas) # horas*60
    else:
        novo_valor = segundos(horas) #horas*360
    return novo_valor

#main
horas = float(input('Informe o valor em horas.'))

print('\tMENU')
option = int(input('Você deseja converter para:\n1 - MINUTOS\n2 - SEGUNDOS'))

print(converter(option, horas))

