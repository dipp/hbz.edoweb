#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
from elasticsearch import Elasticsearch, helpers

client = Elasticsearch()

now = datetime.now().strftime('%Y%m%d%H%M%S')
conf_file = "public-index-config.json"

source_index = 'edoweb'
target_index = '%s-%s' % (source_index, now)

f = open(conf_file, "r")

configuration = f.read()

client.indices.create(index=target_index, body=configuration, ignore=400)

helpers.reindex(client, source_index, target_index)

def main():
    print "hallo Welt"