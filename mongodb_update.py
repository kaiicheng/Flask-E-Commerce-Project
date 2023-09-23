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

# store data in cloud database
db=client.mywebsite  # choose "mywebsite" database
collection=db.users  # choose "users" collections

# get a data by ObjectId via bson.objectid
data=collection.find_one(
    ObjectId("6507bc63805cacca28a35934")
    )
print("Get data successfully!")

# print all fields of a data
print(data)



# 1
print(1)
# update a data in the collection
# update_one({...keyword that matches...}, {"$set" : {{...updated data...}})
result = collection.update_one({
    "email" : "bob@bob.com"
}, {
    "$set" : {
        "password" : "bob"
    }
})
# print out matching result
print("Number of matching data: ", result.matched_count)
print("Number of data updated: ", result.modified_count)
# get a data by ObjectId via bson.objectid
data=collection.find_one(
    ObjectId("6507bc63805cacca28a35934")
    )
print("Get data successfully!")
# print all fields of a data
print(data)



# 2
print(2)
# add a new field to a data in the collection
# update_one({...keyword that matches...}, {"$set" : {{...updated data...}})
result = collection.update_one({
    "email" : "bob@bob.com"
}, {
    "$set" : {
        "description" : "Hello, I'm Kai!"  # add one more new "description" field
    }
})
# print out matching result
print("Number of matching data: ", result.matched_count)
print("Number of data updated: ", result.modified_count)
# get a data by ObjectId via bson.objectid
data=collection.find_one(
    ObjectId("6507bc63805cacca28a35934")
    )
print("Get data successfully!")
# print all fields of a data
print(data)



# 3
print(3)
# unset (delete) a field of a data in the collection
# update_one({...keyword that matches...}, {"$set" : {{...updated data...}})
result = collection.update_one({
    "email" : "bob@bob.com"
}, {
    "$unset" : {
        # "password" : "test"
        "description" : "Hello, I'm Kai!"
    }
})
# print out matching result
print("Number of matching data: ", result.matched_count)
print("Number of data updated: ", result.modified_count)
# get a data by ObjectId via bson.objectid
data=collection.find_one(
    ObjectId("6507bc63805cacca28a35934")
    )
print("Get data successfully!")
# print all fields of a data
print(data)



# 4
print(4)
# increase a field of a data in the collection
# update_one({...keyword that matches...}, {"$set" : {{...updated data...}})
result = collection.update_one({
    "email" : "bob@bob.com"
}, {
    "$inc" : {
        "level" : 2
    }
})
# print out matching result
print("Number of matching data: ", result.matched_count)
print("Number of data updated: ", result.modified_count)
# get a data by ObjectId via bson.objectid
data=collection.find_one(
    ObjectId("6507bc63805cacca28a35934")
    )
print("Get data successfully!")
# print all fields of a data
print(data)



# 5
print(5)
# multiply a field of a data in the collection
# update_one({...keyword that matches...}, {"$set" : {{...updated data...}})
result = collection.update_one({
    "email" : "bob@bob.com"
}, {
    "$mul" : {
        "level" : 0.5
    }
})
# print out matching result
print("Number of matching data: ", result.matched_count)
print("Number of data updated: ", result.modified_count)
# get a data by ObjectId via bson.objectid
data=collection.find_one(
    ObjectId("6507bc63805cacca28a35934")
    )
print("Get data successfully!")
# print all fields of a data
print(data)



# update many data in the collection
result=collection.update_many({
    "level" : 1
}, {
    "$set" : {
        "level" : 4
    }
})
# print out matching result
print("Number of matching data: ", result.matched_count)
print("Number of data updated: ", result.modified_count)
# get a data by ObjectId via bson.objectid
data=collection.find_one(
    ObjectId("6507bc63805cacca28a35934")
    )
print("Get data successfully!")
# print all fields of a data
print(data)
