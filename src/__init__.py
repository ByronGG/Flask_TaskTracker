from flask import Flask
from src.database.config import Config
from src.routes.task_routes import task_bp

def create_app():
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrar Blueprints
    app.register_blueprint(task_bp)

    return app
