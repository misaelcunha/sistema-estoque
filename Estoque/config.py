import os

#Configuração do banco de dados

SECRET_KEY = 'estoque'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '246810',
    servidor = 'localhost',
    database = 'estoque'
    )

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    USER_PASSWORD = os.getenv('USER_PASSWORD', 'default_user_password')

senha_padrao_usuario = '2206'