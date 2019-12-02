from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import config

mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .owners import owners as owners_blueprint
    app.register_blueprint(owners_blueprint, url_prefix='/owners')

    from .games import games as games_blueprint
    app.register_blueprint(games_blueprint, url_prefix='/games')

    from .teams import teams as teams_blueprint
    app.register_blueprint(teams_blueprint, url_prefix='/teams')

    return app
