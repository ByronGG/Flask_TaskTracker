from flask import Flask
from src.database.config import Config
from src.routes.task_routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Registro Blueprints
    app.register_blueprint(task_bp)
    return app