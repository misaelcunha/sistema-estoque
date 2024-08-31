from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, validators, PasswordField, FileField

class FormularioMaterial(FlaskForm):
    unidade = StringField('Unidade', [validators.DataRequired(), validators.Length(min=1, max=10)])
    quantidade = IntegerField('Quantidade', [validators.DataRequired()])
    descricao = StringField('Descrição', [validators.DataRequired(), validators.Length(min=1, max=255)])
    modelo = StringField('Modelo', [validators.DataRequired(), validators.Length(min=1, max=255)])
    fabricante = StringField('Fabricante', [validators.DataRequired(), validators.Length(min=1, max=255)])
    foto = FileField('Foto')
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=1, max=255)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')