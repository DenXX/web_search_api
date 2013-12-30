Python Web Search API wrapper
==============

Python wrapper for Bing and Google Web Search API. 

Installation
------------

This software depends on json module only. Python 2.6 includes json, for Python <2.6 simple_json is required.

To install download the source and run:

    sudo python setup.py install

This version has been tested under Python 2.7, and should run on any 2.5 <= Python < 3.0.

Documentation
-------------

Here is a simple example:
    from web_search_api import SearchProxy
    proxy = SearchProxy(engine='bing', api_key='<YOUR BING API KEY>')
    serp = proxy.search('Who is John Galt?')
    print serp

----------------

Copyright (c) 2013 Denis Savenkov
