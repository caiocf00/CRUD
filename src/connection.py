from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


SQLALCHEMY_DATABASE_URI = "sqlite:///controle_usuario.db"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    conntion = engine.connect()
    print("Conexão com o banco de dados realizada com sucesso!")
except Exception as e:
    print("Erro ao conectar ao banco de dados:")
Base = declarative_base()

Base.metadata.create_all(engine)
