#Faça um programa com duas funções. 
# A primeira função recebe o nome de um arquivo e escreve 
# o nome e sobrenome de 6 pessoas. 
# A segunda função lê o arquivo e permite alterar os nomes.

# Função para criar o arquivo e escrever nomes e sobrenomes

def criar_arquivo(nomedoarquivo):
    # Abre o arquivo no modo de escrita ('w'). Se o arquivo não existir, ele será criado.
    with open(nomedoarquivo, 'w') as file:
        # Executa um laço de 6 iterações (i de 0 a 5).
        for i in range(6):
            # Solicita ao usuário que insira o nome e sobrenome da pessoa.
            nome = input(f"Digite o nome e sobrenome da pessoa {i+1}: ")
            # Escreve o nome digitado no arquivo e adiciona uma nova linha.
            file.write(nome + '\n') # '\n' é um EOL (end of line)

# Função para editar o arquivo criado
def editar_arquivo(nomedoarquivo):
    # Abre o arquivo no modo de leitura ('r') para obter todas as linhas.
    with open(nomedoarquivo, 'r') as file:
        linhas = file.readlines()
    
    # Abre o mesmo arquivo no modo de escrita ('w') para salvar as possíveis modificações.
    with open(nomedoarquivo, 'w') as file:
        # Para cada linha no arquivo original.
        for linha in linhas:
            # Mostra a linha atual (nome) sem a quebra de linha.
            print(f"Nome atual: {linha.strip()}")
            # Pergunta ao usuário se deseja alterar o nome.
            resposta = input("Deseja alterar este nome? (Sim/Não): ")
            # Se a resposta for 'sim', solicita um novo nome e o escreve no arquivo.
            if resposta.lower() == 'sim':
                novo_nome = input("Digite o novo nome e sobrenome: ")
                file.write(novo_nome + '\n')
            # Caso contrário, mantém a linha original no arquivo.
            else:
                file.write(linha)

# Exemplo de uso
nome_arquivo = "nomes.txt"
criar_arquivo(nome_arquivo)  # Primeiro cria o arquivo
editar_arquivo(nome_arquivo)  # Depois edita conforme necessário
