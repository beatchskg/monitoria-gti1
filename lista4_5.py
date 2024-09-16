#Faça uma função que retorne o reverso de um número inteiro informado pelo usuário.
#Por exemplo: 127 -> 721


def reverter_numero(numero):
    # Converte o número para string
    numero_str = str(numero) 
    
    # Invertemos a string
    numero_revertido_str = numero_str[::-1]
    
    # Convertemos a string revertida de volta para inteiro
    numero_revertido = int(numero_revertido_str)
    
    return numero_revertido

#MAIN
# Solicita o número do usuário
numero_usuario = int(input("Digite um número inteiro: "))

# Exibe o número revertido
print("Número revertido:", reverter_numero(numero_usuario))
