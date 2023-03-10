from flask import Flask
import os
from application.configs.config import Config
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        from application.routes import country
        app.register_blueprint(country.country_bp)
        db.create_all()
        return app