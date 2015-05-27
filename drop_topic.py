#!/usr/bin/python

import pymongo 
import json

client = pymongo.MongoClient()

db = client.topics
db.drop_collection('topic1')

