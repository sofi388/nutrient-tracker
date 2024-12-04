# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import index 
    app.add_url_rule('/', 'index', index)  

    from .routes import calculate_calorie_intake
    app.add_url_rule('/calculate', 'calculate_calorie_intake', calculate_calorie_intake, methods=["GET", "POST"])

    from .routes import check_ferrum_level
    app.add_url_rule('/calculate_ferrum', 'check_ferrum_level', check_ferrum_level, methods=["GET", "POST"])

    from .commands import load_data_command
    app.cli.add_command(load_data_command)
    return app