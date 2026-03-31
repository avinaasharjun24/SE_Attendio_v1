import logging

from flask import Flask

from config import Config
from routes.admin_routes import admin_bp
from routes.attendance_management_routes import attendance_management_bp
from routes.attendance_routes import attendance_bp
from routes.auth_routes import auth_bp
from routes.report_routes import dashboard_ui_bp, report_bp
from routes.student_routes import student_bp
from routes.system_routes import system_bp
from routes.ui_routes import ui_bp
from services.auth_service import bcrypt
from utils.db import initialize_database
from utils.response import api_response


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    bcrypt.init_app(app)
    _configure_logging(app)

    # Register versioned API blueprints.
    app.register_blueprint(ui_bp)
    app.register_blueprint(dashboard_ui_bp)
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(admin_bp, url_prefix="/api/v1")
    app.register_blueprint(attendance_management_bp, url_prefix="/api/v1")
    app.register_blueprint(attendance_bp, url_prefix="/api/v1")
    app.register_blueprint(report_bp, url_prefix="/api/v1")
    app.register_blueprint(student_bp, url_prefix="/api/v1")
    app.register_blueprint(system_bp, url_prefix="/api/v1")

    with app.app_context():
        connected, result, error_message = initialize_database()
        if connected:
            app.logger.info("Startup database check passed: %s", result)
        else:
            app.logger.error("Startup database check failed: %s", error_message)

    @app.get("/health")
    def health_check():
        return api_response(True, "Attendance auth module is running", {}, 200)

    return app


def _configure_logging(app):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
    app.logger.setLevel(logging.INFO)


app = create_app()


if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
