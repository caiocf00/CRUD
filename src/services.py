from connection import get_connet
from passlib.hash import pbkdf2_sha256 as sha256

def criar_usuario(nome, email, senha):
    try:
        conn = get_connet()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO TB_USUARIO (NOME, EMAIL, SENHA) VALUES (?, ?, ?)',
                       (nome, email, senha)
    )
        conn.commit()
        print("Usuário criado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao criar usuario: {e}")


def listar_usuario():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT NOME, EMAIL, SENHA FROM TB_USUARIO')
        usuarios = cursor.fetchall()

        if usuarios:
            print(f"{'='*30} Usuários {'='*30}")
            for u in usuarios:
                print(f'| {u}')
        
        else:
            print("Nenhum usuário encontrado.")


    except Exception as e:
        print(f"Erro ao criar usuario: {e}")


def excluir_usuario(id):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM TB_USUARIO WHERE ID = ?""", (id,))
        
        conn.commit()
    
    except Exception as e:
        print(f"Erro ao criar usuario: {e}")

    

def editar_usuario(id):
    ... 

def listar_usuario_email(email):
    ...

def listar_usuario_id(id):
    ...

def criar_tabela():
    try:
        conn = get_connet()
        cursor = conn.cursor()

        cursor.execute('''
    create table tb_usuario(
	ID INTEGER PRIMARY KEY ,
    NOME VARCHAR(120) NOT NULL,
    EMAIL VARCHAR(120) UNIQUE,
    SENHA VARCHAR(255) 
);
''')

    except Exception as e:
        print("Erro ao criar tabela.", e)

if __name__ == "__main__":
    criar_tabela()
    nome = input ('Digite o nome: ').strip().title()
    email = input ('Digite o email: ').strip()
    senha = input ('Digite a senha: ').strip()
    senha = sha256.hash(senha)
 
criar_usuario(nome, email, senha)
listar_usuario()