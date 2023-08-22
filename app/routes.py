from app import app, db, bcrypt
from flask import render_template, url_for, request, flash, session, redirect
from app.forms import Contato
from app.models import ContatoModel, CadastroModel
from app.forms import Cadastro
from flask_bcrypt import check_password_hash
import time


@app.route('/')
def index():
    return render_template('index.html',titulo = 'Pagina inicial')

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    dados_formulario = None
    formulario = Contato()
    print('Acessou a rota contatos')
    if formulario.validate_on_submit():
        flash('Seu formulario foi enviado com sucesso!')
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        mensagem = formulario.mensagem.data
        
        novo_contato = ContatoModel(nome=nome,email=email,telefone=telefone,mensagem=mensagem)
        db.session.add(novo_contato)
        db.session.commit()

    return render_template('contatos.html',titulo = 'Contatos', formulario = formulario,dados_formulario = dados_formulario)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html',titulo = 'Sobre')

@app.route('/linguagens')
def linguagens():
    return render_template('linguagens.html',titulo = 'Linguagens')

@app.route('/teste')
def teste():
    return render_template('teste.html')

@app.route('/cadastro', methods =['POST', 'GET'])
def cadastro():
    dados_formulario = None
    cadastro = Cadastro()
    print('Acessou a rota de cadastro!')
    if cadastro.validate_on_submit():
        flash('Seu cadastro foi realizado com sucesso!')
        nome = cadastro.nome.data
        email = cadastro.email.data
        senha = cadastro.senha.data
        hash_senha = bcrypt.generate_password_hash(senha).decode('utf_8')
        novo_cadastro = CadastroModel(nome=nome,email=email,senha=hash_senha)
        db.session.add(novo_cadastro)
        db.session.commit()
    return render_template('cadastro.html',titulo = 'Cadastro', cadastro=cadastro)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        senha = request.form.get('senha')

        usuario = CadastroModel.query.filter_by(email = email).first()
        if usuario and check_password_hash(usuario.senha, senha):
            session['email'] = usuario.email
            session['nome'] = usuario.nome
            time.sleep(2)
            return redirect(url_for('index'))
        else:
            flash('email ou senha invalido')


    return render_template('login.html',titulo = 'Login')
    
@app.route('/sair')
def sair():
    session.pop('email', None)
    session.pop('nome', None)
    return redirect(url_for('login'))

@app.route('/editar', methods=['POST','GET'])
def editar():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    usuario = CadastroModel.query.filter_by(email = session['email']).first()
    if request.method =='POST':
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')
        senha = request.form.get('senha')
        usuario.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        db.session.commit()
        session['email'] = usuario.email
        session['nome'] = usuario.nome
        session['senha'] = usuario.senha
        flash('Seus dados foram atualizados com sucesso!')
    return render_template('editar.html',titulo = 'Editar')

@app.route('/excluir-conta')
def excluir():
    return render_template('excluir-conta.html',titulo = 'Excluir conta')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html',titulo = 'Usuario')
