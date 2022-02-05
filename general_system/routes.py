from flask import render_template, request, flash, redirect, url_for
from general_system import app
from general_system.forms import FormCreateAccount, FormLogin

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


@app.route("/register_login", methods=['GET', 'POST'])
def register_login():
    form_account = FormCreateAccount()
    form_login = FormLogin()

    if form_account.validate_on_submit() and "button_submit_account" in request.form:
        flash(f'Cadastro de {form_account.username.data} realizado com sucesso.', 'alert-success')
        return redirect(url_for('home'))

    if form_login.validate_on_submit() and "button_submit_login" in request.form:
        flash(f'Login de {form_login.username.data} feito.', 'alert-success')
        return redirect(url_for('home'))

    return render_template('register_login.html', form_account=form_account, form_login=form_login)
