#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implements base SearchResult and Serp (search engine results page) classes.

    Copyright (C) 2013 Denis Savenkov <denissavenkov@gmail.com>
"""

from abc import abstractmethod

class SearchResult:
    """ Represents one web search result """

    def __init__(self, url, display_url, title, snippet):
        self._url = url
        self._display_url = display_url
        self._title = title
        self._snippet = snippet

    @property
    def url(self):
        return self._url

    @property
    def safe_url(self):
        return self._url.replace('://','/')

    @property
    def display_url(self):
        return self._display_url

    @property
    def title(self):
        return self._title

    @property
    def snippet(self):
        return self._snippet

    def __unicode__(self):
        return self.title + u'\n' + self.display_url + '\n' + self.snippet

    def __repr__(self):
        return unicode(self)


class Serp:
    """ Represents a collection of results returned by a search engine. """

    def __init__(self, query, results):
        self.id = None
        self.query = query
        self.results = []
        for result in results:
            self.add_result(result)

    def add_result(self, result):
        """ Adds a search result to the list of results """
        assert isinstance(result, SearchResult)
        self.results.append(result)

    def __getitem__(self, index):
        return self.results[index]

    def __iter__(self):
        """ Allows iterating over search results """
        for result in self.results:
            yield result

    def __len__(self):
        return len(self.results)

    def __unicode__(self):
        res_str = u''
        rank = 1
        for res in self:
            res_str += unicode(rank) + u'. ' + unicode(res)
            res_str += u'\n'
            rank += 1
        return res_str

    def __repr__(self):
        return unicode(self).encode('utf-8')

class SearchProvider:
    """ Abstract class for all search providers. """
    @abstractmethod
    def search(self, query):
        return None

    @abstractmethod
    def __unicode__(self):
        return ""
