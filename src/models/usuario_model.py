from sqlalchemy import Column, Integer, String
from passlib.hash import pbkdf2_sha256 as sha256
from connection import Base

class Usuario():
#construtor quando quero usar os atributos para novos valores
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

#get
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email


    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha    


    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)




    def gen_senha(self, senha):
        return sha256.hash(senha)
    
    def verificar_senha(self, senha):
        return sha256.verify(senha, self.senha)