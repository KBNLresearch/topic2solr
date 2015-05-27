Mongodb
---
Om lokaal te draaien op ubuntu:
```
sudo apt-get install mongodb
```

By default draait mongodb op localhost, poort 27017, voor kbresearch kun je het best aan WJ vragen om het ip-adres of in mijn home dir.

load_topics.py
---
Voert een scrape uit op solr van de woorden uit keywords.txt en vult de mongodb.
De volgende variabelen moeten nog geparameteriseerd worden:
- solr_base_url (bijv. "http://tomcat7.kbresearch.nl/solr/DDD_artikel_research/select/?wt=json&fl=uniqueKey")
- de naam van de database collection (is nu topic1)
- startjaar en eindjaar (nu 1931 - 1998)
- Het bronbestand voor de te zoeken woorden (of uit stdin of anderszins)



Datamodel:
Een record in topic1:
```
{
  "tokens": ["wetenschappelijke", "rol"], 
  "year": 1995, 
  "id": "ddd:010644822:mpeg21:a0122", 
  "tok_amount": 2
}
```
Jaartotaal in topic1 (om percentages te kunnen tonen):
```
{
  "amount": 553179,
  "total_year": 1901
}
```


keywords.txt
---
De woordenlijst

update_indexes.py
---
Maakt indexes aan op alle doorzoekbare velden in mongodb. Te draaien voor of na laden van de set.

webapp.rb
---
De webapp die grafieken tekent (ruby 1.9.x, of 2.x). Gem dependencies:
```
sudo gem install sinatra mongo json # json zit in de 2.x core dus is daar geen gem dependency
```
starten:
```
ruby webapp.rb -p [poortnummer] # poort is 4567 by default
```

drop_topic.py
---
Gooit de hele mongodb collection topic1 weg.

dump.py
---
Maakt een datadump van de hele topic1 collection (platte tekst, rijen van jsonformaat)

load.py
---
Laadt de datadump
