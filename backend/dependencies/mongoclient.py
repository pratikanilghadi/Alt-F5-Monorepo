from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri=os.getenv("MONGODB")

def fetchDBClient():
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return client
        except Exception as e:
            print(e)
            return False
    except Exception as e:
        print(e)
        return False

