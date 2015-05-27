#!/usr/bin/python

# -*- coding: utf-8 -*-
import requests
import urllib
import json
import pymongo

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

client = pymongo.MongoClient()
db = client.topics
coll = db.topic1

solr_base_url = "http://rel-lb-solr-p200.dmz.kb.nl/solr/DDD_artikel/select/?wt=json&fl=uniqueKey"
#current_year = int(sys.argv[1])

def mk_period(year):
	base_str = "2/20e_eeuw/"
	range1 = (year / 10) * 10
	range2 = range1 + 9
	return "\"" + base_str + str(range1) + "-" + str(range2) + "/" + str(year) + "/" + "\""

def store_total(year):
	fq = "periode:" + mk_period(year)
	solr_url = solr_base_url
	solr_url += "&rows=0"
	solr_url += "&" + urllib.urlencode({"q": "*:*"})
	solr_url += "&" + urllib.urlencode({"fq": fq})
	solrresp = requests.get(solr_url)
	solrbod = json.loads(solrresp.text)
	numfound = solrbod["response"]["numFound"]
	coll.replace_one({'total_year': year}, {'total_year': year, 'amount': numfound}, True)
	print coll.find_one({'total_year': year})

def process(keyword, year):
	rows = 10000
	start = 0
	article_urns = []
	q = "content:\"" + keyword + "\""
	fq = "periode:" + mk_period(year)
	while True:
		solr_url = solr_base_url
		solr_url += "&rows=" + str(rows)
		solr_url += "&start=" + str(start)
		solr_url += "&" + urllib.urlencode({"q": q})
		solr_url += "&" + urllib.urlencode({"fq": fq})
		solrresp = requests.get(solr_url)
		solrbod = json.loads(solrresp.text)
		numfound = solrbod["response"]["numFound"]
		print str(year) + ": word: " + keyword + " found: " + str(numfound) + " start: " + str(start)
		sys.stdout.flush()
		start += rows
		for i in range(len(solrbod["response"]["docs"])):
			doc = coll.find_one({'id': solrbod["response"]["docs"][i]["uniqueKey"]})
			if doc == None:
				doc = {
					'id': solrbod["response"]["docs"][i]["uniqueKey"],
					'tok_amount': 0,
					'tokens': [],
					'year': year
				}
			doc['tokens'].append(keyword)
			doc['tokens'] = list(set(doc['tokens']))
			doc['tok_amount'] = len(doc['tokens'])
			coll.replace_one({'id': doc['id']}, doc, True)


		if start > numfound:
			break


for current_year in range(1931, 1998):
	store_total(current_year)
	f = open("keywords.txt", "r")
	lines = f.readlines()
	for line in lines:
		process(line.rstrip(), current_year)



