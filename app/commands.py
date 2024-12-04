import click
from app.db_utils import load_calories_to_db


@click.command('load-calories')
@click.argument('file_path')
def load_calories(file_path):
    """Loading calories from CSV to calories table"""
    load_calories_to_db(file_path)