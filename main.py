from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCreateAccount, FormLogin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ca79946617c662a483d0a5f0f1a179af'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase_modeling_systems.db'

data_base = SQLAlchemy(app)


set_users = ['Ana', 'Bruna', 'Larissa', 'Sofia', 'Maria Eduarda', 'Maria Clara']


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


@app.route("/users")
def users():
    return render_template('users.html', set_users=set_users)


@app.route("/register_login",  methods=['GET', 'POST'])
def register_login():
    form_account = FormCreateAccount()
    form_login = FormLogin()

    if form_account.validate_on_submit() and 'button_submit_create_account' in request.form:
        flash(f'Cadastro de {form_account.email.data} realizado com sucesso.', 'alert-success')
        return redirect(url_for('home'))
    if form_login.validate_on_submit() and 'button_submit_login' in request.form:
        flash(f'Login de {form_login.email.data} feito.', 'alert-success')
        return redirect(url_for('home'))

    return render_template('register_login.html', form_account=form_account, form_login=form_login)


if "__main__" == __name__:
    app.run(debug=True)