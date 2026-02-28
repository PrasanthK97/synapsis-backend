from flask import Flask
from flask_cors import CORS
from app.routes.analyze import analyze_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10MB

    CORS(app, origins=["http://localhost:5173"])

    app.register_blueprint(analyze_bp)

    return app


