while True:
    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

    continuar = input("\nDeseja cadastrar outro aluno? (s/n): ")

    if continuar.lower() != 's':
        print("Encerrando o programa...")
        break
