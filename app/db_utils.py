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


def load_calories_to_db(path):
    # CSV data (you could also read this from a file)
    csv_data = csv.reader(path)

    # Parse the CSV
    data = []
    csv_reader = csv.DictReader(csv_data.splitlines())
    for row in csv_reader:
        age_diapason = f"{row['age_low']}-{row['age_high']}"
        for sex in ['male', 'female']:
            for activity, activity_level in [
                (f"{sex}_low_activity", "low_activity"),
                (f"{sex}_moderate_activity", "moderate_activity"),
                (f"{sex}_high_activity", "high_activity"),
            ]:
                calorie = int(row[activity])
                data.append((age_diapason, sex, activity_level, calorie))

    # Connect to MySQL
    db = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )
    cursor = db.cursor()

    # Insert data into the table
    insert_query = """
    INSERT INTO calories (age_diapason, sex, activity_level, calorie)
    VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(insert_query, data)

    # Commit changes and close connection
    db.commit()
    cursor.close()
    db.close()

    return "Data inserted successfully!"