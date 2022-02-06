"""
home, contacts, users - Associated with the main pages. These functions are statics.
register_login - Associated with pages if the user is not logged in the site.
logout, my_profile, create_posts - Associated with restrict pages. A person just access if it has done the login.

Ps: current_user is not used in this module. But it is necessary import it to use in the navbar.

"""

from flask import render_template, request, flash, redirect, url_for
from general_system import app, data_base, bcrypt
from general_system.forms import FormCreateAccount, FormLogin
from general_system.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required

set_users = ['Ana', 'Bruna', 'Larissa', 'Sofia', 'Maria Eduarda', 'Maria Clara']


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


@app.route("/users")
@login_required
def users():
    return render_template('users.html', set_users=set_users)


@app.route("/register_login", methods=['GET', 'POST'])
def register_login():
    form_account = FormCreateAccount()
    form_login = FormLogin()

    if form_account.validate_on_submit() and "button_submit_account" in request.form:
        password_encrypted = bcrypt.generate_password_hash(form_account.password.data)
        people = Usuario(username=form_account.username.data, email=form_account.email.data,
                         password=password_encrypted)
        data_base.session.add(people)
        data_base.session.commit()
        flash(f'Cadastro de {form_account.username.data} realizado com sucesso.', 'alert-success')
        return redirect(url_for('home'))

    if form_login.validate_on_submit() and "button_submit_login" in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form_login.password.data):
            login_user(usuario, remember=form_login.remember_password.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'Falha no Login. E-mail ou Senha Incorretos', 'alert-danger')

    return render_template('register_login.html', form_account=form_account, form_login=form_login)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f'Logout realizado com sucesso', 'alert-success')
    return redirect(url_for('home'))


@app.route("/my_profile")
@login_required
def my_profile():
    return render_template('my_profile.html')


@app.route("/post/create")
@login_required
def create_post():
    return render_template('create_posts.html')
