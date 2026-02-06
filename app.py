from flask import Flask, redirect, render_template, request
#importando 
app = Flask(__name__)

#senha para a pg
app.secret_key = "segredo"

lista_coment = []



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
        #redireciona = redirect
        return redirect("/comentario")
    else:
        return render_template("/login.html", erro = "Acesso Negado!")
    

    
@app.route("/comentario" , methods=["GET"])
def pg_comentario():
    return render_template("comentarios.html", lista_coment_html = lista_coment)

@app.route("/add_comentario", methods=["POST"])
def pg_add_comentario():
    comentario = request.form.get("comentario")
    lista_coment.append(comentario)
    print(lista_coment)
    return redirect("/comentario")

if __name__ == "__main__":
#rodando 
    app.run(host="0.0.0.0", port=8080, debug= True)