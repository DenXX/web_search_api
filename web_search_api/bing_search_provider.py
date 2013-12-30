import urllib
import urllib2

# Python 2.6 has json built in, 2.5 needs simplejson
try:
    import json
except ImportError:
    import simplejson as json

from search_provider import SearchProvider, SearchResult, Serp

class BingSearchProvider(SearchProvider):
    """ Extracts search results from Bing search engine. """

    _api_url_template="https://api.datamarket.azure.com/Bing/Search/Web?"
    _params={"$format":"json",
             "Options":"'EnableHighlighting'"}

    def __init__(self, api_key):
        self._api_key = api_key

    def search(self, query, verbose=False):
        BingSearchProvider._params["Query"] = "'" + query + "'"
        url = BingSearchProvider._api_url_template + \
            urllib.urlencode(BingSearchProvider._params)
        req = urllib2.Request(url)
        password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_manager.add_password(None, url, '', self._api_key)
        auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
        opener = urllib2.build_opener(auth_manager)
        urllib2.install_opener(opener)
        handler = urllib2.urlopen(req)
        json_results = handler.read()
        if verbose:
            print json_results
        results = json.loads(json_results)['d']['results']
        return Serp(query,
            [SearchResult(self.clean(r["Url"]),
                          self.clean(r["DisplayUrl"]),
                          self.clean(r["Title"]),
                          self.clean(r["Description"])) for r in results])

    def clean(self, text):
        """
        Replace some service chars sequences with more appropriate text. E.g.
        \ue000 with <strong>, etc.
        """
        return text.replace(u'\ue000', u'<strong>'). \
                    replace(u'\ue001', u'</strong>')

    def __unicode__(self):
        """
        Returns the name of the search engine. Used for caching.
        """
        return u'BING'
