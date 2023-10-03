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

# filter one data
print("Filter one data.")
doc=collection.find_one({
    "email":"daniel@daniel.com"
})
print("Matching data: ", doc)
print("Matching data (Name field): ", doc["name"])

# filter one data with conditional and
print("Filter one data with conditional and.")
doc=collection.find_one({
    "$and": [
        {"email":"daniel@daniel.com"},
        {"password":"daniel"}
    ]
})
print("Matching data: ", doc)
print("Matching data (Name field): ", doc["name"])

# filter one data with conditional or
print("Filter one data with conditional or.")
cur=collection.find_one({
    "$or": [
        {"email":"alice@alice.com"},
        {"level":4}
    ]
})
print("Matching data: ", doc)
print("Matching data (Name field): ", doc["name"])

# filter multiple data
print("Filter multiple data.")
cur=collection.find({
    "$or": [
        {"email":"alice@alice.com"},
        {"level":4}
    ]
})
for doc in cur:
    print("Matching data: ", doc)
    print("Matching data (Name field): ", doc["name"])

# filter multiple data in descending order
print("Filter multiple data in descending order.")
cur=collection.find({
    "$or": [
        {"email":"alice@alice.com"},
        {"level":4}
    ]
}, sort=[
    ("level", pymongo.DESCENDING)
])
for doc in cur:
    print("Matching data: ", doc)
    print("Matching data (Name field): ", doc["name"])