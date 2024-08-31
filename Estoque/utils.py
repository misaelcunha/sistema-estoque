import datetime

from functools import wraps

from models import Materiais, Movimentacoes
from flask import session, url_for, redirect, request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #Verifica se o usuário está logado
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            return redirect(url_for('login', proxima=request.url))
        return f(*args, **kwargs)
    return decorated_function

def get_materiais(offset=0, per_page=20):
    """
       Retorna uma lista paginada de materiais, ordenada pelo código do material.
    """
    return Materiais.query.order_by(Materiais.codigo).offset(offset).limit(per_page).all()

def get_historico(offset=0, per_page=20):
    """
       Retorna uma lista paginada de movimentações, ordenada pela data/hora em ordem decrescente.
    """
    return Movimentacoes.query.order_by(Movimentacoes.data_hora.desc()).offset(offset).limit(per_page).all()

def get_hora():
    """
      Retorna a data e hora atual no formato DD/MM/AAAA HH:MM.
    """
    data = datetime.datetime.now()
    return datetime.datetime.strftime(data, "%d/%m/%Y %H:%M")