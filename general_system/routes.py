"""
home, contacts, users - Associated with the main pages. These functions are statics.
register_login - Associated with pages if the user is not logged in the site.
logout, my_profile, create_posts - Associated with restrict pages. A person just access if it has done the login.

Ps: current_user is not used in this module. But it is necessary import it to use in the navbar.

"""

import secrets
import os
from flask import render_template, request, flash, redirect, url_for
from general_system import app, data_base, bcrypt
from general_system.forms import FormCreateAccount, FormLogin, FormEditProfile
from general_system.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required
from PIL import Image

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
            # Cath a specific parameter in the url
            next_parameter = request.args.get('next')
            if next_parameter:
                return redirect(next_parameter)
            else:
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
    image_id = url_for('static', filename='image_id_user/{}'.format(current_user.perf_photo))
    return render_template('my_profile.html', image_id=image_id)


def save_image_profile(image_profile):
    # code of image
    code_img = secrets.token_hex(8)
    # filename = name of the image with the extension
    # separate the name of the extension
    name_img, extension_img = os.path.splitext(image_profile.filename)

    # group name+code+extension
    name_file = name_img + code_img + extension_img

    # complete_path to save file in the images directory
    all_path = os.path.join(app.root_path, 'static/image_id_user', name_file)

    # Reduce the px of image and save image in the directory
    length = (400, 400)
    reduced_image = Image.open(image_profile)
    reduced_image.thumbnail(length)
    reduced_image.save(all_path)

    return name_file

@app.route("/my_profile/edit_profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    form_profile = FormEditProfile()
    image_id = url_for('static', filename='photo_profile/{}'.format(current_user.perf_photo))
    # Changing email or username
    if form_profile.validate_on_submit():
        current_user.username = form_profile.username.data
        current_user.email = form_profile.email.data
        if form_profile.photo_profile.data:
            name_file = save_image_profile(form_profile.photo_profile.data)
            current_user.perf_photo = name_file
        data_base.session.commit()
        flash(f'Edição feita com sucesso', 'alert-success')
        return redirect(url_for('my_profile'))
    # Automatic fill in the forms.
    elif request.method == 'GET':
        form_profile.username.data = current_user.username
        form_profile.email.data = current_user.email
    return render_template('edit_profile.html', image_id=image_id, form_profile=form_profile)


@app.route("/post/create")
@login_required
def create_post():
    return render_template('create_posts.html')
