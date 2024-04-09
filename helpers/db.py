from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

client = MongoClient(os.environ['MONGO_URI'])
db = client.test
token = db.token

def insert_document(payload):    
    token.update_one({"user_id": payload["user_id"]}, {'$set': payload}, upsert=True)
    # print("inserted document successfully")

def fetch_document(user_id):
    db = client.test
    token = db.token
    result = token.find_one({"user_id": user_id})
    # print("fetched document status: ")
    # print(result)
    return result
