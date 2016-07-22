#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# json_es.py ist ein kleines Helferskript, das statt json_pp genutzt werden kann, 
# um das Ergebnis von Elastic Search Suchen etwas kompakter auszugeben. 
# Er werden nur die Zahl der Treffer (hits) und die Werte des @id und title Feldes
# ausgeben. Bei Umlautsuchen müssen die Umlaute urlencoded werden. 
# 
# $ curl -XGET 'localhost:9200/edoweb/_search?q=title:Nebenth%C3%A4ler' | ./json_es.py

import sys
import json

def main():
    data = sys.stdin.readlines()
    if len(data) == 1:
        x = json.loads(data[0])
    
    hits = x['hits']['total']
    
    print '\nHits: ', hits
    
    for hit in x['hits']['hits']:
        source = hit['_source']
        id = source['@id']
        title = source['title'][0]
        print "%s, %s" % (id, title)
