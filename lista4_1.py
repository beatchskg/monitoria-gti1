#Por conta da pandemia, o CEF (Curso Estudante Feliz) adotou o Google Classroom como ferramenta para auxiliar 
# o ensino remoto. Para acessá-lo, os estudantes precisam logar com e-mail institucional e senha. 
# A senha inicial, enviada pela Agenda Digital, é gerada automaticamente a partir da data de nascimento do aluno, 
# do seguinte modo:

#mm + ‘$’ + dd(invertido) + ‘#’ + dd + ‘!’ + mm(invertido) + ‘*’  + aaaa 

# Escreva um programa que leia o dia, mês e ano de nascimento de um estudante e informe a senha de acordo com a formatação acima

# Função que inverte uma string recebida como argumento

def invertido(data):
    return data[::-1]  # Retorna a string invertida, utilizando slicing [::-1]

# Função que gera uma senha baseada em informações da data de nascimento
def gerar_senha():
    # Lista para armazenar as partes da data (dia, mês e ano)
    datas = ['dia', 'mês', 'ano']
    # dia = 0, mes = 1, ano = 2
    # Exibe uma mensagem para o usuário inserir a data de nascimento
    print('\tData de Nascimento (dd/mm/aaaa)')
    
    # Loop para capturar o dia, mês e ano do usuário
    for i in range(len(datas)):
        # Solicita ao usuário que informe o dia, mês ou ano
        informacao = input(f'Informe o {datas[i]}: ')
        # Armazena o valor inserido na lista datas
        datas[i] = informacao
    
    # Retorna a senha formatada com as partes da data e algumas inversões
    # Formato da senha: {mês}${dia invertido}#{dia}!{mês invertido}*{ano}
    return f'{datas[1]}${invertido(datas[0])}#{datas[0]}!{invertido(datas[1])}*{datas[2]}'

# Chama a função gerar_senha para gerar a senha

#main
senha = gerar_senha()

# Exibe a senha gerada
print(F'Sua senha é: {senha}')
