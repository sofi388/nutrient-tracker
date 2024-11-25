import click
from app.db_utils import load_csv_to_db

@click.command('load-data')
@click.argument('file_path')
def load_data_command(file_path):
    """Loading data from CSV to nutrient_intake tab;e"""
    load_csv_to_db(file_path)
