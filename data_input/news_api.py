import json
import urllib3.request


# Interfaces with the newsapi.org API
class NewsApi:

    def __init__(self, api_key, source):
        self.apiKey = api_key
        self.source = source
        self.http = urllib3.PoolManager()

    # Retrieves articles from source
    def get_articles(self, sort='latest'):
        request_uri = "https://newsapi.org/v1/articles"
        request_uri += "?apiKey=" + self.apiKey
        request_uri += "&source=" + self.source
        request_uri += "&sortBy=" + sort

        response = self.http.request("GET", request_uri)
        jsonobj = json.loads(response.data.decode("utf-8"))
        if not jsonobj["status"] == "error":
            return jsonobj["articles"]
        else:
            print("Error: the source \'" + self.source + "\' cannot be sorted by \'latest.\'"
                + " Changing the sort to \'top\'")
            return self.get_articles(sort='top')
