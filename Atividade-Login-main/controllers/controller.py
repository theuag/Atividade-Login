from flask import *
from models.model import *

app_controller = Blueprint("login", __name__)

@app_controller.route("/", methods =["GET"])
def index():
   return render_template("index.html")

@app_controller.route("/login", methods=["POST", "GET"])
def login(): 
    if request.method == "POST":
        if request.form["usuario"]==logado.usuario and request.form["senha"] == logado.getSenha():
            session["usuario"] = request.form["user"]
            return "Logado"
        else:
            flash("Login incorreto", "error")
    return redirect(url_for("/login"))
   
@app_controller.route("/login", methods=["DELETE"])
def logout():
    session.pop('usuario', None)
    return redirect(url_for("/"))
