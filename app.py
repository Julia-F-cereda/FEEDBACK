from flask import Flask, render_template
#importando 
app = Flask(__name__)



@app.route("/")
def pg_principal():
    return render_template("principal.html")

@app.route("/sobre")
def pg_desenvolvedor():
    return render_template("sobre.html")

#rodando 
app.run(debug= True)