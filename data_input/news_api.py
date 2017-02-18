import json
import urllib.request

class NewsApi:
    def __init__(self, apiKey, source):
        self.apiKey = apiKey
        self.source = source

    def getArticles(self, sort='latest'):
        requestUri = "https://newsapi.org/v1/articles"
        requestUri += "?apiKey=" + self.apiKey
        requestUri += "&source=" + self.source
        requestUri += "&sortBy=" + sort

        response = urllib.request.urlopen(requestUri).read()
        return json.loads(response)['articles']
