from flask import Flask, redirect, render_template, request
#importando 
app = Flask(__name__)



@app.route("/")
def pg_principal():
    return render_template("principal.html")

@app.route("/sobre")
def pg_desenvolvedor():
    return render_template("sobre.html", methods=["GET"])

@app.route("/login", methods=["GET"])
def pg_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def pg_login_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == "Julia" and senha == "Juliaabc":
        return "voce acessou a pagina com sucesso"
    else:
        return render_template("/login.html", erro = "Acesso Negado!")

#rodando 
app.run(debug= True)