from flask import Blueprint, session, request, redirect, url_for,render_template
from models.model import *

app_controller = Blueprint("login", __name__)

@app_controller.route("/", methods =["GET"])
def index():
   return render_template("index.html")

@app_controller.route("/login", methods=["POST", "GET"])
def login(): 
    if request.method == "POST" :
        session["usuario"] = request.form["user"]
        return "Logado"
   
@app_controller.route("/logout")
def logout():
    session.pop('usuario', None)
    return redirect(url_for("index"))