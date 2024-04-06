# After install docker just run the following commands 
# 1-docker run -d -p 27017:27017 --name m1 mongo
# 2-python mongo-test.py

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [ 
    { "name" : "Amy" , "address": "Apple st 652"},
    { "name" : "Hannah", "address": "Mountain 21"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents: 
print(x.inserted_ids)