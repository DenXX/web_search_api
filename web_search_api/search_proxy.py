#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module implements search providers returning a set of search
    results for a query. You can create an instance of SearchProxy
    object passing the name of search to use and call its search(query)
    method to get search results.

    Copyright (C) 2013 Denis Savenkov <denissavenkov@gmail.com>
"""

from abc import abstractmethod
import pickle
import re
import urllib
import urllib2

from search_provider import SearchProvider
from bing_search_provider import BingSearchProvider

class SearchProxy(SearchProvider):
    """ Search engine proxy, used to get search results for a query. Hides actual
    search engine used. """

    # The list of supported search engines
    _engines = {"bing" : BingSearchProvider}

    @staticmethod
    def get_supported_engines():
        return SearchProxy._engines.keys()

    def __init__(self, engine, api_key):
        self._search_provider = self._get_search_provider(engine, api_key)

    def _get_search_provider(self, engine, api_key):
        """ Returns a search provider. """

        if engine not in SearchProxy._engines:
            raise KeyError("No such engine found: " + engine)

        # Use caching
        return SearchProxy._engines[engine](api_key)

    def _normalize_query(self, query):
        """
        Normalizes query, the goal is to reduce the number of unique queries.
        """
        return re.sub('\s+', ' ', query).strip().lower()

    def search(self, query):
        """
        Returns search results for the given query. Uses search engine specified
        when object was created.
        """
        return self._search_provider.search(self._normalize_query(query))

    def __unicode__(self):
        return "Proxy"

if __name__ == "__main__":
    print "This file contains classes to work with search results"
