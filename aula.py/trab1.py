tarefas = []

def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Remover tarefa")
    print("5. Organizar tarefas (ordem alfabética)")
    print("6. Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção (1-6): ")

    if escolha == "1":
        descricao = input("Digite a descrição da nova tarefa: ")
        tarefas.append(descricao)
        print("Tarefa adicionada!")

    elif escolha == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- Tarefas ---")
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")

    elif escolha == "3":
        if not tarefas:
            print("Nenhuma tarefa para atualizar.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")
            indice = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
            if 0 <= indice < len(tarefas):
                nova_desc = input("Digite a nova descrição da tarefa: ")
                tarefas[indice] = nova_desc
                print("Tarefa atualizada!")
            else:
                print("Número inválido.")

    elif escolha == "4":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")
            indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas.pop(indice)
                print("Tarefa removida!")
            else:
                print("Número inválido.")

    elif escolha == "5":
        tarefas.sort()
        print("Tarefas organizadas em ordem alfabética!")

    elif escolha == "6":
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")