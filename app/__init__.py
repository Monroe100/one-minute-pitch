from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    #initializing flask extensions
    bootstrap.init_app(app)
    

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

