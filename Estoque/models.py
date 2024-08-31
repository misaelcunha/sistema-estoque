from sistema import db

#Definição da tabela 'materiais' no banco de dados
class Materiais(db.Model):
    """
       Modelo para a tabela de materiais no banco de dados.
    """
    __tablename__ = 'materiais'
    codigo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unidade = db.Column(db.String(10), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    modelo = db.Column(db.String(255), nullable=False)
    fabricante = db.Column(db.String(255), nullable=False)
    data_hora = db.Column(db.String(255), nullable=False)
    foto = db.Column(db.String(255), nullable=True)

#Definição da tabela 'movimentações' no banco de dados
class Movimentacoes(db.Model):
    """
       Modelo para a tabela de movimentações no banco de dados.
    """
    __tablename__ = 'movimentacoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    material_codigo = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    data_hora = db.Column(db.String(255), nullable=False)
    feito_por = db.Column(db.String(255), nullable=False)

class Usuarios(db.Model):
    """
       Modelo para a tabela de usuários no banco de dados.
    """
    __tablename__ = 'usuarios'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.nome