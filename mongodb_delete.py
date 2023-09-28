# import pymongo library
import pymongo

# import objectid to get id of data
from bson.objectid import ObjectId

# conntect to MongoDB cloud database
# copy and paste from MongoDB website
from pymongo.mongo_client import MongoClient

uri="mongodb+srv://root:root123@kaicluster.f9neu2k.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client=MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# get cloud database
db=client.mywebsite  # choose "mywebsite" database
collection=db.users  # choose "users" collections

# delete one data
result=collection.delete_one({
    "email": "charlie@charlie.com"
})
print("Delete one data successfully!")
print("Number of deleted data: ", result.deleted_count)

# delete many data
result=collection.delete_many({
    "level": 4
})
print("Delete multiple data successfully!")
print("Number of deleted data: ", result.deleted_count)

