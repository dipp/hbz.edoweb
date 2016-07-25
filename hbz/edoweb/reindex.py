#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse
import os.path
import sys

from datetime import datetime
from elasticsearch import Elasticsearch, helpers

client = Elasticsearch()

def create_target_index_name(source_index):
    """Return name of target_index based on source_index
       and timestamp
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s-%s' % (source_index, now)

def reindex(source_index):
    """ Reindex a given index to a newly created one.
    
    Returns number of successfully executed actions.    
    """
    
    target_index = create_target_index_name(source_index)
    
    exists_source = client.indices.exists(index=source_index)
    exists_target = client.indices.exists(index=target_index)
         
    if exists_source and exists_target:
        actions, errors = helpers.reindex(client, source_index, target_index) 
        return actions
    else:
        return None

def main():
    
    parser = argparse.ArgumentParser(description='Reindex a given elastic search (ES) index into a new index \
        based on a provided configuration file. Works only with ES running on localhost.')
    parser.add_argument('index', help='Name of the elastic search index')
    parser.add_argument('-c', '--conf', help='Configuration file with settings and mappings')
        
    args = parser.parse_args()
    conf_file = args.conf
    source_index = args.index
    
    if not client.indices.exists(index=source_index):
        print "Index '%s' does not exist" % source_index
        sys.exit()
    
    if conf_file:
        if os.path.exists(conf_file): 
            f = open(conf_file, "r")
            configuration = f.read()
            target_index = create_target_index_name(source_index)
            client.indices.create(index=target_index, body=configuration, ignore=400)
            print "Create new index '%s'" % target_index     
        else:
            print "Configuration '%s' file does not exist" % conf_file
            sys.exit()

    if source_index :
        actions = reindex(source_index)
        print "Actions: %s" % actions   
    