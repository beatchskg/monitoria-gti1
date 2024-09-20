frequencia = int(input("Digite a frequência do aluno."))
nota1 = float(input("Digite a primeira nota do aluno."))
nota2 = float(input("Digite a segunda nota do aluno."))

media = (nota1 + nota2)/ 2

if frequencia >= 75:
    if media >= 7:
        print ("Aprovado por média.")
    else:
        print ("Reprovado por média.")
else:
    print ("Reprovado por falta.")
