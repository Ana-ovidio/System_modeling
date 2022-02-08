# Allow the access to a form
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
# Associated with fields
from wtforms import StringField, PasswordField, SubmitField, BooleanField
# Restriction of same fields to users
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from general_system.models import Usuario
from flask_login import current_user


class FormCreateAccount(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    confirmation_password = PasswordField('Confirmar senha:', validators=[DataRequired(), EqualTo('password')])
    button_submit_account = SubmitField('Criar uma conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    password = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    remember_password = BooleanField('Aceita relembrar os dados de acesso')
    button_submit_login = SubmitField('Entrar')


class FormEditProfile(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    error_message = 'Extensão inválida, insira com jpeg, jpg ou png.'
    photo_profile = FileField('Atualizar foto de perfil: ', validators=[FileAllowed(['jpg', 'png', 'jpeg'],
                                                                                    message= error_message)])
    course_algorithms = BooleanField('Disciplina de Algoritimos')
    course_data_struct = BooleanField('Disciplina de Estrutura de dados')
    course_resistance_materials = BooleanField('Disciplina de Resistência dos materiais')
    course_modeling_system = BooleanField('Disciplina de Modelagem de sistemas')
    course_graphs = BooleanField('Disciplina de Grafos')
    course_conclusion_course = BooleanField('Disciplina de TCC 1')


    button_submit_edit_profile = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já cadastrado. Por gentileza, inclua outro email.')
