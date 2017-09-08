# prerequisites

from pymongo import MongoClient

# Making a connection with MongoClient
client = MongoClient('localhost', 27017)

# getting a database
db = client.test

# getting a collection
# collection = db.test_collection
posts = db.posts

# Documents
import datetime

post = {"author": "Noi",
        "text": "My first db example",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

# inserting a Document

post_id = posts.insert_one(post).inserted_id

# print(post_id)

# getting a single document with find_one()
import pprint

pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "ladin"}))

for p in posts.find():
    print(p)

# from bson.objectid import ObjectId
# #the Web framework gets post_id from the URL and passes it as a string
# def get(post_id):
# 	#convert from string to ObjectID
# 	document = client.db.collection.find_one({'_id':ObjectId(post_id)})
