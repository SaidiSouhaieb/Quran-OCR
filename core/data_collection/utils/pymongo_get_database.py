from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


def get_database():

    CONNECTION_STRING = os.getenv("MONGO_DB_URL")

    client = MongoClient(CONNECTION_STRING)

    return client["Quran"]


if __name__ == "__main__":
    dbname = get_database()
