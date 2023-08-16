from app import app, db
from flask import render_template, url_for, request, flash
from app.forms import Contato
from app.models import ContatoModel
from app.forms import Cadastro
from app.models import CadastroModel


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
    if cadastro.validate_on_submite():
        flash('Seu cadastro foi realizado com sucesso!')
        nome = cadastro.nome.data
        email = cadastro.email.data
        senha = cadastro.senha.data

        novo_cadastro = CadastroModel(nome=nome,email=email,senha=senha)
        db.session.add(novo_cadastro)
        db.session.comnit()
    return render_template('cadastro.html',titulo = 'Cadastro')

@app.route('/login')
def login():
    return render_template('login.html',titulo = 'Login')
