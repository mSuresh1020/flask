from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db=SQLAlchemy()

def create_app(config_name):
    app =Flask(__name__)
    app.config.from_object(app_config[config_name])
    from first_flask_db.details.views import mod as anyname             ## User module any define
    db.init_app(app)

    app.register_blueprint(anyname)
    return app