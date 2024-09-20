#Escreva um programa que lê um arquivo .txt contendo endereços IPs 
# e mostra os IPs válidos e inválidos 
# (um IP válido não pode ter uma de suas partes maior que 255).


# Função para verificar se um IP é válido
def ip_valido(ip):
    # Divide o IP em partes, separando pelos pontos
    partes = ip.split(".")
    
    # Verifica se o IP tem exatamente 4 partes
    if len(partes) != 4:
        return False  # Se não tiver 4 partes, o IP é inválido
    
    # Itera sobre cada parte do IP
    for parte in partes:
        # Verifica se cada parte é numérica e se está entre 0 e 255
        if not parte.isdigit() or int(parte) > 255 or int(parte) < 0: 
            # .isdigit() utilizado para verificar se todos os caracteres de uma string são dígitos numéricos
            return False  # Se não for um número ou estiver fora do intervalo, o IP é inválido
    # Se todas as condições forem atendidas, o IP é válido
    return True

# Função principal que lê um arquivo e valida os IPs contidos nele
def verifica_ips(arquivo):
    # Abre o arquivo no modo de leitura
    with open(arquivo, 'r') as file:
        # Lê todas as linhas do arquivo
        linhas = file.readlines()
    
    # Itera sobre cada linha (IP) no arquivo
    for ip in linhas:
        # Remove espaços em branco no início e no fim da string
        ip = ip.strip()
        
        # Chama a função ip_valido para verificar se o IP é válido
        if ip_valido(ip):
            # Se for válido, imprime uma mensagem indicando que o IP é válido
            print(f"{ip} é válido.")
        else:
            # Se for inválido, imprime uma mensagem indicando que o IP é inválido
            print(f"{ip} é inválido.")

# Chama a função verifica_ips passando o nome do arquivo contendo os IPs
verifica_ips("ips.txt")
