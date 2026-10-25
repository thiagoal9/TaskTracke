from datetime import datetime

tarefas = []

PRIORIDADES = {
    "alta": "Alta",
    "media": "Média",
    "média": "Média",
    "baixa": "Baixa",
}


def mostrar_menu():
    print("\n===== TASKTRACKER =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("0 - Sair")


def cadastrar_tarefa():
    print("\n--- Nova tarefa ---")

    titulo = input("Título: ").strip()
    if titulo == "":
        print("Erro: toda tarefa precisa ter um título.")
        return

    descricao = input("Descrição: ").strip()

    prioridade = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
    if prioridade not in PRIORIDADES:
        print("Erro: a prioridade deve ser Alta, Média ou Baixa.")
        return

    prazo = input("Data limite (DD/MM/AAAA, ou Enter para pular): ").strip()
    if prazo != "":
        try:
            datetime.strptime(prazo, "%d/%m/%Y")
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA.")
            return
    else:
        prazo = "Sem prazo"

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": PRIORIDADES[prioridade],
        "prazo": prazo,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' cadastrada com sucesso! (status: Pendente)")


def listar_tarefas():
    print("\n--- Tarefas cadastradas ---")
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada ainda.")
        return

    for t in tarefas:
        print(f"\n[{t['id']}] {t['titulo']}")
        print(f"    Descrição : {t['descricao'] or '-'}")
        print(f"    Prioridade: {t['prioridade']}")
        print(f"    Prazo     : {t['prazo']}")
        print(f"    Status    : {t['status']}")


def concluir_tarefa():
    if len(tarefas) == 0:
        print("Não há tarefas para concluir.")
        return

    listar_tarefas()
    escolha = input("\nDigite o número da tarefa que quer concluir: ").strip()

    if not escolha.isdigit():
        print("Erro: digite apenas o número da tarefa.")
        return

    numero = int(escolha)
    for t in tarefas:
        if t["id"] == numero:
            if t["status"] == "Concluída":
                print("Essa tarefa já está concluída.")
            else:
                t["status"] = "Concluída"
                print(f"Tarefa '{t['titulo']}' marcada como concluída!")
            return

    print("Erro: tarefa não encontrada.")


def main():
    while True:
        mostrar_menu()
        try:
            opcao = input("Escolha uma opção: ").strip()
        except EOFError:
            break

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "0":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
