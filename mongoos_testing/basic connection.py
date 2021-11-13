import datetime
import os

from pymongo import MongoClient

# Load config from a .env file:
MONGODB_URI = "mongodb+srv://preyash_user:preyash12345@workonme.b1hlp.mongodb.net/workonme"

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
# for db_info in client.list_database_names():
#    print(db_info)

# Get a reference to the 'sample_mflix' database:
db = client['workonme']

# List all the collections in 'sample_mflix':
# collections = db.list_collection_names()
# for collection in collections:
#    print(collection)

# collection
auth = db["authentication"]
print(auth.find_one())