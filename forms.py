# Allow the access to a form
from flask_wtf import FlaskForm
# Associated with fields
from wtforms import StringField, PasswordField, SubmitField, BooleanField
# Restriction of same fields to users
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCreateAccount(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    complete_name = StringField('Nome completo:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    confirmation_password = PasswordField('Confirmar senha:', validators=[DataRequired(),
                                                                          EqualTo('password')])
    button_submit_create_account = SubmitField('Criar uma conta')


class FormLogin(FlaskForm):
    username = StringField('Usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    remember_password = BooleanField('Aceita relembrar os dados de acesso')
    button_submit_login = SubmitField('Entrar')
