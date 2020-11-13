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
    pass


def insert_password(cursor, service, username, password):
    cursor.execute(f"""
        INSERT INTO users (service, username, password)
        VALUES ({service}, {username}, {password});
    """)
    conn.commit()


def show_services(cursor):
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


conn.close()
