import mysql.connector
from config import Config
import csv

def get_db_connection():
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )

def insert_nutrient_data(cursor, age_low, age_high, male_low, male_mod, male_high, female_low, female_mod, female_high):
    query = """
    INSERT INTO nutrient_intake (
        age_low, age_high,
        male_low_activity, male_moderate_activity, male_high_activity,
        female_low_activity, female_moderate_activity, female_high_activity
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (age_low, age_high, male_low, male_mod, male_high, female_low, female_mod, female_high))



def load_csv_to_db(file_path):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_nutrient_data(
                cursor,
                int(row['age_low']),
                int(row['age_high']),
                int(row['male_low_activity']),
                int(row['male_moderate_activity']),
                int(row['male_high_activity']),
                int(row['female_low_activity']),
                int(row['female_moderate_activity']),
                int(row['female_high_activity'])
            )
    connection.commit()
    cursor.close()
    connection.close()
    print("Data load successfully!")