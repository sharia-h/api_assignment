from flask import Flask
def create_app():
    app=Flask(__name__)
    with app.app_context():
        from application.routes import country
        app.register_blueprint(country.country_bp)
        return app