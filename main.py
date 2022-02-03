from flask import Flask, render_template

from forms import FormCreateAccount, FormLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ca79946617c662a483d0a5f0f1a179af'

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
    ca = FormCreateAccount()
    cl = FormLogin()
    return render_template('register_login.html', ca=ca, cl=cl)


if "__main__" == __name__:
    app.run(debug=True)
