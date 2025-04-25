from flask import Flask, render_template, request, session
from app import app

@app.route("/", methods=["GET", "POST"])
def index():
    if 'expressao' not in session:
        session['expressao'] = ""

    if request.method == "POST":
        botao = request.form['botao']

        if botao == "=":
            try:
                resultado = eval(session['expressao'])
                session['expressao'] = str(resultado)
            except Exception:
                 session['expressao'] = "Erro"
        else:
            session['expressao'] += botao
                 
    display = session['expressao']

    return render_template("index.html", display=display)