alunos = []

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar():
    try:
        matricula = input("Digite a matrícula do aluno: ")
        # Verifica se matrícula já existe
        for aluno in alunos:
            if aluno['matricula'] == matricula:
                print("Matrícula já cadastrada!")
                return

        nome = input("Digite o nome do aluno: ")
        n1 = float(input("Digite a nota 1: "))
        n2 = float(input("Digite a nota 2: "))

        media = calcular_media(n1, n2)
        status = situacao(media)

        aluno = {
            "matricula": matricula,
            "nome": nome,
            "n1": n1,
            "n2": n2,
            "media": media,
            "situacao": status
        }

        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!\n")
    except ValueError:
        print("Erro: Digite valores válidos para as notas.")

def alterar():
    matricula = input("Digite a matrícula do aluno que deseja alterar: ")
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            try:
                print(f"Alterando dados do aluno {aluno['nome']}")
                aluno['nome'] = input("Novo nome: ")
                aluno['n1'] = float(input("Nova nota 1: "))
                aluno['n2'] = float(input("Nova nota 2: "))
                aluno['media'] = calcular_media(aluno['n1'], aluno['n2'])
                aluno['situacao'] = situacao(aluno['media'])
                print("Dados alterados com sucesso!\n")
            except ValueError:
                print("Erro: Digite valores válidos para as notas.")
            return
    print("Aluno não encontrado!\n")

def excluir():
    matricula = input("Digite a matrícula do aluno que deseja excluir: ")
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            alunos.remove(aluno)
            print("Aluno excluído com sucesso!\n")
            return
    print("Aluno não encontrado!\n")

def listar():
    if not alunos:
        print("Nenhum aluno cadastrado!\n")
    else:
        print("\nLista de Alunos:")
        print("-" * 60)
        for aluno in alunos:
            print(f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | "
                  f"Nota 1: {aluno['n1']} | Nota 2: {aluno['n2']} | "
                  f"Média: {aluno['media']:.2f} | Situação: {aluno['situacao']}")
        print("-" * 60 + "\n")


# ------------------- Programa Principal -------------------
while True:
    try:
        opcao = int(input(
            "Digite: 1 - Cadastrar, 2 - Alterar, 3 - Excluir, 4 - Listar, 5 - Sair do Sistema: "
        ))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            listar()
        elif opcao == 5:
            break
        else:
            print("Erro: Opção inválida.\n")
    except ValueError:
        print("Erro: Digite apenas números.\n")

print("Sistema finalizado com sucesso!!!!")