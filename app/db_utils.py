import mysql.connector
from config import Config, AGE_DIAPASONS
import csv


def get_db_connection():
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )


def load_calories_to_db(path):
    """Load CSV data to the database."""

    csv_data = csv.reader(path)
    data = []
    csv_reader = csv.DictReader(csv_data.splitlines())
    for row in csv_reader:
        age_diapason = f"{row['age_low']}-{row['age_high']}"
        for sex in ['male', 'female']:
            for activity, activity_level in [
                (f"{sex}_low_activity", "low"),
                (f"{sex}_moderate_activity", "moderate"),
                (f"{sex}_high_activity", "high"),
            ]:
                calorie = int(row[activity])
                data.append((age_diapason, sex, activity_level, calorie))

    db = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )
    cursor = db.cursor()

    insert_query = """
    INSERT INTO calories (age_diapason, sex, activity_level, calorie)
    VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(insert_query, data)

    db.commit()
    cursor.close()
    db.close()

    return "Data inserted successfully!"


def calculate_age_diapason(age):
    for age_diapason in AGE_DIAPASONS:
        age_low, age_high = map(int, age_diapason.split('-'))
        if age_low <= age <= age_high:
            return age_diapason
    return None


def get_calories(age , sex, activity_level):
    """Perform SQL queries to get the calories."""

    age_diapason = calculate_age_diapason(age)
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    data = (age_diapason, sex, activity_level)

    query = "SELECT calorie FROM calories WHERE age_diapason = %s AND sex = %s AND activity_level = %s"
    
    # Print the query and data for debugging
    # print("Executing query:", query)
    # print("With data:", data)

    cursor.execute(query, data)
    result = cursor.fetchall()

    # Print the result for debugging
    # print("Query result:", result)

    cursor.close()
    db.close()
    
    if result and len(result) > 0:
        return result[0]['calorie']
    else:
        return None 