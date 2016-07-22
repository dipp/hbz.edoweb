#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse
import os.path
import sys

from datetime import datetime
from elasticsearch import Elasticsearch, helpers

from hbz.edoweb import __version__
"""
client = Elasticsearch()

now = datetime.now().strftime('%Y%m%d%H%M%S')
conf_file = "public-index-config.json"

source_index = 'edoweb'
target_index = '%s-%s' % (source_index, now)

f = open(conf_file, "r")

configuration = f.read()

client.indices.create(index=target_index, body=configuration, ignore=400)

helpers.reindex(client, source_index, target_index)
"""
client = Elasticsearch()

def create_new_index(target_index, configuration):
    
    client.indices.create(index=target_index, body=configuration, ignore=400)

def create_target_index_name(source_index):
    """Return name of target_index based on source_index
       and timestamp
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s-%s' % (source_index, now)

def reindex(source_index):
    
    if client.indices.exists(index=source_index):
        target_index = create_target_index_name(source_index)
        helpers.reindex(client, source_index, target_index)
    else:
        print "Index '%s' does not exist" % source_index
    

def main():
    
    parser = argparse.ArgumentParser(description='Reindex elastic search')
    parser.add_argument('index', help='Index')
    parser.add_argument('-c', '--conf', help='Configuration file with access data')
        
    args = parser.parse_args()
    conf_file = args.conf
    source_index = args.index
    
    if conf_file:
        if os.path.exists(conf_file):
            target_index = create_target_index_name(source_index)
            create_new_index(target_index, conf_file)
            print "Create new index"    
        else:
            print "Configuration file does not exist"
    else:
        print "Using automatic configuration"  

    if source_index:
        reindex(source_index)
    