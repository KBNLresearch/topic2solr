#!/usr/bin/python

import pymongo 
import json

client = pymongo.MongoClient()

db = client.topics

coll = db.topic1

for doc in coll.find():
	doc.pop("_id", None)
	print json.dumps(doc)
