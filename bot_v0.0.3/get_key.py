#get_key_v0.0.1
import bson
from datetime import date
from pymongo import MongoClient

def get_key():
    MONGODB_URI = "mongodb+srv://preyash_user:preyash12345@workonme.b1hlp.mongodb.net/workonme"
    db = MongoClient(MONGODB_URI)['workonme']["authentication"]
    result = db.find_one({"_id": bson.ObjectId("618de38f6c40da1b3b8c2cc9")})
    current_date = date.today().year * 10000 + date.today().month * 100 + date.today().day
    if(current_date > result["expiry_date"]):
        print("#"*100)
        print("\nContact 2developer.tech to renew your licance\n")
        print("#"*100)
        exit()
    else:
        return result["key"]