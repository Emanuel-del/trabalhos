
def menu():
    print("\n===== AGENDA DE CONTATOS =====")
    print("1. Cadastrar contato")
    print("2. Listar contatos")
    print("3. Pesquisar contato")
    print("4. Atualizar contato")
    print("5. Excluir contato")
    print("6. Sair")

def cadastrar_contato(agenda):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    agenda.append({
        "nome": nome,
        "telefone": telefone,
        "email": email
    })
    print(f" Contato '{nome}' cadastrado com sucesso!")

def listar_contatos(agenda):
    if not agenda:
        print("📭 Nenhum contato cadastrado.")
        return
    print("\n--- Lista de Contatos ---")
    for i, contato in enumerate(agenda, 1):
        print(f"{i}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

def pesquisar_contato(agenda):
    nome = input("Digite o nome para pesquisar: ").strip().lower()
    resultados = [c for c in agenda if nome in c['nome'].lower()]

    if resultados:
        print("\n--- Resultados da Pesquisa ---")
        for c in resultados:
            print(f"{c['nome']} - {c['telefone']} - {c['email']}")
    else:
        print(" Nenhum contato encontrado com esse nome.")

def atualizar_contato(agenda):
    nome = input("Nome do contato para atualizar: ").strip().lower()
    for c in agenda:
        if c['nome'].lower() == nome:
            print(f"Contato encontrado: {c['nome']} - {c['telefone']} - {c['email']}")
            novo_nome = input("Novo nome (ou Enter para manter): ").strip()
            novo_tel = input("Novo telefone (ou Enter para manter): ").strip()
            novo_email = input("Novo e-mail (ou Enter para manter): ").strip()

            if novo_nome:
                c['nome'] = novo_nome
            if novo_tel:
                c['telefone'] = novo_tel
            if novo_email:
                c['email'] = novo_email

            print(" Contato atualizado com sucesso!")
            return
    print(" Contato não encontrado.")

def excluir_contato(agenda):
    nome = input("Nome do contato para excluir: ").strip().lower()
    for c in agenda:
        if c['nome'].lower() == nome:
            agenda.remove(c)
            print(f" Contato '{c['nome']}' removido com sucesso!")
            return
    print(" Contato não encontrado.")

# Programa Principal
def main():
    agenda = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_contato(agenda)
        elif opcao == "2":
            listar_contatos(agenda)
        elif opcao == "3":
            pesquisar_contato(agenda)
        elif opcao == "4":
            atualizar_contato(agenda)
        elif opcao == "5":
            excluir_contato(agenda)
        elif opcao == "6":
            print(" Saindo da agenda. Até logo!")
            break
        else:
            print(" Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
