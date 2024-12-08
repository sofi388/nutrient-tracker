from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MYSQL_HOST = os.getenv('DB_HOST')
    MYSQL_USER = os.getenv('DB_USER')
    MYSQL_PASSWORD = os.getenv('DB_PASSWORD')
    MYSQL_DB = os.getenv('DB_NAME')


AGE_DIAPASONS = [
    "0-2", "3-3", "4-4", "5-5", "6-6", "7-7", "8-8", "9-9", "10-10", "11-11",
    "12-12", "13-13", "14-14", "15-15", "16-16", "17-17", "18-18", "19-20",
    "21-25", "26-30", "31-35", "36-40", "41-45", "46-50", "51-55", "56-60",
    "61-65", "66-70", "71-75", "76-1000"
]