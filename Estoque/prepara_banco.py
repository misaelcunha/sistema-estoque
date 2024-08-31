import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash
from config import senha_padrao_usuario

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='246810'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `estoque`;")

cursor.execute("CREATE DATABASE `estoque`;")

cursor.execute("USE `estoque`;")

# criando tabelas
TABLES = {}
TABLES['Materiais'] = ('''
      CREATE TABLE `materiais` (
      `codigo` int(11) NOT NULL AUTO_INCREMENT,
      `unidade` varchar(10) NOT NULL,
      `quantidade` int(255) NOT NULL,
      `descricao` varchar(255) NOT NULL,
      `modelo` varchar(255) NOT NULL,
      `fabricante` varchar(255) NOT NULL,
      `data_hora` varchar(255) NOT NULL,
      `foto` varchar(255),
      PRIMARY KEY (`codigo`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Movimentacoes'] = ('''
      CREATE TABLE `movimentacoes` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `material_codigo` int(11) NOT NULL,
      `tipo` varchar(10) NOT NULL,
      `quantidade` int(255) NOT NULL,
      `descricao` varchar(255),
      `data_hora` varchar(255) NOT NULL,
      `feito_por` varchar(255),
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `user_id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `email` varchar(255) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`user_id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Misael Augusto", "misael@esa-eng.com.br", generate_password_hash(senha_padrao_usuario).decode('utf-8')),
      ("Leandro Batista", "leandro@esa-eng.com.br", generate_password_hash(senha_padrao_usuario).decode('utf-8')),
      ("Osmar Vasques", "osmar@esa-eng.com.br", generate_password_hash(senha_padrao_usuario).decode('utf-8')),
      ("Estagiário", "estagio@esa-eng.com.br", generate_password_hash(senha_padrao_usuario).decode('utf-8')),
      ("Caique Henrique", "caique@esa-eng.com.br", generate_password_hash(senha_padrao_usuario).decode('utf-8')),
      ("Maximiliam Claudio", "maximiliam@esa-eng.com.br", generate_password_hash(senha_padrao_usuario).decode('utf-8')),
      ("Guilherme Batista", "guilherme@esa-eng.com.br", generate_password_hash(senha_padrao_usuario).decode('utf-8')),
]
cursor.executemany(usuario_sql, usuarios)

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()