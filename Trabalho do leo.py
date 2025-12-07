import sqlite3
import os

DATABASE_NAME = 'agenda_contatos.db'

def connect_db():
    """Conecta ou cria o arquivo do banco de dados SQLite."""
    return sqlite3.connect(DATABASE_NAME)

def setup_db():
    """Inicializa o banco de dados e cria a tabela 'contatos' se ela não existir."""
    conn = connect_db()
    cursor = conn.cursor()
    # Garante que o nome seja único para evitar duplicidade
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            telefone TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

# --- Funções de Interface (Menu) ---

def menu():
    print("\n===== AGENDA DE CONTATOS (SQLite) =====")
    print("1. Cadastrar contato")
    print("2. Listar contatos")
    print("3. Pesquisar contato")
    print("4. Atualizar contato")
    print("5. Excluir contato")
    print("6. Sair")

# --- Funções CRUD Integradas ao SQLite ---

def cadastrar_contato():
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Insere o novo registro no banco de dados
        cursor.execute(
            'INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)',
            (nome, telefone, email)
        )
        conn.commit()
        print(f"\n[SUCESSO] Contato '{nome}' cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        # Tratamento para nome duplicado
        print(f"\n[ERRO] Um contato com o nome '{nome}' já está cadastrado.")
    except Exception as e:
        print(f"\n[ERRO] Ao cadastrar contato: {e}")
    finally:
        conn.close()

def listar_contatos():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Recupera todos os contatos ordenados por nome
    cursor.execute('SELECT id, nome, telefone, email FROM contatos ORDER BY nome')
    contatos = cursor.fetchall()
    
    conn.close()
    
    if not contatos:
        print("\nNenhum contato cadastrado.")
        return
        
    print("\n--- Lista de Contatos ---")
    print(f"{'ID':<4} | {'Nome':<25} | {'Telefone':<15} | {'E-mail':<30}")
    print("-" * 79)
    
    for id_contato, nome, telefone, email in contatos:
        print(f"{id_contato:<4} | {nome:<25} | {telefone:<15} | {email:<30}")
    print("-" * 79)

def pesquisar_contato():
    termo = input("Digite o nome ou parte do nome para pesquisar: ").strip()
    
    conn = connect_db()
    cursor = conn.cursor()
    
    # Usa LIKE para busca parcial (ex: %termo%)
    cursor.execute(
        "SELECT nome, telefone, email FROM contatos WHERE nome LIKE ?",
        (f'%{termo}%',)
    )
    resultados = cursor.fetchall()
    
    conn.close()

    if resultados:
        print("\n--- Resultados da Pesquisa ---")
        for nome, telefone, email in resultados:
            print(f"{nome} - {telefone} - {email}")
    else:
        print(f"\n[INFO] Nenhum contato encontrado contendo '{termo}'.")

def atualizar_contato():
    nome_antigo = input("Nome do contato para atualizar: ").strip()
    
    conn = connect_db()
    cursor = conn.cursor()
    
    # 1. Busca o contato pelo nome
    cursor.execute("SELECT id, nome, telefone, email FROM contatos WHERE nome = ?", (nome_antigo,))
    contato = cursor.fetchone()

    if not contato:
        print(f"\n[ERRO] Contato '{nome_antigo}' não encontrado.")
        conn.close()
        return

    id_contato, nome_atual, tel_atual, email_atual = contato
    
    print(f"\nContato encontrado (ID: {id_contato}): {nome_atual} - {tel_atual} - {email_atual}")
    
    # 2. Coletar novos dados (mantendo os antigos se o input for vazio)
    novo_nome = input(f"Novo nome (Atual: {nome_atual}) - [Enter para manter]: ").strip()
    novo_tel = input(f"Novo telefone (Atual: {tel_atual}) - [Enter para manter]: ").strip()
    novo_email = input(f"Novo e-mail (Atual: {email_atual}) - [Enter para manter]: ").strip()

    # Define os valores finais (preserva o antigo se o novo estiver vazio)
    final_nome = novo_nome if novo_nome else nome_atual
    final_tel = novo_tel if novo_tel else tel_atual
    final_email = novo_email if novo_email else email_atual

    # 3. Executar o UPDATE
    try:
        cursor.execute(
            'UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?',
            (final_nome, final_tel, final_email, id_contato)
        )
        conn.commit()
        print("\n[SUCESSO] Contato atualizado com sucesso!")
    except sqlite3.IntegrityError:
        print(f"\n[ERRO] O nome '{final_nome}' já está em uso por outro contato.")
    except Exception as e:
        print(f"\n[ERRO] Ao atualizar contato: {e}")
    finally:
        conn.close()

def excluir_contato():
    nome_excluir = input("Nome do contato para excluir: ").strip()
    
    conn = connect_db()
    cursor = conn.cursor()
    
    # Executa o DELETE e verifica a contagem de linhas afetadas
    cursor.execute('DELETE FROM contatos WHERE nome = ?', (nome_excluir,))
    rows_deleted = cursor.rowcount
    
    conn.commit()
    conn.close()

    if rows_deleted > 0:
        print(f"\n[SUCESSO] Contato '{nome_excluir}' removido com sucesso!")
    else:
        print(f"\n[INFO] Contato '{nome_excluir}' não encontrado.")


# Programa Principal
def main():
    # Inicializa o banco de dados
    setup_db() 
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            pesquisar_contato()
        elif opcao == "4":
            atualizar_contato()
        elif opcao == "5":
            excluir_contato()
        elif opcao == "6":
            print("\nSaindo da agenda. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
