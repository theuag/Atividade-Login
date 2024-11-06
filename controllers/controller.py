from flask import *
from models.model import logado, Login

app_controller = Blueprint("login", __name__)

@app_controller.route("/")
def index():
   return render_template("index.html")

@app_controller.route("/verifica", methods=["POST", "GET"])
def verifica(): 
        user = request.form["user"]
        senha = request.form["senha"]
        for usuario in logado:
            if  Login.usuario == user:
                if Login.__senha__ == senha:
                    session["usuario"] = request.form["user"]
            return redirect(url_for("login.questoes"))
        else: 
           flash("Algo esta erado, tente novamente", "error")

@app_controller.route("/questoes", methods = ["GET", "POST"])
def questionario():
    if request.method == "POST":
        resposta1 = request.form["pergunta1"]
        resposta2 = request.form["pergunta2"]
        response = make_response(render_template("resposta.html"))
        
        if resposta1 == "janeiro":
            response.set_cookie("resposta1", "Correto", max_age = 60 * 60 * 24)
        else:
            response.set_cookie("resposta1", "Incorreto", max_age = 60 * 60 * 24)
        
        if resposta2 == "2024":
            response.set_cookie("resposta2", "Correto", max_age = 60 * 60 * 24)
        else:
            response.set_cookie("resposta2", "Incorreto", max_age = 60 * 60 * 24)
        
        return response
    return render_template("resposta.html")

   
@app_controller.route("/logout")
def logout():
    resp = make_response(redirect(url_for(".index")))
    session.pop("user", None)
    resp.set_cookie("resposta1", "", expires = 0)
    resp.set_cookie("resposta2", "", expires = 0)
    return resp