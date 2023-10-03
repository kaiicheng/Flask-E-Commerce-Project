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

# # get the first data of collection
# data=collection.find_one()
# print(data)  # print out the first data

# get a data by ObjectId via bson.objectid
data=collection.find_one(
    ObjectId("6507bd50e8c477211a94f395")
    )
print("Get data successfully!")

# print all fields of a data
print(data)

# print specific fields of data
print("ID: ", end="")
print(data["_id"])
print("Email: ", end="") 
print(data["email"])
print()

# get all data
print("All data:")
cursor=collection.find()
for doc in cursor:
    print("Username: ", end="")
    print(doc["name"])
    print(doc)
