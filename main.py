from flask import Flask, render_template, request, flash, redirect
import json


app = Flask(__name__)
app.config['SECRET_KEY']= "password"

@app.route("/")
def home():
    return render_template("html/login.html")

@app.route('/login', methods=['POST'])
def login():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)
        cont = 0
        for usuario in usuarios:
            cont += 1

            if nome == 'adm' and senha == '000':
                return render_template("html/administrador.html")

            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template("html/usuarios.html")
            
            if cont >= len(usuarios):
                flash('USUARIO INVALIDO')
                return redirect("/")

@app.route("/cadastrarUsuario", methods=['POST'])
def cadastrarUsuario():
    user = []
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    user = [
        {
            "nome": nome,
            "senha": senha
        }
    ]
    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)

    usuarioNovo = usuarios + user

    with open('usuarios.json', 'w' ) as gravarTemp:
        json.dump(usuarioNovo, gravarTemp, indent=4)

    return render_template("html/administrador.html")


if __name__ in "__main__":
    app.run(debug=True)