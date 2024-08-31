from flask import render_template, request, redirect, session, flash, url_for
from flask_bcrypt import check_password_hash

from sistema import app
from models import Usuarios
from helpers import FormularioUsuario

@app.route('/login')
def login():
    """
    Rota para a página de login.
    """
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    """
    Rota para autenticar o usuário.
    """
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(email=form.email.data).first()

    if usuario is not None:
        senha = check_password_hash(usuario.senha, form.senha.data)
    else:
        flash('Usuário não cadastrado!')
        return redirect(url_for('login'))

    if usuario and senha:
        session['usuario_logado'] = usuario.nome
        flash(usuario.nome + ' logado com sucesso')
        return redirect(url_for('mostra_estoque'))
    else:
        flash('Email ou senha incorretos!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    """
    Rota para logout do usuário.
    """
    flash('Logout realizado com sucesso!')
    session['usuario_logado'] = None
    return redirect(url_for('login'))