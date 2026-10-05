import os
import secrets
import warnings

from flask import Flask
from app.extensions import db, csrf

# 🔥 IMPORTAR MODELOS PARA QUE SQLALCHEMY LOS DETECTE
from app import models
from app.routes import main


def resolve_secret_key():
    """Devuelve la clave de la sesion leida del entorno.

    Nunca se escribe una clave fija en el codigo: si la variable de entorno
    SECRET_KEY no esta definida se genera una aleatoria y se avisa, de modo que
    las sesiones se invalidan al reiniciar pero no se filtran credenciales.
    La clave tambien firma los tokens CSRF de Flask-WTF.
    """
    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key:
        warnings.warn(
            "SECRET_KEY no esta definida en el entorno; "
            "se genera una clave aleatoria para esta ejecucion.",
            RuntimeWarning,
            stacklevel=2,
        )
        secret_key = secrets.token_hex(32)
    return secret_key


def create_app():

    app = Flask(__name__,
                static_folder="../static",
                template_folder="../templates")
    
    # 🔥 Configuración SQLite
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///adcalcsci.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = resolve_secret_key()

    # 🔐 Protección CSRF: exige token en register, login, calculadora y borrar
    csrf.init_app(app)

    # Inicializar base de datos
    db.init_app(app)

# 🔥 IMPORTAR MODELOS PARA QUE SQLALCHEMY LOS DETECTE
    app.register_blueprint(main)
    return app