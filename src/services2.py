import os
import json
from connection import get_connet
#login

def menu1():
    print('1 - fazer login')
    print('2 - Cadastrar ')



usuario = {}
def criar_conta():
    nome = input('Digite o nome do usuário: ').strip()
    email = input('Digite o seu email:').strip()
    senha= input('Digite sua senha:').strip()
    print(f"Conta criada com sucesso para {nome , email , senha}!")
    with open(fr"conta.json", "w", encoding='utf-8') as f:
        json.dump(nome, f,ensure_ascii=False, indent=4)


menu1()
criar_conta()




''''def menu():
    print("1. Criar conta")
    print("2. Exibir dados da conta")
    print("3. Depositar valor")
    print("4. Sacar valor")
    print("5. Encerrar conta")
    print("6. Sair do programa")
    escolha = input("Escolha uma opção (1-6): ")
    return escolha'''