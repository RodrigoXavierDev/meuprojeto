from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TelField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    telefone = TelField('telefone', validators=[DataRequired()])
    mensagem = TextAreaField('mensagem')
    enviar = SubmitField('enviar')

class Cadastro(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    sobrenome = StringField('sobrenome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    cpf = StringField('cpf', validators=[DataRequired()])
    telefone = StringField('telefone', validators=[DataRequired()])
    endereco = StringField('endereco', validators=[DataRequired()])
    bairro = StringField('bairro', validators=[DataRequired()])
    cidade = StringField('cidade', validators=[DataRequired()])
    uf = StringField('uf', validators=[DataRequired()])
    enviar = SubmitField('Enviar')