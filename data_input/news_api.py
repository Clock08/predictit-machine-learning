import json
import urllib.request


# Interfaces with the newsapi.org API
class NewsApi:

    def __init__(self, api_key, source):
        self.apiKey = api_key
        self.source = source

    # Retrieves articles from source
    def get_articles(self, sort='latest'):
        request_uri = "https://newsapi.org/v1/articles"
        request_uri += "?apiKey=" + self.apiKey
        request_uri += "&source=" + self.source
        request_uri += "&sortBy=" + sort

        response = urllib.request.urlopen(request_uri).read()
        return json.loads(response)['articles']
