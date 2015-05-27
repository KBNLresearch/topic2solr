#!/usr/bin/python

import pymongo 
import json

client = pymongo.MongoClient()

db = client.topics

coll = db.topic1

print("indexing...")
coll.create_index([("id", pymongo.ASCENDING)])
coll.create_index([("tok_amount", pymongo.ASCENDING)])
coll.create_index([("year", pymongo.ASCENDING)])
coll.create_index([("tokens", pymongo.ASCENDING)])
coll.create_index([("total_year", pymongo.ASCENDING)])

#print("autowarming...")
#for num in range(1, 15):
#	print(coll.aggregate([
#		{"$match": {"tok_amount": {"$gte": num}}},
#		{"$group": {"_id": "$year", "total": {"$sum": 1}}}
#	]))
