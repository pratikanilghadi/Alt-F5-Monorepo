from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("PINECONE")

def get_pine_client():
    try:
        pc = Pinecone(api_key=api_key)
        return pc
    except Exception as e:
        print(e)
        return False