hbz.edoweb
==========

hbz.edoweb ist ein Pythonmodul, das den Umgang mit der Elasticsearch Komponente
von `edoweb`_ erleichtern soll. Zwei Kommandozeilentools stehen zur Verfügung: 

reindex
   Zum Neuindexieren eines Index unter Verwendung einer neuen Konfiguration
  
json_es
   Pretty Printing einer Elasticsearch Suche, als Ersatz für json_pp 


Installation
------------

Das Modul hängt ab vom offiziellen `Python client für Elasticsearch`_. Da Edoweb
Elasticsearch in Version 1.1.0 verwendet, ist die richtige Version des clients entscheident.
Um die systemweite Pythoninstallation nicht zu verändern, wird eine eigene virtuelle Pythonumgebung 
verwendet. Unter Ubuntu: 

.. code-block:: bash

   $ sudo apt-get install python-virtualenv python-pip
   $ sudo virtualenv /opt/python-2.7
   $ . /opt/python-2.7/bin/activate
   $ sudo pip install "elasticsearch>=1.0.0,<2.0.0"

in edoweb:/usr/share/elasticsearch:

.. code-block:: bash

   $ sudo su
   $ cd /usr/share/elasticsearch
   $ bin/plugin -install elasticsearch/elasticsearch-analysis-icu/2.1.0
   $ bin/plugin -install com.yakaz.elasticsearch.plugins/elasticsearch-analysis-combo/1.5.1 
   $ service elasticsearch restart

   $ bin/plugin -l

   Installed plugins:
       - analysis-icu
       - head
       - analysis-combo

Build
-----

.. code-block:: bash

   $ cd /tmp
   $ git clone https://github.com/edoweb/hbz.edoweb
   $ cd hbz.edoweb
   $ . /opt/python-2.7/bin/activate
   $ sudo python setup.py install
   
Run
---

Nun steht das Kommando "reindex" zur Verfügung

.. code-block:: bash

   $ reindex -h
   
Beispiel:

.. code-block:: bash

   $ reindex -c /opt/regal/regal-api/conf/public-index-config.json frl
   $ reindex -c /opt/regal/regal-api/conf/public-index-config.json public_frl
   

.. _edoweb: https://github.com/edoweb
.. _Python client für Elasticsearch: https://pypi.python.org/pypi/elasticsearch/2.3.0
