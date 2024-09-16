
choice1 = int(input('Escolha o primeiro numero (entre 0 e 5).'))
choice2 = int(input('Escolha o segundo numero (entre 0 e 5)'))

if 0 < choice1 > 5:
    print(f"Opção 1 inválida! Escolher novamente.")
if 0 < choice2 > 5:
    print(f'Opção 2 inválida! Escolher novamente.')

if choice1+choice2 <= 6:
    if choice1+choice2 == 0:
        print(f'Now playing: Cheia de Manias (Raça Negra).')
    elif choice1+choice2 == 1:
        print(f"Now playing: Me leva junto com você (Raça Negra).")
    elif choice1+choice2 == 2:
        print(f'Now playing: É tarde demais (Raça Negra).')
    elif choice1+choice2 == 3:
        print(f'Now playing: Quando te encontrei (Raça Negra)')
    elif choice1+choice2 == 4:
        print(f'Now playing: Deus me livre (Raça Negra).')
    elif choice1+choice2 == 5:
        print(f'Now playing: Ciúme de você (Raça Negra)')
    else:
        print(f'Now playing: Cigana (Raça Negra).')
else:
    print('Escolha fora do alcance. Tente novamente!')


