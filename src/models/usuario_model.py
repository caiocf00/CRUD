from sqlalchemy import Column, Integer, String
from passlib.hash import pbkdf2_sha256 as sha256


class Usuario():
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)


    def gen_senha(self, senha):
        return sha256.hash(senha)
    
    def verificar_senha(self, senha):
        return sha256.verify(senha, self.senha)