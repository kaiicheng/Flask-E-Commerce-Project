# download mongoDB locally on terminal
# pip install pymongo[srv]

# import pymongo library
import pymongo

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

# # create a "test" database
# # store data in cloud database
# db=client.test  # choose "test" database
# collection=db.users  # choose "users" collections
# # put data in the collection (in JSON format)
# collection.insert_one({
#     "name" : "Kai",
#     "gender" : "Male"
# })

# # create a "website" database
# # store data in cloud database
# db=client.website  # choose "website" database
# collection=db.members  # choose "members" collections
# # put data in the collection (in JSON format)
# collection.insert_one({
#     "email" : "test@test.com",
#     "password" : "test"
# })

# create a "mywebsite" database
# store data in cloud database
db=client.mywebsite  # choose "mywebsite" database
collection=db.users  # choose "users" collections
# put data in the collection (in JSON format)
# collection.insert_one({
#     "name" : "Alice",
#     "email" : "alice@alice.com",
#     "password" : "alice",
#     "level" : 2
# })
# # save the result in a variable "result" of data in the collection (in JSON format)
# result = collection.insert_one({
#     "name" : "Bob",
#     "email" : "bob@bob.com",
#     "password" : "bob",
#     "level" : 3
# })
# save many data at one time
result=collection.insert_many([{
    "name" : "Charlie",
    "email" : "charlie@charlie.com",
    "password" : "charlie",
    "level" : 5
},{
    "name" : "Daniel",
    "email" : "daniel@daniel.com",
    "password" : "daniel",
    "level" : 4
}])

print("Data added successfully!")
# print(result.inserted_id)  # print out id of the data added
print(result.inserted_ids)  # print out all ids of the data added
