#!/usr/bin/python

# -*- coding: utf-8 -*-
import json
import pymongo
import sys
import fileinput

reload(sys)
sys.setdefaultencoding('utf-8')

client = pymongo.MongoClient()
db = client.topics
coll = db.topic1

for line in fileinput.input():
    doc = coll.insert_one(json.loads(line))
    print doc 
