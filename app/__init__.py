# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import index 
    app.add_url_rule('/', 'index', index)  

    from .commands import load_data_command
    app.cli.add_command(load_data_command)
    
    return app
