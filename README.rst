hbz.edoweb
==========

hbz.edoweb ist ein Pythonmodul, das den Umgang mit der Elastic Search Komponente
von `edoweb`_ leichter machen soll. 

 reindex
   Zum Neuindexieren eines Index unter Verwendung einer neuen Konfiguration
  
 json_es
   Pretty Printing einer elastic search Suche, als Ersatz für json_pp 
 

Installation
------------


.. code-block:: bash

   $ apt-get install python-virtualenv
   $ virtualenv /opt/python-2.7
   $ . /opt/python-2.7/bin/activate
   $ pip install "elasticsearch>=1.0.0,<2.0.0"

in edoweb:/usr/share/elasticsearch:

.. code-block:: bash

   $ bin/plugin -install elasticsearch/elasticsearch-analysis-icu/2.1.0
   $ bin/plugin -install com.yakaz.elasticsearch.plugins/elasticsearch-analysis-combo/1.5.1 
   $ /etc/init.d/elasticsearch restart

   $ bin/plugin -l

   Installed plugins:
       - analysis-icu
       - head
       - analysis-combo

       
.. _edoweb: https://github.com/edoweb