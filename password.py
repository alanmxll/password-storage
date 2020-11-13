import sqlite3

MASTER_PASSWORD = "123456"

password = input("Insira sua senha master: ")
if password != MASTER_PASSWORD:
    print("Senha inválida! Encerrando...")
    exit()

conn = sqlite3.connect("passwords.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")


def menu():
    print("****************************************")
    print("*        i : Inserir nova senha        *")
    print("*      l : Listas serviços salvos      *")
    print("*       r : Recuperar uma senha        *")
    print("*              s : Sair                *")
    print("****************************************")


def get_password(service):
    cursor.execute(f"""
        SELECT username, password FROM users
        WHERE service = '{service}';
    """)
    if cursor.rowcount == 0:
        print("Serviço não cadastrado (use 'l' para verificar os serviços.)")
    else:
        for user in cursor.fetchall():
            print(user)


def insert_password(service, username, password):
    cursor.execute(f"""
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}');
    """)
    conn.commit()


def show_services():
    cursor.execute("""
        SELECT * FROM users;
    """)
    for service in cursor.fetchall():
        print(service)


while True:
    menu()
    op = input("Escolha uma opção: ")
    if op not in ["i", "l", "r", "s"]:
        print("Opção inválida.")
        continue

    if op == "s":
        break

    if op == "i":
        service = input("Qual o nome do serviço? ")
        username = input("Qual o nome do usuário? ")
        password = input("Qual a senha? ")
        insert_password(service, username, password)

    if op == "l":
        show_services()

    if op == "r":
        service = input("Qual o serviço para o qual quer a senha? ")
        get_password(service)


conn.close()
