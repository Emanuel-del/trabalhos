import sqlite3

DATABASE_NAME = 'agenda.db'

def connect_db():
    return sqlite3.connect(DATABASE_NAME)

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
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

def adicionar_contato(nome, telefone, email):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)',
            (nome, telefone, email)
        )
        conn.commit()
        print(f"\nContato '{nome}' adicionado com sucesso.")
    except sqlite3.IntegrityError:
        print(f"\nErro: Contato com o nome '{nome}' já existe.")
    finally:
        conn.close()

def listar_contatos():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, nome, telefone, email FROM contatos ORDER BY nome')
    
    contatos = cursor.fetchall()
    
    conn.close()
    
    print("\n--- AGENDA DE CONTATOS ---")
    
    if not contatos:
        print("Nenhum contato encontrado na agenda.")
        return

    print(f"{'ID':<4} | {'Nome':<25} | {'Telefone':<15} | {'E-mail':<30}")
    print("-" * 79)
    
    for contato in contatos:
        id_contato, nome, telefone, email = contato
        print(f"{id_contato:<4} | {nome:<25} | {telefone:<15} | {email:<30}")
    
    print("-" * 79)

def menu():
    while True:
        print("\n--- MENU DA AGENDA ---")
        print("1. Adicionar Novo Contato")
        print("2. Listar Todos os Contatos")
        print("3. Sair")
        
        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contato(nome, telefone, email)
        
        elif escolha == '2':
            listar_contatos()
            
        elif escolha == '3':
            print("Saindo da Agenda. Até logo!")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    setup_db()
    menu()