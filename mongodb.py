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
