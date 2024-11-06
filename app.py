from flask import *
from controllers.controller import app_controller

app = Flask(__name__)
app.secret_key = "6b61d6f501bd285d397a40a984959a05"


rotas_publicas = ["login.index", "login.verifica"]

@app.before_request
def verificaSessao():
    if request.endpoint in rotas_publicas:
        return
    return

app.register_blueprint(app_controller)

if __name__ == "__main__" :
    app.run(debug = True)